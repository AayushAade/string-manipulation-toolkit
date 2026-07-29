from transform import to_uppercase, to_lowercase, merge_strings


def main():
    try:
        text = input("Enter a string: ")

        print("Uppercase:", to_uppercase(text))
        print("Lowercase:", to_lowercase(text))

        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        separator = input("Enter separator (optional): ")

        print("Merged string:", merge_strings(str1, str2, separator))
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")


if __name__ == "__main__":
    main()