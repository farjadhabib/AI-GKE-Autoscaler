import google.auth
from google.cloud.container_v1 import ClusterManagerClient

def scale_gke_cluster(project_id, zone, cluster_id, node_count):
    credentials, project = google.auth.default()
    client = ClusterManagerClient(credentials=credentials)

    cluster = client.get_cluster(project_id, zone, cluster_id)
    cluster.node_pools[0].initial_node_count = node_count

    client.update_cluster(project_id, zone, cluster_id, cluster)
    print(f"Scaled cluster {cluster_id} to {node_count} nodes")

if __name__ == "__main__":
    scale_gke_cluster("your-project-id", "us-central1", "your-cluster-id", 5)
