#!/usr/bin/env python3

#Author ID: dmuhammad4

import subprocess

def free_space():
    process = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], 
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, 
                                shell=True)
    output = process.communicate()
    return output[0].decode('utf-8').strip()
    
if __name__ == '__main__':
    print(free_space())