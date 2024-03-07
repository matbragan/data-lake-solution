# Plataform Deployment

### Build
~~~sh
terraform init
terraform apply
~~~

### Expose the MinIO tenant console
~~~sh
kubectl port-forward svc/datalake-console -n minio-tenant 9090:9090
~~~
Now you can connect to the MinIO console at http://localhost:9090, with credentials past in minion-tenant.yaml value.

### Expose Trino coordinator
~~~sh
POD_NAME=$(kubectl get pods -n trino -l "app=trino,release=trino,component=coordinator" -o name)
kubectl port-forward -n trino $POD_NAME 8080:8080
~~~
Now you can connect to the Trino coordinator at http://localhost:8080, with trino user.

### Useful links
- [Trino Helm](https://trino.io/docs/current/installation/kubernetes.html#creating-your-own-yaml)
- [MinIO Operator Helm](https://min.io/docs/minio/kubernetes/upstream/operations/install-deploy-manage/deploy-operator-helm.html)
- [MinIO Tenant Helm](https://min.io/docs/minio/kubernetes/openshift/operations/install-deploy-manage/deploy-minio-tenant-helm.html)
- [Helm Provider Terraform](https://registry.terraform.io/providers/hashicorp/helm/latest/docs)