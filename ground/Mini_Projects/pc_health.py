#!/bin/env/ python3
import shutil
import psutil
def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    freepersent=du.free/du.total*100
    return freepersent >=20
def cpu_usage_check():
    print("please wait for 10 second to diagonise the system....")
    cpu=psutil.cpu_percent(10)
    return cpu <= 50
if not check_disk_usage("/") or not cpu_usage_check():
    print("ERROR!")
else:
    print("Every Think is ok")

