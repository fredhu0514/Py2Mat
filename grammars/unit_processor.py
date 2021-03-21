"""
This is the file process single unit, currently have array
"""

import re

from processor import data_frame_separator as ds

class UnitProcess:
    @classmethod
    def separation(cls, raw_line):
        if (len(raw_line) > 0) and re.match("[a-zA-Z]", raw_line[0]):
            array_objects = re.finditer("\[(.*?)\]", raw_line)
            if array_objects:
                reverse_array_objects = []
                for obj in array_objects:
                    reverse_array_objects.append(obj)
                return cls.translate_array(reverse_array_objects, raw_line)
            else:
                return raw_line
        else:
            return raw_line

    @classmethod
    def translate_array(cls, reverse_array_objects, raw_line):
        for _ in range(len(reverse_array_objects)):
            cur_obj = reverse_array_objects.pop()
            rightmost_interval = cur_obj.span()
            content = raw_line[rightmost_interval[0]:rightmost_interval[1]]
            if not ("'" in content or '"' in content):
                raw_line = f"{raw_line[0:rightmost_interval[0]]}(({ds.Separator.separate(raw_line[(rightmost_interval[0] + 1):(rightmost_interval[1] - 1)], False)[0]}) + 1){raw_line[(rightmost_interval[1]):len(raw_line)]}"
        return raw_line

if __name__ == "__main__":
    print(UnitProcess.separation("a = arr[a ** (c + 2)]"))
