def make_repeater_off(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string  * n
    return repeater

def run():
    repeat_5 = make_repeater_off(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_off(10)
    print(repeat_10("Platzi"))

if __name__ == "__main__":
    run()