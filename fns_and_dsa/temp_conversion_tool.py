FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError(
                "Invalid temperature. Please enter a numeric value.")

        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        converted_temp = None
        original_unit = ""
        target_unit = ""

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            original_unit = "°F"
            target_unit = "°C"
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            original_unit = "°C"
            target_unit = "°F"
        else:
            print("Invalid unit input. Please enter 'C' or 'F'.")
            return

        if converted_temp is not None:
            print(f"{temperature}{original_unit} is {converted_temp}{target_unit}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
