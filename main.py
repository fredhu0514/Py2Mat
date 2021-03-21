import processor.read_python_file as pr
import processor.write_matlab_file as pw
import processor.core_processor as pc


def run(file_name):
    python_data = pr.ParsePythonFile.file2list("./z-test_in/" + file_name + ".py")
    python_data.append("EOF")
    matlab_data = []
    pc.CoreProcessor.frame_process(python_data, matlab_data)
    print(matlab_data.pop())
    pw.WriteMatlabFile.list2file(matlab_data, "./z-test_out/" + file_name + ".m")


if __name__ == "__main__":
    primitive_data_type = "primitive_data_type"
    operations = "operations"
    comments = "simple_comments_test"
    indentation = "indentation_if_test"
    while_loop = "while_loop_test"
    complex_func_test = "complex_func_test"
    simple_func_test = "simple_func_test"
    test_file = "test_file"
    array_test = "array_test"
    run(array_test)
