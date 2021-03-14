from processor import filter, data_frame_separator

COMMENT_MODE = [0] # 0 off 1 on

class CoreProcessor:
    @classmethod
    def inline_process(cls, raw_string, comment_mode=False):
        whites, line = filter.Filter.space_tab_filter(raw_string)
        record = data_frame_separator.Separator.separate(line, comment_mode)
        # print("2DEBUG", record[1], record[0])
        if record[1] == 1:
            COMMENT_MODE[0] = COMMENT_MODE[0] ^ 1
        return whites[0]*'\t' + whites[1]*' ' + record[0]

    @classmethod
    def frame_process(cls, line):
        if COMMENT_MODE[0] == 1:
            return cls.inline_process(raw_string=line, comment_mode=True)
        else:
            return cls.inline_process(raw_string=line, comment_mode=False)




if __name__ == "__main__":
    print(CoreProcessor.inline_process("   'HELLO' = 13 ** 2\n"))