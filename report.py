from check_service import check_service



def print_report(services):
    print("SERVICES INFORMATION")
    print("-" * 20)
    for service in services:
        check_service(service["name"], service["status"])




