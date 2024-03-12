resource "null_resource" "gitsync-credentials" {
    provisioner "local-exec" {
        command = "kubectl create namespace orchestration && kubectl apply -f gitsync-credentials.yaml --namespace orchestration"
    }
}

resource "helm_release" "airflow" {
    depends_on       = [null_resource.gitsync-credentials]
    repository       = "https://airflow.apache.org"
    chart            = "airflow"
    name             = "airflow"
    namespace        = "orchestration"
    values           = [file("values/airflow.yaml")]
    timeout          = 600
}
