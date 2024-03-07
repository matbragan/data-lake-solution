# Kubernetes with Terraform and AKS (Azure)

### Install
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

### Build

#### Azure login
~~~sh
az login
az account set --subscription <sub_id>

# get possible vm sizes
az vm list-sizes --location brazilsouth
~~~

#### Terraform
~~~sh
terraform init
terraform apply
~~~

#### Merge cluster in context
~~~sh
az aks get-credentials --resource-group DataLakeSolution --name DataLake --overwrite-existing
~~~

### Useful links
- [Terraform tutorial Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build)
- [Azure Provider doc](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)