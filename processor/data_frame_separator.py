from processor import core_processor as cp

from grammars import comments as cmt
from grammars import primitive_data as pd
from grammars import operations as op

NO_TYPE_FOUND = -1
NORMAL = 0
COMMENT_STATUS_CHANGE = 1


class Separator:
    @classmethod
    def separate(cls, line, cast_comments=False):
        # COMMENTS
        if line[0:3] == '"""' or line[0:3] == "'''" or line[0:1] == '#' or cast_comments:
            obj = cmt.Comment(line)
            status = NORMAL
            if obj.type == 3 or obj.type == 5:
                status = COMMENT_STATUS_CHANGE
            return obj.aim_content, status # if obj.type == 3 or 5 cast_comment = True

        # PRIMITIVE DATA
        if line[0:1] == "'" or line[0:1] == '"':
            obj = pd.String(line)
            return obj.aim_content, NORMAL
        try:
            if type(eval(line.split(' ')[0])) in [int, float, bool]:
                obj = pd.PrimitiveData(line)
                return obj.aim_content, obj.type
        # except SyntaxError or NameError:
        except Exception as e:
            if type(e) != SyntaxError and type(e) != NameError:
                raise e

        # Operations
        if line[0:1] in ["+", "-", "*", "=", "/", "&", "|", "^", "%", "!", "<", ">"] or line[0:2] in ["or", "in", "is"] or line[0:3] in ["and", "not"]:
            obj = op.Operation(line)
            return obj.aim_content, obj.type



        if line[0:3] == "def":
            pass

        if line[0:5] == "while":
            pass



        if line:
            count = 0
            while count < len(line) and line[count] != ' ':
                count += 1
            return line[0:count] + cp.CoreProcessor.inline_process(line[count:len(line)]), NO_TYPE_FOUND

        return line, NO_TYPE_FOUND


