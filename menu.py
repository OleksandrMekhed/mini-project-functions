from services import services, get_all_services, get_one_service
from report import print_report


def menu():
    while True:
        print("-" * 30)
        print("--- Welcome to the menu ---")
        print("1. Show all services")
        print("2. Show one service")
        print("3. Show report")
        print("4. Exit")
        print("-" * 30)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            get_all_services(services)

        elif choice == 2:
            get_one_service(services)

        elif choice == 3:
            print_report(services)
        elif choice == 4:
            print("Services Stopped...")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")