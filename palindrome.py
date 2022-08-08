# Los palindromos son palabras que se leen igual al derecho y al revés

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    #El usar [::-1] permite dar vuelta a la cadena de caracteres
    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()