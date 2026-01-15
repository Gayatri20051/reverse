def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    try:
        text = input("Enter string: ")
        print("Reversed:", reverse_string(text))
    except EOFError:
        # Jenkins / non-interactive fallback
        print("Reversed:", reverse_string("hello"))
