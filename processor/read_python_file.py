"""
This file parses python file with a given path and output as a list of consecutive lines.
"""


class ParsePythonFile:
    @classmethod
    def file2list(cls, path):
        f = open(path, "r")
        data = []
        for line in f.readlines():
            data.append(line)
        f.close()
        return data