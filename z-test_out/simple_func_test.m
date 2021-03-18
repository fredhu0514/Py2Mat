function [c, d] = hello()
    i = 0
    c = 1
    d = 2
    while i < 10
        c = c + i
        d = d + c
        if i >= 12
            return
end
        i = i + 1
end
    return
end
