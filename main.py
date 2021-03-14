import processor.read_python_file as pr
import processor.write_matlab_file as pw
import processor.core_processor as pc


def run(file_name):
    python_data = pr.ParsePythonFile.file2list("./z-test_in/" + file_name + ".py")
    matlab_data = []
    for i in python_data:
        matlab_data.append(pc.CoreProcessor.frame_process(i))
    pw.WriteMatlabFile.list2file(matlab_data, "./z-test_out/" + file_name + ".m")


if __name__ == "__main__":
    filename = "primitive_data_type"
    run("simple_comments_test")
