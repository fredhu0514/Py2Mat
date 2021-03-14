"""
This file creates matlab file with a given list of string and output as a file.
"""

class WriteMatlabFile:
    @classmethod
    def list2file(cls, string_list, path):
        f = open(path, "w")
        f.writelines(string_list)
        f.close()
