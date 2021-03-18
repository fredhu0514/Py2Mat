def hello(): # {}
    a = 3
    b = a ** 2
    def inside_func(x, y): # {c, d}
        i = 0
        while i < 5:
            x = x * i
            y = x - y
            # Update the i
            i = i + 1
        c = x
        d = y
        return c, d
    print("HELLO WORLD!")
