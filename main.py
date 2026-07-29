from transform import to_uppercase, to_lowercase, merge_strings


def main():
    text = input("Enter a string: ")

    print("Uppercase:", to_uppercase(text))
    print("Lowercase:", to_lowercase(text))

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    print("Merged string:", merge_strings(str1, str2))


if __name__ == "__main__":
    main()