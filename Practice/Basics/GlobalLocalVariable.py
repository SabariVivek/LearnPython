global_variable = "Sabari Vivek"  # Global Variable Declaration...


def func_1():
    local_variable = "Rocky Vivek"  # Local Variable Declaration...
    print(local_variable)


def func_2():
    print(global_variable)
    # print(local_variable) --> We cannot access local variable to outside the function...


func_1()
func_2()
