# AI-Based Kubernetes Autoscaler on GKE

This repository contains an AI-driven autoscaler for Google Kubernetes Engine (GKE) that predicts workload demand and dynamically adjusts cluster resources.

## Features
- Collects historical workload metrics from GKE
- Trains an AI model (using Prophet) to predict resource demands
- Dynamically scales Kubernetes clusters based on AI forecasts
- Deploys as a microservice using Kubernetes and Google Cloud APIs

## Setup Instructions

### Prerequisites
- Python 3.x
- Google Cloud SDK (`gcloud` CLI)
- Vertex AI for model training (optional)
- Kubernetes cluster on GKE

### Install Dependencies
```sh
pip install google-cloud-monitoring google-cloud-container fbprophet pandas matplotlib flask
```

### Train AI Model
```sh
python ai_autoscaler/train_model.py
```

### Deploy Autoscaler on Kubernetes
```sh
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## License
MIT License
