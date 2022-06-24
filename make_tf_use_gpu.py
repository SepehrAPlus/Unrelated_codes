import os
import platform



import urllib2

def internet_on():
    #got it from unutbu in stack overflow 
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False




os_name_allowed_filter = lambda n : n == "Windows"
lib_to_remove = "tensorflow"
libs_to_install = ["tensorflow-gpu","pycuda","pip install nvidia-cudnn"]
uninsatall_command = 'pip uninstall "{lib_name}"'
install_command = 'pip install "{lib_name}"'
cmd_sender = os.popen

def uninstall_lib(lib_name):
    output = cmd_sender(uninsatall_command.format(lib_name=lib_name)).read()
    print(f"[CMD OUTPUT] : \n {output} \n {'='*15}")


def install_lib(lib_name):
    output = cmd_sender(install_command.format(lib_name=lib_name)).read()
    print(f"[CMD OUTPUT] : \n {output} \n {'='*15}")


def get_current_os_name():
    return platform.system()


def avoid_execution_on_non_windows():
    os_name = get_current_os_name()
    if os_name_allowed_filter(os_name) == False:
        print("[ERROR]: THIS CODE CAN ONLY BE USED ON WINDOWS")
    else:
        pass













if '__main__' == __name__:
    print("@Who_cares_anyway")
    avoid_execution_on_non_windows()
    uninstall_lib(lib_to_remove)
    for i1 in libs_to_install:
        install_lib(i1)
