def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):
        for line in data_file:
            operation_type, amount = line.split(",")
            report_file.write(f"{operation_type},{amount}\n")
