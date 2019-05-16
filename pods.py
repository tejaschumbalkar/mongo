from kubernetes import client, config


config.load_kube_config()

v1 = client.CoreV1Api()
ret = v1.list_pod_for_all_namespaces(watch=False)

result = []
for i in ret.items:
    temp ={}

    temp['name'] = i.metadata.name
    temp['namespace'] = i.metadata.namespace
    temp['timestamp'] = i.metadata.creation_timestamp
    temp['container_name'] = i.spec.containers[0].name
    temp['image_name'] = i.spec.containers[0].image
    temp['node'] = i.spec.node_name
    temp['host_ip'] = i.status.host_ip
    temp['pod_ip'] = i.status.pod_ip
    if i.spec.containers[0].ports is not None:
        temp['container_port'] = i.spec.containers[0].ports[0].container_port
        temp['protocol'] = i.spec.containers[0].ports[0].protocol
    else:
        temp['container_port'] = None
        temp['protocol'] = None

    if i.status.container_statuses is not None:
       if i.status.container_statuses[0] is not None:
           temp['start_time'] = i.status.container_statuses[0].state.running.started_at
           temp['terminated'] = i.status.container_statuses[0].state.terminated
           temp['waiting'] = i.status.container_statuses[0].state.waiting
    
    else:
        temp['start_time'] = None
        temp['terminated'] = None
        temp['waiting'] = None
          
    result.append(temp)
print(result)
#return jsonify({'metric': result})
