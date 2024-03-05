resource "azurerm_resource_group" "rg" {
    name     = var.resource_group_name
    location = var.resource_group_location
}

resource "azurerm_kubernetes_cluster" "k8s" {
    name                = var.cluster_name
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    dns_prefix          = "Lake"

    default_node_pool {
        name       = "lowcost"
        node_count = var.node_count
        vm_size    = var.vm_size
    }

    identity {
        type = "SystemAssigned"
    }
}