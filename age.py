from datetime import datetime, date


def calculate_age_in_years(input_date: str) -> int | None:
    # Validate input string by trying to convert to date object
    try:
        input_date_converted: date = datetime.strptime(
            input_date, "%d-%m-%Y").date()
    except:
        print("Invalid input.")
        return None

    today: date = datetime.today().date()
    age_in_years: int = today.year - input_date_converted.year

    # If we haven't reached the birthday this year, subtract a year from total
    if (today.month, today.day) < (input_date_converted.month, input_date_converted.day):
        age_in_years -= 1

    return age_in_years


def main() -> None:
    while True:
        age_in_years: int | None = calculate_age_in_years(
            input("Enter a date (dd-mm-yyyy): "))
        if age_in_years:
            break

    print(age_in_years)


if __name__ == "__main__":
    main()
