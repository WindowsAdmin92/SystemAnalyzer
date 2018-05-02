"""The module for running Bash Scripts"""
import subprocess as s

shell = True

def disk():
    print("Disk Usage")
    print("_________________________")
    


def memory_info():
    s.call("Bash/memory.sh", shell)



def os_info():
    s.call("Bash/os.sh", shell)


def network_info():
    s.call("Bash/network.sh", shell)


