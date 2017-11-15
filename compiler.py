#
#  Wrap this code in a class and plan a proper error handling mechanism.
#
#  import tarfile
import subprocess

#  tar_filename = "sample.tar.gz"
#  tar = tarfile.open(tar_filename)

#  tar.extractall(path="./flask_compilo/uploads/extracts")
#  tar.close()


class Compiler:
    #  TODO: Check the path of the compiler if moved to a different server
    COMPILER_PATH = "/usr/bin/g++"

    # has_make: boolean
    def __init__(self, has_make):
        #  Use this initilize to initilize the type of compiler to use
        #  or to set a boolean if there is a make file or single cpp file.
        self.has_make = has_make

    def compile_cpp(self):
        #  file_to_compile = file
        #  executable_name =
        if not self.has_make:
            process = subprocess.Popen([self.COMPILER_PATH, "-Wall", "-o",
                                       "test", "test_cpp.cc"],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            compilation_output = process.communicate()
            if compilation_output[1]:
                print("failed to compile\n")
                print(compilation_output[1])
                return
            process = subprocess.Popen(["./test"], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            return_value = process.communicate()
            if return_value[1]:
                print("There was a runtime error!")
                print(return_value[1])
                return
            print("Success!")
            print("stdout: {0}".format(return_value[0]))

    def execute_the_binary(self, object_file):
        if object_file:
            execution_command = "./{0}".format(object_file)
            process = subprocess.Popen([execution_command],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            execution_result = process.communicate
            error = execution_result[1]
            stdOut = execution_result[0]
            if error:
                print("There was a runtime error!")
                print(error)
            elif stdOut:
                print("Success!")
                print("StdOut: {0}".format(stdOut))
