## Iris Species Prediction API 
#### Assignment Objective
Develop and integrate continuous deployment script using CML for building the iris API using docker and deploying it into Kubernetes

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Deployment](#deployment)
  - [CI/CD with GitHub Actions](#cicd-with-github-actions)
  - [Kubernetes on GKE](#kubernetes-on-gke)
- [Dependencies](#dependencies)

## Project Overview

The core of this project is a classification model that predicts one of the three Iris species (setosa, versicolor, virginica) from four features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

The model is served via a FastAPI application, which is containerized using Docker and deployed to a GKE cluster.

## Folder Structure

.
├── .github
│ └── workflows
│ └── deployment.yml
├── k8
│ ├── deployement.yml
│ └── service.yml
├── models
│ └── iris_model.joblib
├── Dockerfile
├── deployment.sh
├── iris.csv
├── main.py
├── requirements.txt
└── train.py


## Deployment
#### CI/CD with GitHub Actions
The deployment.yml file in the .github/workflows directory defines a CI/CD pipeline that automates the deployment process. On every push to the master branch, the following steps are executed:
**Checkout code:** The repository code is checked out.
**Set up gcloud CLI:** The Google Cloud CLI is configured.
**Authenticate and Set up GKE Auth Plugin:** Authenticates with Google Cloud using a service account key stored in GitHub secrets.
**Configure Docker:** Configures Docker to use Google Artifact Registry.
**Build and Tag Docker image:** Builds a Docker image of the FastAPI application.
**Push Docker image to Artifact Registry:** Pushes the built image to Google Artifact Registry.
**Get GKE cluster credentials:** Connects to the specified GKE cluster.
**Deploy to GKE:** Applies the Kubernetes manifest files from the k8/ directory to deploy the application.
**Run smoke test:** Performs a simple test on the live endpoint to ensure it's running correctly.

#### Kubernetes on GKE
The k8/ directory contains the Kubernetes configuration files:
**deployement.yml**: Defines the Deployment resource, which manages the pods running the application container.
**service.yml:** Defines the Service resource, which exposes the application to the internet via a LoadBalancer.

## Dependencies
The project's dependencies are listed in the requirements.txt file:
**pandas**
**numpy**
**fastapi**
**scikit-learn**
**joblib**
**uvicorn**


