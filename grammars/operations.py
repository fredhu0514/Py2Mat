"""
This is the file describes operations.
"""

import enum

from processor import core_processor as cp


class Operation:
    @enum.unique
    class OperationType(enum.IntEnum):
        ADD = 1         # +
        SUB = 2         # -
        MUL = 3         # *
        POW = 4         # **
        DIV = 5         # /
        DFL = 6         # //
        AEQ = 7         # =
        MOD = 8         # %

        ADD_EQ = 9      # +=
        SUB_EQ = 10     # -=
        MUL_EQ = 11     # *=
        POW_EQ = 12     # **=
        DIV_EQ = 13     # /=
        DFL_EQ = 14     # //=
        MOD_EQ = 15     # %=

        BEQ = 16        # ==
        BNE = 17        # !=
        AND = 18        # &
        AND_TEXT = 19   # and
        OR = 20         # |
        OR_TEXT = 21    # or
        BLT = 22        # <
        BLE = 23        # <=
        BGT = 24        # >
        BGE = 25        # >=
        NOT_TEXT = 26   # not

        IS = 27         # is
        IN = 28         # in
        XOR = 29        # ^

    def __init__(self, line):
        self.raw_content = line
        self.type = self.type_judge(self.raw_content)
        self.aim_content = self.translate(self.type, self.raw_content)

    def type_judge(self, raw_line):
        if raw_line[0:3] == "**=":
            return self.OperationType.POW_EQ
        elif raw_line[0:3] == "//=":
            return self.OperationType.DFL_EQ
        elif raw_line[0:3] == "and":
            return self.OperationType.AND_TEXT
        elif raw_line[0:3] == "not":
            return self.OperationType.NOT_TEXT

        elif raw_line[0:2] == "**":
            return self.OperationType.POW
        elif raw_line[0:2] == "//":
            return self.OperationType.DFL
        elif raw_line[0:2] == "+=":
            return self.OperationType.ADD_EQ
        elif raw_line[0:2] == "-=":
            return self.OperationType.SUB_EQ
        elif raw_line[0:2] == "*=":
            return self.OperationType.MUL_EQ
        elif raw_line[0:2] == "/=":
            return self.OperationType.DIV_EQ
        elif raw_line[0:2] == "%=":
            return self.OperationType.MOD_EQ
        elif raw_line[0:2] == "==":
            return self.OperationType.BEQ
        elif raw_line[0:2] == "!=":
            return self.OperationType.BNE
        elif raw_line[0:2] == "or":
            return self.OperationType.OR_TEXT
        elif raw_line[0:2] == "<=":
            return self.OperationType.BLE
        elif raw_line[0:2] == ">=":
            return self.OperationType.BGE
        elif raw_line[0:2] == "is":
            return self.OperationType.IS
        elif raw_line[0:2] == "in":
            return self.OperationType.IN

        elif raw_line[0:1] == "+":
            return self.OperationType.ADD
        elif raw_line[0:1] == "-":
            return self.OperationType.SUB
        elif raw_line[0:1] == "*":
            return self.OperationType.MUL
        elif raw_line[0:1] == "/":
            return self.OperationType.DIV
        elif raw_line[0:1] == "%":
            return self.OperationType.MOD
        elif raw_line[0:1] == "=":
            return self.OperationType.AEQ
        elif raw_line[0:1] == "<":
            return self.OperationType.BLT
        elif raw_line[0:1] == ">":
            return self.OperationType.BGT
        elif raw_line[0:1] == "&":
            return self.OperationType.AND
        elif raw_line[0:1] == "|":
            return self.OperationType.OR
        elif raw_line[0:1] == "^":
            return self.OperationType.XOR
        else:
            raise Exception("No Such Operation")

    def translate(self, line_type, raw_line):
        if line_type in [self.OperationType.ADD,
                         self.OperationType.SUB,
                         self.OperationType.MUL,
                         self.OperationType.DIV,
                         self.OperationType.AEQ,
                         self.OperationType.BLT,
                         self.OperationType.BGT]:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return raw_line[0:1] + cp.CoreProcessor.inline_process(later_text)

        if line_type in [self.OperationType.BEQ,
                         self.OperationType.BNE,
                         self.OperationType.BLE,
                         self.OperationType.BGE,
                         self.OperationType.IS]:
            later_text = ''
            if len(raw_line) > 2:
                later_text = raw_line[2:len(raw_line)]
            return raw_line[0:2] + cp.CoreProcessor.inline_process(later_text)

        if line_type == self.OperationType.AND:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return "&&" + cp.CoreProcessor.inline_process(later_text)
        if line_type == self.OperationType.AND_TEXT:
            later_text = ''
            if len(raw_line) > 3:
                later_text = raw_line[3:len(raw_line)]
            return "&&" + cp.CoreProcessor.inline_process(later_text)

        if line_type == self.OperationType.OR:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return "||" + cp.CoreProcessor.inline_process(later_text)
        if line_type == self.OperationType.OR_TEXT:
            later_text = ''
            if len(raw_line) > 2:
                later_text = raw_line[2:len(raw_line)]
            return "||" + cp.CoreProcessor.inline_process(later_text)

        if line_type == self.OperationType.NOT_TEXT:
            later_text = ''
            if len(raw_line) > 3:
                later_text = raw_line[3:len(raw_line)]
            return raw_line[0:3] + cp.CoreProcessor.inline_process(later_text)

        if line_type == self.OperationType.POW:
            later_text = ''
            if len(raw_line) > 2:
                later_text = raw_line[2:len(raw_line)]
            return "^" + cp.CoreProcessor.inline_process(later_text)

        # NEEDS TO BE REBUILT A BETTER STRUCTURE
        if line_type in [self.OperationType.IN,
                         self.OperationType.DFL,
                         self.OperationType.ADD_EQ,
                         self.OperationType.SUB_EQ,
                         self.OperationType.MUL_EQ,
                         self.OperationType.DIV_EQ,
                         self.OperationType.MOD_EQ,]:
            later_text = ''
            if len(raw_line) > 2:
                later_text = raw_line[2:len(raw_line)]
            return raw_line[0:2] + cp.CoreProcessor.inline_process(later_text)
        if line_type == self.OperationType.XOR:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return "xor" + cp.CoreProcessor.inline_process(later_text)
        if line_type == self.OperationType.XOR:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return "xor" + cp.CoreProcessor.inline_process(later_text)
        if line_type == self.OperationType.MOD:
            later_text = ''
            if len(raw_line) > 1:
                later_text = raw_line[1:len(raw_line)]
            return "mod" + cp.CoreProcessor.inline_process(later_text)
        if line_type in [
            self.OperationType.DFL_EQ,
            self.OperationType.POW_EQ,]:
            later_text = ''
            if len(raw_line) > 3:
                later_text = raw_line[3:len(raw_line)]
            return raw_line[0:3] + cp.CoreProcessor.inline_process(later_text)

    def __str__(self):
        return self.aim_content

if __name__ == "__main__":
    print(Operation("+ 1 = 2"))
    print(Operation("* 1 = 2"))
    print(Operation("** 1 = 2"))
    print(Operation("/ 1 = 2"))
    print(Operation("// 1 = 2"))
    print(Operation("and 1 = 2"))
    print(Operation("& 1 = 2"))
    print(Operation("or 1 = 2"))
    print(Operation("| 1 = 2"))
    print(Operation("not 1 = 2"))
    print(Operation("is 1 = 2"))
    print(Operation("== 1 = 2"))
    print(Operation("!= 1 = 2"))
    print(Operation(">= 1 = 2"))
    print(Operation("<= 1 = 2"))
    print(Operation("< 1 = 2"))
    print(Operation("> 1 = 2"))
    print(Operation("^ 1 = 2"))
