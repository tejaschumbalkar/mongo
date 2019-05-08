import subprocess
from subprocess import check_output
from flask import Flask, jsonify
import json


app = Flask(__name__)

@app.route('/kube-api/graph', methods=['GET']) # http://localhost:5000/kube-api/graph
def get_graph():

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
    
    return jsonify({'metric': result})

if __name__ == '__main__':
    app.run(debug=True)
