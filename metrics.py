import subprocess
from subprocess import check_output

'''
kubernetes-sdn-master: 24% CPU, 0% memory
slave01: 0% CPU, 0% memory
slave02: 0% CPU, 0% memory
slave03: 0% CPU, 0% memory
Average usage: 6% CPU, 0% memory.
'''
result = {}
#file_ = open("metric_result.txt", "w")
#a = subprocess.call('./cpu.sh')
a = check_output(["./cpu.sh"])
#subprocess.Popen("./cpu.sh", stdout=a)
#print(type(a))

print(a)
'''
for line in a:
    print(line)
'''


