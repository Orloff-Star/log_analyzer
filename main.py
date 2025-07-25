import argparse
import json
from report_generator import generate_average_report
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='Analyze log files.')
    parser.add_argument('--file', action='append', required=True,
                        help='Path to the log file (you can specify several)')
    parser.add_argument('--report', required=True,
                        choices=['average'], help='Report type')
    parser.add_argument('--date', help='filter logs by date in format (YYYY-MM-DD)')
    return parser.parse_args()

def read_logs(file_paths, filter_date=None):
    logs = []
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            for line in f:
                record = json.loads(line)  

                if filter_date:
                    if '@timestamp' not in record:
                        continue  
                    
                    try:
                        log_time = datetime.strptime(
                            record['@timestamp'].replace('Z', '+0000'),
                            '%Y-%m-%dT%H:%M:%S%z'
                        ).date()
                    except ValueError:
                        continue 

                    if log_time != filter_date:
                        continue
                
                logs.append(record)
    return logs

def main():
    args = parse_args()
    filter_date = None
    
    if args.date:
        try:
            filter_date = datetime.strptime(args.date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            exit(1)

    logs = read_logs(args.file, filter_date)
    
    if args.report == 'average':
        report_data = generate_average_report(logs)
        print(report_data)

if __name__ == '__main__':
    main()
