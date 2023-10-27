###################################
# A+ donors can donate to: A+, AB+
# A- donors can donate to: A+, A-, AB+, AB-
# B+ donors can donate to: B+, AB+
# B - donors can donate to: B+, B-, AB+, AB-
# AB+ donors can donate to: AB+
# AB- donors can donate to: AB+, AB-
# O+ donors can donate to: A+, B+, AB+, O+
# O- donors can donate to: A+, A-, B+, B-, AB+, AB-, O+, O-
####################################


def can_donate(donor, receiver):
    # A person with none of the above factors (O-) can give blood to anyone.
    if donor == 'O-':
        return True

    # A person with antigen A may only give blood to another person with antigen A.
    if 'A' in donor and 'A' not in receiver:
        return False

    # A person with antigen B may only give blood to another person with antigen B.
    if 'B' in donor and 'B' not in receiver:
        return False

    # A person with the Rh factor may only give blood to another person with the Rh factor.
    if '+' in donor and '+' not in receiver:
        return False

    return True

def main():
    try:
        donor = input("Enter the donor's blood type (e.g., A-, B+, AB+, O-): ").strip().upper()
        receiver = input("Enter the receiver's blood type (e.g., A-, B+, AB+, O-): ").strip().upper()

        blood_type = ['A-', 'A+', 'B-', 'B+', 'AB-', 'AB+', 'O-', 'O+']
        if donor not in blood_type or receiver not in blood_type:
            print("Invalid blood type entered. Please enter a valid blood type.")
            return

        result = can_donate(donor, receiver)

        if result:
            print(f"The donor ({donor}) can safely give blood to the receiver ({receiver}).")
        else:
            print(f"The donor ({donor}) cannot give blood to the receiver ({receiver}).")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
