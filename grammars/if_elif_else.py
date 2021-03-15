"""
This is the file deals if, elif, else lines
"""

import enum

from processor import core_processor as cp

class FrameIf:
    @enum.unique
    class FrameIfType(enum.IntEnum):
        IF = 1
        ELIF = 2
        ELSE = 3

    def __init__(self, line):
        self.raw_content = line
        self.type = self.type_judge(self.raw_content)
        self.aim_content = self.translate(self.type, self.raw_content)

    def type_judge(self, raw_line):
        if len(raw_line) >= 2 and raw_line[0:2] == "if":
            return self.FrameIfType.IF
        if len(raw_line) >= 4 and raw_line[0:4] == "elif":
            return self.FrameIfType.ELIF
        if len(raw_line) >= 4 and raw_line[0:4] == "else":
            return self.FrameIfType.ELSE

    def translate(self, line_type, raw_line):
        if line_type == self.FrameIfType.IF: # What if the code is something like this? Cannot handle this situation right now.
            if raw_line[-1] == '\n':
                delete_colon = raw_line[:-2:] + '\n'
            else:
                delete_colon = raw_line[:-1:] # Assume : is the last one
            return 'if' + cp.CoreProcessor.inline_process(delete_colon[2:len(delete_colon)])
        if line_type == self.FrameIfType.ELIF: # What if the code is something like this? Cannot handle this situation right now.
            if raw_line[-1] == '\n':
                delete_colon = raw_line[:-2:] + '\n'
            else:
                delete_colon = raw_line[:-1:] # Assume : is the last one
            return 'elseif' + cp.CoreProcessor.inline_process(delete_colon[4:len(delete_colon)])
        if line_type == self.FrameIfType.ELSE:
            return 'else' + cp.CoreProcessor.inline_process(raw_line[5:len(raw_line)])

    def __str__(self):
        return self.aim_content