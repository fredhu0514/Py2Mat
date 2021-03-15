from processor import filter, data_frame_separator

COMMENT_MODE = [0] # 0 off 1 on

RECURSIVE_LAYER = {0:0}
CUR_MAX_LAYER = [0]
PREV_INDENTATION = 0

def filter_diction(dict, func):
    new_dict = {}
    for i in dict:
        if func(i):
            new_dict.update({i:dict[i]})
    return new_dict

def empty_line(line):
    if line.replace(" ", "").replace("\t", "").replace("\n", "") == "":
        return True
    else:
        return False

def spaces_indentation(white):
    return white[0]*'\t' + white[1]*' '

class CoreProcessor:
    @classmethod
    def inline_process(cls, raw_string, comment_mode=False):
        global COMMENT_MODE
        whites, line = filter.Filter.space_tab_filter(raw_string)
        record = data_frame_separator.Separator.separate(line, comment_mode)
        if record[1] == 1: # Decide if the comment mode is changed (1 is on, 0 other wise)
            COMMENT_MODE[0] = COMMENT_MODE[0] ^ 1
        return whites[0]*'\t' + whites[1]*' ' + record[0]

    @classmethod
    def frame_process(cls, python_data, matlab_data):
        global COMMENT_MODE
        global RECURSIVE_LAYER
        global CUR_MAX_LAYER
        global PREV_INDENTATION

        for python_line in python_data:

            if COMMENT_MODE[0] == 1:
                matlab_data.append(cls.inline_process(raw_string=python_line, comment_mode=True))
            else:
                if empty_line(python_line):
                    matlab_data.append(python_line)
                else:
                    whites, line = filter.Filter.space_tab_filter(python_line)
                    cur_indentation = whites[0]*4 + whites[1]
                    if ((len(line) >= 2 and line[0:2] in ["if"])
                        or (len(line) >= 3 and line[0:3] in ["def", "for"])
                        or (len(line) >= 5 and line[0:5] in ["while"])):
                        CUR_MAX_LAYER[0] += 1
                        RECURSIVE_LAYER.update({cur_indentation:CUR_MAX_LAYER[0]})
                        matlab_data.append(spaces_indentation(whites) + data_frame_separator.Separator.frame_separate(line=line)[0])
                    else:
                        if (len(line) >= 4 and line[0:4] in ["else", "elif"]):
                            if cur_indentation == max(RECURSIVE_LAYER):
                                matlab_data.append(spaces_indentation(whites) + data_frame_separator.Separator.frame_separate(line=line)[0])
                            else:
                                cur_layer = RECURSIVE_LAYER[cur_indentation]
                                diff_layers = CUR_MAX_LAYER[0] - cur_layer
                                for i in range(diff_layers):
                                    matlab_data.append("end\n")
                                CUR_MAX_LAYER[0] = cur_layer
                                RECURSIVE_LAYER = filter_diction(RECURSIVE_LAYER, lambda x: x <= cur_indentation)
                                matlab_data.append(spaces_indentation(whites) +
                                                   data_frame_separator.Separator.frame_separate(line=line)[0])
                        elif cur_indentation <= max(RECURSIVE_LAYER) and cur_indentation < PREV_INDENTATION:
                            cur_layer = RECURSIVE_LAYER[cur_indentation] - 1
                            diff_layers = CUR_MAX_LAYER[0] - cur_layer # numbers of end need to be added
                            for i in range(diff_layers):
                                matlab_data.append("end\n")
                            CUR_MAX_LAYER[0] = cur_layer
                            RECURSIVE_LAYER = filter_diction(RECURSIVE_LAYER, lambda x: x <= cur_indentation)
                            matlab_data.append(cls.inline_process(raw_string=python_line, comment_mode=False))
                        else:
                            matlab_data.append(cls.inline_process(raw_string=python_line, comment_mode=False))
                    PREV_INDENTATION = cur_indentation
            # print("DEBUG", CUR_MAX_LAYER, RECURSIVE_LAYER, python_line, "END")
            # print("***********************************************************")









if __name__ == "__main__":
    print(CoreProcessor.inline_process("   'HELLO' = 13 ** 2\n"))