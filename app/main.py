def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation_type, amount = line.split(",")
            if operation_type not in report:
                report[operation_type] = 0
            report[operation_type] += int(amount)

    with open(report_file_name, "a") as report_file:
        for operation_type, amount in report.items():
            report_file.write(f"{operation_type},{amount}\n")
