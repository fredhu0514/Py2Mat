"""
This is the file describes while loop.
"""

import enum

from processor import core_processor as cp

class WhileLoop:
    @enum.unique
    class WhileLoopType(enum.IntEnum):
        WHILE_LOOP = 1

    def __init__(self, line):
        self.raw_content = line
        self.type = self.WhileLoopType.WHILE_LOOP
        self.aim_content = self.translate(self.type, self.raw_content)

    def translate(self, line_type, raw_line):
        if line_type == self.WhileLoopType.WHILE_LOOP:
            # Assume that the very end of the line would be : of the functional code

            if raw_line[len(raw_line)-1] == '\n':
                raw_line = raw_line[:-2:] + '\n'
                return "while" + cp.CoreProcessor.inline_process(raw_line[5:len(raw_line)])
            elif raw_line[len(raw_line)-1] == ':':
                raw_line = raw_line[:-1:]
                return "while" + cp.CoreProcessor.inline_process(raw_line[5:len(raw_line)])
            else:
                raise Exception("Invalid while loop grammar!")
        else:
            raise Exception("Does NOT Exists WhileLoopType:", line_type, raw_line)

    def __str__(self):
        return self.aim_content


if __name__ == "__main__":
    print(WhileLoop('while a ** 0:'))
    print(WhileLoop('while a == 0:\n'))
    print(WhileLoop('while a % 0:\n'))
