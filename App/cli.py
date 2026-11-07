from App.records import (
    load_records,
    search,
    count_by,
    get_by_id
)


def main():

    records = load_records()

    while True:

        print("\n========== MINDMATE RECORD MANAGER ==========")
        print("1. Display All Records")
        print("2. Search Records")
        print("3. Count Records")
        print("4. Find Record By ID")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            for record in records:
                print(record)

        elif choice == "2":

            keyword = input("Enter keyword: ")

            results = search(records, keyword)

            for record in results:
                print(record)

            if not results:
                print("No records found.")

        elif choice == "3":

            field = input("Enter field (category/status/name): ")

            results = count_by(records, field)

            for key, value in results.items():
                print(f"{key}: {value}")

        elif choice == "4":

            try:
                record_id = int(input("Enter record ID: "))

                result = get_by_id(records, record_id)

                print(result if result else "Record not found.")

            except ValueError:
                print("Enter a valid numeric ID.")

        elif choice == "0":

            print("Thank you for using MindMate!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()