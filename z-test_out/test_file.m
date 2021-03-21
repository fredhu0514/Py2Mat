function [] = hello()
    a = 3
    b = a ^ 2
    function [c, d] = inside_func(x, y)
        i = 0
        while i < 5
            x = x * i
            y = x - y
            % Update the i
            i = i + 1
end
        c = x
        d = y
        return
end
    disp("HELLO WORLD!")
    inside_func(a, b)

end
