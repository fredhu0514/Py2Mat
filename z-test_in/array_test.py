
def a(): # {}
    arr = [0] * 10

    i = 0
    while i < len(arr):
        def foo(inp): # {out}
            out = inp
            return out
        arr[(foo(i))] = i
        i = i + 1
    # This is a test for the array and while loop and some
    # functions.
    print(arr)

if __name__ == "__main__":
    a()
