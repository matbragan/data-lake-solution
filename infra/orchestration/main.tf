resource "helm_release" "airflow" {
    repository       = "https://airflow.apache.org"
    chart            = "airflow"
    name             = "airflow"
    namespace        = "orchestration"
    create_namespace = true
    values           = [file("values.yaml")]
}