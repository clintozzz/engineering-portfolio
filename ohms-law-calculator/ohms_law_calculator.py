def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")
        except EOFError:
            print("\nError: No input detected. Program stopped.")
            exit()


print("=" * 40)
print("        OHM'S LAW CALCULATOR")
print("     by Clinto Saju — EEE Graduate")
print("=" * 40)

while True:
    print("\nWhat do you want to calculate?")
    print("1. Voltage     (V = I × R)")
    print("2. Current     (I = V ÷ R)")
    print("3. Resistance  (R = V ÷ I)")
    print("4. Power       (P = V × I)")

    while True:
        try:
            choice = input(
                "\nEnter your choice:\n"
                "1 = Voltage (Current and Resistance needed)\n"
                "2 = Current (Voltage and Resistance needed)\n"
                "3 = Resistance (Voltage and Current needed)\n"
                "4 = Power (Voltage and Current needed)\n"
                "👉 Enter 1, 2, 3, or 4: "
            )
        except EOFError:
            print("\nError: No input detected. Program stopped.")
            exit()

        if choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    if choice == "1":
        print("\nYou selected Voltage calculation.")
        print("Formula: V = I × R")
        print("You need to enter:")
        print(" - Current (I) in Amps (A)")
        print(" - Resistance (R) in Ohms (Ω)\n")

        I = get_number("Enter Current (A): ")
        R = get_number("Enter Resistance (Ω): ")

        V = I * R
        print(f"\nResult: Voltage = {V:.2f} V")

    elif choice == "2":
        print("\nYou selected Current calculation.")
        print("Formula: I = V ÷ R")
        print("You need to enter:")
        print(" - Voltage (V) in Volts (V)")
        print(" - Resistance (R) in Ohms (Ω)\n")

        V = get_number("Enter Voltage (V): ")
        R = get_number("Enter Resistance (Ω): ")

        if R == 0:
            print("\nError: Resistance cannot be zero.")
        else:
            I = V / R
            print(f"\nResult: Current = {I:.2f} A")

    elif choice == "3":
        print("\nYou selected Resistance calculation.")
        print("Formula: R = V ÷ I")
        print("You need to enter:")
        print(" - Voltage (V) in Volts (V)")
        print(" - Current (I) in Amps (A)\n")

        V = get_number("Enter Voltage (V): ")
        I = get_number("Enter Current (A): ")

        if I == 0:
            print("\nError: Current cannot be zero.")
        else:
            R = V / I
            print(f"\nResult: Resistance = {R:.2f} Ω")

    elif choice == "4":
        print("\nYou selected Power calculation.")
        print("Formula: P = V × I")
        print("You need to enter:")
        print(" - Voltage (V) in Volts (V)")
        print(" - Current (I) in Amps (A)\n")

        V = get_number("Enter Voltage (V): ")
        I = get_number("Enter Current (A): ")

        P = V * I
        print(f"\nResult: Power = {P:.2f} W")

    try:
        again = input("\nDo you want to calculate again? (y/n): ").strip().lower()
    except EOFError:
        print("\nError: No input detected. Program stopped.")
        exit()

    if again != "y":
        print("\nCalculation complete. Goodbye.")
        break