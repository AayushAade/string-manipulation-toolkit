def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Reversed string:", reverse_string(string))
