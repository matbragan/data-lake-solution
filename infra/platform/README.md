# Platform Deployment

### Build
~~~sh
# necessary to build airflow with gitsync
kubectl create namespace orchestration
kubectl apply -f gitsync-credentials.yaml --namespace orchestration

terraform init
terraform apply
~~~

### Expose MinIO console
~~~sh
kubectl port-forward svc/console -n deepstorage 9090:9090

# copy in clipboard the JWT
kubectl get secret/console-sa-secret -n deepstorage -o json | jq -r ".data.token" | \
base64 -d | xclip -selection clipboard
~~~
Now you can connect to the MinIO console at http://localhost:9090, with JWT previously copied.

### Expose Trino
~~~sh
POD_NAME=$(kubectl get pods -n trino -l "app=trino,release=trino,component=coordinator" \
--field-selector=status.phase=Running -o jsonpath='{.items[0].metadata.name}')

kubectl port-forward $POD_NAME -n trino 8080:8080
~~~
Now you can connect to the Trino coordinator at http://localhost:8080, with trino user.

### Useful links
- [MinIO Operator Helm](https://min.io/docs/minio/kubernetes/upstream/operations/install-deploy-manage/deploy-operator-helm.html)
- [MinIO Tenant Helm](https://min.io/docs/minio/kubernetes/openshift/operations/install-deploy-manage/deploy-minio-tenant-helm.html)
- [Trino Helm](https://trino.io/docs/current/installation/kubernetes.html#creating-your-own-yaml)
- [Airflow Helm Chart doc](https://airflow.apache.org/docs/helm-chart/stable/index.html)
- [Airflow Helm Chart package](https://artifacthub.io/packages/helm/apache-airflow/airflow)