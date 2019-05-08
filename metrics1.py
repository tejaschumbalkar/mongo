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

a = check_output(["./cpu.sh"])

data = a.split('\n')
result = []

for line in data:
  resul = {}
  if line != '':
    line = line.split(':')
    resul['node'] = line[0]
    #print(line[0])
    metric = line[1].split(',')

    metric[0] = metric[0].strip().split('%')[0]
    resul['cpu'] = metric[0]
    metric[1] = metric[1].strip().split('%')[0]
    resul['memory'] = metric[1]
    result.append(resul)
  
print(result)


