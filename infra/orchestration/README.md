# Orchestration Deployment

### Build
~~~sh
kubectl create namespace orchestration
kubectl apply -f git-credentials-secret.yaml --namespace orchestration

terraform init
terraform apply
~~~

### Useful links
- [Airflow Helm Chart doc](https://airflow.apache.org/docs/helm-chart/stable/index.html)
- [Airflow Helm Chart package](https://artifacthub.io/packages/helm/apache-airflow/airflow)
