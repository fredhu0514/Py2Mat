class Filter:
    @classmethod
    def tab_filter(cls, line):
        """
        This is the function takes single line,
         and return the num of tabs in front of the line,
         and return the content after indentations.
        """
        count = 0
        for character in line:
            if character == '\t':
                count += 1
            else:
                break
        return count, line[count:len(line)]

    @classmethod
    def white_space_filter(cls, line):
        """
        This is the class takes single line,
         and return the num of white spaces in front of the line,
         and return the content after white spaces.
        """
        count = 0
        for character in line:
            if character == ' ':
                count += 1
            else:
                break
        return count, line[count:len(line)]

    @classmethod
    def space_tab_filter(cls, line):
        """
        This is the class takes single line,
         and return the num of white spaces and num of tabs in front of the line,
         and return the content after white spaces and tabs.
        """
        tab_count = 0
        space_count = 0
        while line[0:1] == ' ' or line[0:1] == '\t':
            t_count, line = cls.tab_filter(line)
            tab_count += t_count
            s_count, line = cls.white_space_filter(line)
            space_count += s_count
        return (tab_count, space_count), line

if __name__ == "__main__":
    print(Filter.white_space_filter('          HELLO')) # 10, HELLO
    print(Filter.tab_filter('\t\t\t\t\tHELLO'))  # 5, HELLO
    print(Filter.space_tab_filter('  \t  \t  \t    \t\tHELLO'))  # 5, HELLO