# 🌸 Iris Species Prediction API

## 🎯 Assignment Objective

Develop and integrate a **continuous deployment script using CML** for building the Iris API using Docker and deploying it into **Kubernetes**.

---

## 📋 Table of Contents

* [Project Overview](#project-overview)
* [Deployment](#deployment)

  * [CI/CD with GitHub Actions](#cicd-with-github-actions)
  * [Kubernetes on GKE](#kubernetes-on-gke)
* [Dependencies](#dependencies)

---

## 📌 Project Overview

The core of this project is a **classification model** that predicts one of the three Iris species from four input features:

* 🌱 Sepal Length (cm)
* 🌿 Sepal Width (cm)
* 🌺 Petal Length (cm)
* 🌸 Petal Width (cm)

The model is served via a **FastAPI** application, containerized using **Docker**, and deployed to a **GKE (Google Kubernetes Engine)** cluster.

---

## 🚀 Deployment

### 🔄 CI/CD with GitHub Actions

The `deployment.yml` file in the `.github/workflows` directory defines a CI/CD pipeline that automates the deployment process.

On every push to the `master` branch, the following steps are executed:

1. **Checkout code**: The repository code is checked out.
2. **Set up gcloud CLI**: Configures the Google Cloud CLI.
3. **Authenticate and Set up GKE Auth Plugin**: Authenticates with Google Cloud using a service account key stored in GitHub Secrets.
4. **Configure Docker**: Enables Docker to use **Google Artifact Registry**.
5. **Build and Tag Docker image**: Builds a Docker image of the FastAPI application.
6. **Push Docker image to Artifact Registry**: Uploads the image to Google Artifact Registry.
7. **Get GKE cluster credentials**: Authenticates with the GKE cluster.
8. **Deploy to GKE**: Applies the Kubernetes manifests from the `k8/` directory to deploy the application.
9. **Run smoke test**: Performs a basic live endpoint check to verify successful deployment.

---

### ☸️ Kubernetes on GKE

The `k8/` directory contains the Kubernetes configuration files:

* **`deployement.yml`**: Defines the Deployment resource that manages the pods running the app container.
* **`service.yml`**: Defines the Service resource that exposes the application via a **LoadBalancer** to the internet.

---

## 📦 Dependencies

The project dependencies are listed in the `requirements.txt` file:

* `pandas`
* `numpy`
* `fastapi`
* `scikit-learn`
* `joblib`
* `uvicorn`

---


