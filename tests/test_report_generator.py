from report_generator import generate_average_report
from .test_data import sample_logs

def test_average_report():
    logs = sample_logs()
    report = generate_average_report(logs)
    
    assert "/users" in report
    assert "2" in report
    assert "0.100s" in report
    assert "/products" in report
    assert "1" in report
    assert "0.450s" in report
