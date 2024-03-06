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
