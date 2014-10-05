#!/usr/bin/env python
import os
import os.path
import sys

params=dict()
def main():
    input = raw_input()

    parts = input.split()
    
    for p in parts:
	keyval=p.split("=")
        params[keyval[0]] = keyval[1]

    if (params["action"] == "start") :
       start()
    elif (params["action"] == "statlog") :
       statlog()
    elif (params["action"] == "taillog") :
       taillog()
    
def start():
    require_arguments("port,version")
    cmd = "/ucic/bin/portal -q -p " + params["port"] + " start " + params["version"]
    cmd = cmd + " >/dev/null 2>&1 &"
    print cmd
    exit_code = os.system(cmd)
    if exit_code == 0:
        print "SUCCESS"
    else:
        print "ERR: " + exit_code 

def statlog():
    require_arguments("port")
    file_path = "/data/servers/portal.theubi.com_" + params["port"]+"/logs/catalina.out"
    if os.path.isfile(file_path):
        size = os.popen("stat -c %s " + file_path).read()
    else:
        size = "0"
    print size

def taillog():
    require_arguments("port,offset")
    log = os.popen("tail -c +" + params["offset"] + " /data/servers/portal.theubi.com_" + params["port"]+"/logs/catalina.out").read()
    print log

def require_arguments(argNames):
    names=argNames.split(",")
    for n in names:
        if not n in params:
            print "FAILED: parameter " + n + " is not provided"
            sys.exit(1)

if __name__ == "__main__":
    main()

