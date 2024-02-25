variable "resource_group_location" {
    type    = string
    default = "brazilsouth"
}

variable "resource_group_name" {
    type    = string
    default = "DataLakeSolution"
}

variable "cluster_name" {
    type    = string
    default = "DataLake"
}

variable "vm_size" {
    type    = string
    default = "Standard_D2_v2"
}

variable "node_count" {
    type    = number
    default = 1
}