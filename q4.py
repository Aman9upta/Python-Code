def change_string(s):
    if s:
        s = "x" + s[1:]
        print("inside function:", s)
        original = "hello"
        change_string(original)
        print("outside function:", original)