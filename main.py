import processor.read_python_file as pr
import processor.write_matlab_file as pw
import processor.core_processor as pc


def run(file_name):
    python_data = pr.ParsePythonFile.file2list("./z-test_in/" + file_name + ".py")
    matlab_data = []
    pc.CoreProcessor.frame_process(python_data, matlab_data)
    pw.WriteMatlabFile.list2file(matlab_data, "./z-test_out/" + file_name + ".m")


if __name__ == "__main__":
    primitive_data_type = "primitive_data_type"
    operations = "operations"
    comments = "simple_comments_test"
    indentation = "indentation_if_test"
    run(indentation)
