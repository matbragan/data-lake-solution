# GitOps using ArgoCD

### Install
- [Helm](https://helm.sh/docs/intro/install/)
- [ArgoCD](https://argo-cd.readthedocs.io/en/stable/cli_installation/)

### Repos
~~~sh
helm repo add argo https://argoproj.github.io/argo-helm
~~~

### Build
~~~sh
terraform init
terraform apply
~~~

### Configure

#### Open ArgoCD to external id
~~~sh
kubectl patch svc argocd-server -n gitops -p '{"spec": {"type": "LoadBalancer"}}'
~~~

#### Get ArgoCD external id
~~~sh
kubectl get svc argocd-server -n gitops
~~~

#### Get ArgoCD login password, the user name is admin
~~~sh
kubectl -n gitops get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
~~~

#### Log in ArcoCD CLI
~~~sh
argocd login "<external_id>" --username "admin" --password "<pwd>" --insecure
~~~

#### Add k8s cluster to ArgoCD
~~~sh
argocd cluster add "DataLake"
~~~
