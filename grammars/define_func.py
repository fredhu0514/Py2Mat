"""
This is the file describes def special word, and requires
"""

from processor import core_processor as cp
import re

class DefineFunc:
    """
    Takes arguments like
        def func(input1, input2): # ... {output1, output2, output3} ...
    -->
        function [output1, output2, output3] = func(input1, input2)

    If the function does not return
        def func(input1, input2): # ... {} ...
    -->
        function [] = func(input1, input2)
    """

    @classmethod
    def translate_def(cls, raw_line):
        split_data = raw_line.split("#")
        if len(split_data) < 2:
            raise Exception("def function invalid form")

        def_part, output_part = split_data[0], split_data[1]

        bounds = re.search("{.*}", output_part)
        if not bounds:
            raise Exception("def function invalid form, no {ouput1, ...}")
        left_bound, right_bound = bounds.span()
        output_part = output_part[left_bound:right_bound].replace("{", "").replace("}", "")
        def_part = def_part[4:len(def_part)].split(":")[0]

        return f"function [{output_part}] = {def_part}\n"

    @classmethod
    def translate_ret(cls):
        return "return\n"
