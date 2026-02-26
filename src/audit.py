from kubernetes import client, config
from kubernetes.client.rest import ApiException

def main():

    try:
        config.load_kube_config()
        print("✅ Successfully connected to the Holodeck Cluster")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        return

    v1 = client.CoreV1Api()
    
    print("\n--- Scanning Cluster Health ---")
  
    pods = v1.list_pod_for_all_namespaces(watch=False)
    
    for pod in pods.items:
        name = pod.metadata.name
        status = pod.status.phase
        
        if status not in ["Running", "Succeeded"]:
            print(f"⚠️ Alert: Pod {name} is in state: {status}")

if __name__ == "__main__":
    main()