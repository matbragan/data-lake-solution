## Kubernetes with Terraform and AKS (Azure)

- [Building Terraform in Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started/azure-build)
- [Doc Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- Merge cluster as context in host machine:
    ~~~sh
    az aks get-credentials --resource-group DataLakeSolution --name DataLake --overwrite-existing
    ~~~