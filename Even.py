def check_even_odd(number: int) -> str:
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return "Even Number"
    return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"{number} is {check_even_odd(number)}.")
