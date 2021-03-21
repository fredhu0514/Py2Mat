from processor import core_processor as cp

from grammars import comments as cmt
from grammars import primitive_data as pd
from grammars import operations as op

from grammars import if_elif_else as iee
from grammars import while_loop as wl

from grammars import set_function as sf
from grammars import define_func as df

from grammars import unit_processor as up

EMPTY = -2
NO_TYPE_FOUND = -1
NORMAL = 0
COMMENT_STATUS_CHANGE = 1


class Separator:
    @classmethod
    def separate(cls, line, cast_comments):
        if not line:
            return line, EMPTY
        # COMMENTS
        if (len(line) >= 1 and line[0:1] == '#') or (len(line) >= 3 and (line[0:3] == '"""' or line[0:3] == "'''")):
            obj = cmt.Comment(line)
            status = NORMAL
            if obj.type == cmt.Comment.CommentType.THREE_DOUBLE_QUOTES_SEPARATE or obj.type == cmt.Comment.CommentType.THREE_SINGLE_QUOTES_SEPARATE:
                status = COMMENT_STATUS_CHANGE
            return obj.aim_content, status # if obj.type == 3 or 5 cast_comment = True

        # PRIMITIVE DATA
        if len(line) >= 1 and (line[0] == "'" or line[0] == '"'):
            obj = pd.String(line)
            return obj.aim_content, NORMAL
        try:
            if type(eval(line.split(' ')[0])) in [int, float, bool]:
                obj = pd.PrimitiveData(line)
                return obj.aim_content, NORMAL
        # except SyntaxError or NameError:
        except Exception as e:
            if type(e) != SyntaxError and type(e) != NameError:
                raise e

        # Set functions
        if len(line) >= 4 and line[0:4] == "len(":
            return sf.FuncMap.len2length(line), NORMAL
        if len(line) >= 5 and line[0:5] == "eval(":
            return sf.FuncMap.eval2eval(line), NORMAL
        if len(line) >= 5 and line[0:5] == "type(":
            return sf.FuncMap.type2class(line), NORMAL
        if len(line) >= 6 and line[0:6] == "print(":
            return sf.FuncMap.print2disp(line), NORMAL
        if len(line) >= 6 and line[0:6] == "input(":
            return sf.FuncMap.input2input(line), NORMAL

        # Operations
        if line[0:1] in ["+", "-", "*", "=", "/", "&", "|", "^", "%", "!", "<", ">"] or (len(line) >= 3 and line[0:2] in ["or", "in", "is"] and (line[2] == ' ' or line[2] == '\n')) or line[0:3] in ["and", "not"]:
            obj = op.Operation(line)
            return obj.aim_content, NORMAL

        # Return line
        if len(line) >= 6 and line[0:6] == "return" and (line[6] in ['', ' ', '\n', '\t', '#', '"', "'"]):
            return df.DefineFunc.translate_ret(), NORMAL

        if cast_comments:
            obj = cmt.Comment(line)
            status = NORMAL
            if obj.type == cmt.Comment.CommentType.THREE_DOUBLE_QUOTES_SEPARATE or obj.type == cmt.Comment.CommentType.THREE_SINGLE_QUOTES_SEPARATE:
                status = COMMENT_STATUS_CHANGE
            return obj.aim_content, status

        if line:
            count = 0
            while count < len(line) and line[count] != ' ':
                count += 1
            return up.UnitProcess.separation(line[0:count]) + cp.CoreProcessor.inline_process(line[count:len(line)], False), NO_TYPE_FOUND
        return line, NO_TYPE_FOUND

    @classmethod
    def frame_separate(cls, line):
        # print("+++++++")
        # print("DEBUG2", line, "END")
        # print("+++++++")
        if not line:
            return line, EMPTY

        if len(line) >= 3:
            if line[0:3] == 'if ':
                obj = iee.FrameIf(line)
                return obj.aim_content, NORMAL
        if len(line) >= 4:
            if line[0:4] == 'def ':
                return df.DefineFunc.translate_def(line), NORMAL
            elif line[0:4] == 'for ':
                pass
        if len(line) >= 5:
            if line[0:5] in ['elif ', 'else ']:
                obj = iee.FrameIf(line)
                return obj.aim_content, NORMAL
        if len(line) >= 6:
            if line[0:6] == 'while ':
                obj = wl.WhileLoop(line)
                return obj.aim_content, NORMAL
