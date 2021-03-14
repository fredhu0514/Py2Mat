from processor import filter, data_frame_separator

class CoreProcessor:
    @classmethod
    def inline_process(cls, raw_string):
        whites, line = filter.Filter.space_tab_filter(raw_string)
        return whites[0]*'\t' + whites[1]*' ' + data_frame_separator.Separator.separate(line)[0]




if __name__ == "__main__":
    print(CoreProcessor.inline_process("   'HELLO' = 13 ** 2\n"))