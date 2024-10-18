def match_demo_1():
    var = "abc"
    match var:
        case "a":
            print("One letter 'a'")
        case "abc":
            print("Word 'abc'")
        case _:
            print("Other sequence")

# Wywołanie funkcji
match_demo_1()
