"""
This is the file describes core functions mapping.
"""

from processor import core_processor as cp

class FuncMap:
    @classmethod
    def print2disp(cls, raw_line):
        "print( --> disp("
        return "disp(" + cp.CoreProcessor.inline_process(raw_line[6:len(raw_line)])

    @classmethod
    def type2class(cls, raw_line):
        "type( --> class("
        return "class(" + cp.CoreProcessor.inline_process(raw_line[5:len(raw_line)])

    @classmethod
    def eval2eval(cls, raw_line):
        "eval( --> eval("
        return raw_line[0:5] + cp.CoreProcessor.inline_process(raw_line[5:len(raw_line)])

    @classmethod
    def input2input(cls, raw_line):
        "input( --> input("
        return raw_line[0:6] + cp.CoreProcessor.inline_process(raw_line[6:len(raw_line)])
