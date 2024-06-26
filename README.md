# Setting Up a CI Pipeline with GitHub Actions for a Python Web Application

## Introduction

This guide provides a step-by-step tutorial on setting up a CI (Continuous Integration) pipeline using GitHub Actions for a Python web application. The pipeline automates building, testing, and deploying the application, ultimately pushing a Docker image to Docker Hub.

## Why CI/CD?

CI/CD pipelines automate the process of integrating code changes, running tests, and deploying applications. This enhances productivity, ensures consistent quality, and accelerates the delivery of applications.

## Pipeline Overview

The CI pipeline includes the following steps:

- **Build the application**: Installs dependencies required for the application.
- **Run tests**: Ensures the application functions correctly.
- **Run the application in a Docker container**: Validates that the application runs as expected.
- **Push Docker image to Docker Hub**: Makes the application available for deployment.

## Step-by-Step Guide

### Step 1: Create a GitHub Repository

Start by creating a [GitHub repository](https://github.com/new) for your Python web application.

### Step 2: Add Your Application Code

Add your application code (`app.py` and `test_app.py`) and a `requirements.txt` file for dependencies.

### Step 3: Set Up GitHub Actions Workflow

Create a `.github/workflows/ci.yml` file in your repository with the following content:

```yaml
# Path: .github/workflows/ci.yml

name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

  test:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest

    - name: Run tests
      run: pytest test_app.py

  run_docker:
    needs: test
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Build Docker image
      run: |
        docker build -t my-web-app .

    - name: Run Docker container
      run: |
        docker run -d -p 5000:5000 --name my-web-app-container my-web-app

    - name: Test Docker container
      run: |
        # Wait for the container to be ready
        for i in {1..10}; do
          curl -f http://localhost:5000 && break || sleep 5;
        done

    - name: Stop Docker container
      run: |
        docker stop my-web-app-container
        docker rm my-web-app-container

  push:
    needs: run_docker
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Login to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build Docker image
      run: |
        docker build -t ${{ secrets.DOCKER_USERNAME }}/my-web-app:latest .

    - name: Push Docker image to Docker Hub
      run: |
        docker push ${{ secrets.DOCKER_USERNAME }}/my-web-app:latest
'''


#### Step 4: Add Docker Hub Credentials
Add your Docker Hub credentials as secrets in your GitHub repository (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).

#### Step 5: Commit and Push
Commit and push the changes to the main branch of your repository. The CI pipeline will automatically run on each push.

#### Key Takeaways
- **Automation**: This setup automates the entire process of building, testing, and deploying your application.
  
- **Quality Assurance**: Running tests ensures your application works correctly before deploying.

- **Efficiency**: Automating these tasks saves time and reduces the potential for human error.

By implementing this CI pipeline, you can ensure a consistent and reliable deployment process for your Python web applications.

#### Pipeline Overview

The CI pipeline includes the following steps:

- **Build the application**: Installs dependencies required for the application.
  
- **Run tests**: Ensures the application functions correctly.
  
- **Run the application in a Docker container**: Validates that the application runs as expected.
  
- **Push Docker image to Docker Hub**: Makes the application available for deployment.
