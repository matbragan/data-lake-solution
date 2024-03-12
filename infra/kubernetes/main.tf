resource "azurerm_resource_group" "rg" {
    name     = var.resource_group_name
    location = var.resource_group_location
}

resource "azurerm_kubernetes_cluster" "k8s" {
    name                = var.cluster_name
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    dns_prefix          = "lake"

    default_node_pool {
        name                        = "agentpool"
        node_count                  = var.node_count
        vm_size                     = var.vm_size
        temporary_name_for_rotation = "poolrotation"
    }

    identity {
        type = "SystemAssigned"
    }
}

resource "null_resource" "use-context" {
    depends_on  = [azurerm_kubernetes_cluster.k8s]
    provisioner "local-exec" {
        command = "az aks get-credentials --resource-group DataLakeSolution --name DataLake --overwrite-existing"
    }
}