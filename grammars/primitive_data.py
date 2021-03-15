"""
This is the file describes primitive data types.
"""

import enum

from processor import core_processor as cp

class String:
    @enum.unique
    class StringType(enum.IntEnum):
        STRING_DOUBLE_QUOTE = 1
        STRING_SINGLE_QUOTE = 2

    def __init__(self, line):
        self.raw_content = line
        self.type = self.type_judge(self.raw_content)
        self.aim_content = self.translate(self.type, self.raw_content)

    def type_judge(self, raw_line):
        if raw_line[0:1] == '"':
            return self.StringType.STRING_DOUBLE_QUOTE
        elif raw_line[0:1] == "'":
            return self.StringType.STRING_SINGLE_QUOTE
        else:
            raise Exception("None String Type Applies:", raw_line)

    def translate(self, line_type, raw_line):
        if line_type == self.StringType.STRING_DOUBLE_QUOTE:
            split_data = raw_line.split('"')

            # Validate the string
            if len(split_data) <= 2:
                raise Exception("Invalid String:", raw_line)

            split_data.pop(0) # Pop the first null char
            string_data = '"' + split_data.pop(0) + '"' # Wanted content
            # Get the rest words
            if split_data:
                later_text = split_data.pop(0)
                for i in split_data:
                    later_text += '"'
                    later_text += i
            else:
                later_text = ''

            return string_data + cp.CoreProcessor.inline_process(later_text)

        elif line_type == self.StringType.STRING_SINGLE_QUOTE:
            split_data = raw_line.split("'")

            # Validate the string
            if len(split_data) <= 2:
                raise Exception("Invalid String:", raw_line)

            split_data.pop(0)  # Pop the first null char
            string_data = "'" + split_data.pop(0) + "'"  # Wanted content

            # Get the rest words
            if split_data:
                later_text = split_data.pop(0)
                for i in split_data:
                    later_text += "'"
                    later_text += i
            else:
                later_text = ''

            return string_data + cp.CoreProcessor.inline_process(later_text)

        else:
            raise Exception("Does NOT Exists StringType:", line_type, raw_line)

    def __str__(self):
        return self.aim_content

class PrimitiveData:
    @enum.unique
    class PrimitiveDataType(enum.IntEnum):
        INTEGER = 1
        FLOAT = 2
        BOOLEAN = 3

    def __init__(self, line):
        self.raw_content = line
        self.type = self.type_judge(self.raw_content)
        self.aim_content = self.translate(self.type, self.raw_content)

    def type_judge(self, raw_line):
        categ = type(eval(raw_line.split(' ')[0]))
        if categ == int:
            return self.PrimitiveDataType.INTEGER
        elif categ == float:
            return self.PrimitiveDataType.FLOAT
        elif categ == bool:
            return self.PrimitiveDataType.BOOLEAN

    def translate(self, line_type, raw_line):
        split_data = raw_line.split(' ')
        num = split_data[0]
        split_data.pop(0)

        if split_data:
            later_text = ' ' + split_data.pop(0)
            for item in split_data:
                later_text += ' '
                later_text += item
        else:
            later_text = ''

        if line_type == self.PrimitiveDataType.INTEGER:
            return str(num) + cp.CoreProcessor.inline_process(later_text)

        elif line_type == self.PrimitiveDataType.FLOAT:
            return str(num) + cp.CoreProcessor.inline_process(later_text)

        elif line_type == self.PrimitiveDataType.BOOLEAN:
            return num.lower() + cp.CoreProcessor.inline_process(later_text)

        else:
            raise Exception("Does NOT Exists PrimitiveDataType:", line_type, raw_line)

    def __str__(self):
        return self.aim_content

if __name__ == "__main__":
    print(String('"DQ1" + "DQ2"\n'))
    print(String("'SQ1' + 'SQ2'\n"))
    print(PrimitiveData("5 ** 2 = 25\n"))
    print(PrimitiveData("5 % 2 = 2\n"))
    print(PrimitiveData("5 'An int'\n"))
    print(PrimitiveData("6.7584 'A float'\n"))
    print(PrimitiveData("True 'bool True'\n"))
    print(PrimitiveData("False 'bool False'\n"))
    # print(String('"Seriously?" """\n'))
