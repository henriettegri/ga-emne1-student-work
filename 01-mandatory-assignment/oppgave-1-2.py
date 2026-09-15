#oppgave 1.2

text = input("Enter a word or a sentence:")

if text.isspace() or text =='':
    print("Wrong input, please try again.")

else:
    print(f' Number of letters: {len(text)}')
    print(f' Text written in lower letters: {text.lower()}')
    print(f' Text reversed: {text[::-1]}')

    if "python" in text:
        print("Yes, python is present!")
    elif "Python" in text:
        print("Yes, python is present!")
    elif "PYTHON" in text:
        print("Yes, python is present!")
    else:
        print("No, python is not present!")
