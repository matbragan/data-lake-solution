# Manifests Deployment

### MinIO (deepstorage)
~~~sh
kubectl apply -f app-manifests/deepstorage/minio-operator.yaml
kubectl apply -f app-manifests/deepstorage/minio-tenant.yaml
~~~

### Hive Metastore (metastore)
~~~sh
kubectl apply -f app-manifests/metastore/hive-metastore.yaml
~~~

### Trino (warehouse)
~~~sh
kubectl apply -f app-manifests/warehouse/trino.yaml
~~~

### Airflow (orchestrator)
~~~sh
kubectl create secret generic airflow-fernet-key --from-literal=fernet-key='t5u8Dst5tkt1F5fwsxnfEwGfytY3Ry5KrP02B32mPxY=' --namespace orchestrator
kubectl apply -f git-credentials-secret.yaml --namespace orchestrator
kubectl apply -f app-manifests/orchestrator/airflow.yaml
~~~
