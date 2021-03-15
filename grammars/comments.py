"""
This is the file describes comments.
"""

import enum

from processor import core_processor as cp


class Comment:
    @enum.unique
    class CommentType(enum.IntEnum):
        CASTED = 0 # Given this line is a comment
        HASHTAG = 1 # "#"
        THREE_DOUBLE_QUOTES_INLINE = 2 # """ """
        THREE_DOUBLE_QUOTES_SEPARATE = 3 # """ \n """
        THREE_SINGLE_QUOTES_INLINE = 4  # ''' '''
        THREE_SINGLE_QUOTES_SEPARATE = 5  # ''' \n '''

    def __init__(self, line):
        self.raw_content = line
        self.type = self.type_judge(self.raw_content)
        self.aim_content = self.translate(self.type, self.raw_content)


    def type_judge(self, raw_line):
        if raw_line[0:1] == "#":
            return self.CommentType.HASHTAG
        elif raw_line[0:3] == '"""':
            if len(raw_line.split('"""')) % 2 == 1:
                return self.CommentType.THREE_DOUBLE_QUOTES_INLINE
            else:
                return self.CommentType.THREE_DOUBLE_QUOTES_SEPARATE
        elif raw_line[0:3] == "'''":
            if len(raw_line.split("'''")) % 2 == 1:
                return self.CommentType.THREE_SINGLE_QUOTES_INLINE
            else:
                return self.CommentType.THREE_SINGLE_QUOTES_SEPARATE
        return self.CommentType.CASTED

    def translate(self, line_type, raw_line):
        if line_type == self.CommentType.CASTED:
            return "% " + raw_line

        elif line_type == self.CommentType.HASHTAG:
            return "%" + raw_line[1:len(raw_line)]

        elif line_type == self.CommentType.THREE_DOUBLE_QUOTES_INLINE:
            split_data = raw_line.split('"""')
            split_data.pop(0)
            cur_content = split_data.pop(0)

            if split_data:
                later_text = split_data.pop(0)
                for i in split_data:
                    later_text += '"""'
                    later_text += i
            else:
                later_text = ''

            return "%" + cur_content + cp.CoreProcessor.inline_process(later_text)

        elif line_type == self.CommentType.THREE_DOUBLE_QUOTES_SEPARATE:
            return "%" + cp.CoreProcessor.inline_process(raw_line[3:len(raw_line)])

        elif line_type == self.CommentType.THREE_SINGLE_QUOTES_INLINE:
            split_data = raw_line.split("'''")
            split_data.pop(0)
            cur_content = split_data.pop(0)

            if split_data:
                later_text = split_data.pop(0)
                for i in split_data:
                    later_text += "'''"
                    later_text += i
            else:
                later_text = ''

            return "%" + cur_content + cp.CoreProcessor.inline_process(later_text)

        elif line_type == self.CommentType.THREE_SINGLE_QUOTES_SEPARATE:
            return "%" + cp.CoreProcessor.inline_process(raw_line[3:len(raw_line)])

        else:
            raise Exception("Does NOT Exists CommentType:", line_type, raw_line)

    def __str__(self):
        return self.aim_content

if __name__ == "__main__":
    print("###################################")
    print(Comment("Cast Comments lc\n"))
    print(Comment("Cast Comments"))
    print("###################################")
    print(Comment("# Hashtag Comments lc\n"))
    print(Comment("# Hashtag Comments"))
    print("###################################")
    print(Comment('""" Inline Comments DQ lc """ # Second Type\n'))
    print(Comment('""" Inline Comments DQ """'))
    print("###################################")
    print(Comment('""" ""\n'))
    print(Comment('"""'))
    print("###################################")
    print(Comment("''' Inline Comments SQ lc '''\n"))
    print(Comment("''' Inline Comments SQ '''"))
    print("###################################")
    print(Comment("''' lc\n"))
    print(Comment("'''"))
    print("###################################")
