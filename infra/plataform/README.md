# Plataform Deployment

### Build
~~~sh
terraform init
terraform apply
~~~

### Expose MinIO console
~~~sh
kubectl port-forward svc/console -n deepstorage 9090:9090

# copy in clipboard the JWT
kubectl get secret/console-sa-secret -n deepstorage -o json | jq -r ".data.token" | base64 -d | xclip -selection clipboard
~~~
Now you can connect to the MinIO console at http://localhost:9090, with JWT previously copied.

### Expose Trino
~~~sh
POD_NAME=$(kubectl get pods -n trino -l "app=trino,release=trino,component=coordinator" -o name)
kubectl port-forward $POD_NAME -n trino 8080:8080
~~~
Now you can connect to the Trino coordinator at http://localhost:8080, with trino user.

### Useful links
- [Trino Helm](https://trino.io/docs/current/installation/kubernetes.html#creating-your-own-yaml)
- [MinIO Operator Helm](https://min.io/docs/minio/kubernetes/upstream/operations/install-deploy-manage/deploy-operator-helm.html)
- [MinIO Tenant Helm](https://min.io/docs/minio/kubernetes/openshift/operations/install-deploy-manage/deploy-minio-tenant-helm.html)
- [Helm Provider Terraform](https://registry.terraform.io/providers/hashicorp/helm/latest/docs)