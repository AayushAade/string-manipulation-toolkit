def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    text = input("Enter a string: ")
    if is_palindrome(text):
        print("Palindrome")
    else:
        print("Not a palindrome")
