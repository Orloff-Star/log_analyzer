from tabulate import tabulate


def generate_average_report(logs):
    handler_stats = {}
    
    for log in logs:
        handler = log['url']
        time = float(log['response_time'])        
        if handler not in handler_stats:
            handler_stats[handler] = {
                'count': 0,
                'total_time': 0.0
            }        
        handler_stats[handler]['count'] += 1
        handler_stats[handler]['total_time'] += time
    
    report = []
    for handler, stats in handler_stats.items():
        avg_time = stats['total_time'] / stats['count']
        report.append([handler, stats['count'], f"{avg_time:.3f}s"])
    
    headers = ["Handler", "Count", "Average Time"]
    return tabulate(report, headers=headers, tablefmt="grid")
