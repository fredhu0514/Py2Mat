# import processor.read_python_file as pr
# import processor.write_matlab_file as pw
import processor.core_processor as pc


def test():
    print(pc.CoreProcessor.inline_process('"Seriously?" """'))


if __name__ == "__main__":
    test()
