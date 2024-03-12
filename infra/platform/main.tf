resource "helm_release" "minio-operator" {
    repository       = "https://operator.min.io"
    chart            = "operator"
    name             = "operator"
    namespace        = "deepstorage"
    create_namespace = true
    values           = [file("values/minio-operator.yaml")]
}

resource "helm_release" "minio-tenant" {
    depends_on       = [helm_release.minio-operator]
    repository       = "https://operator.min.io"
    chart            = "tenant"
    name             = "tenant"
    namespace        = "deepstorage"
    create_namespace = true
    values           = [file("values/minio-tenant.yaml")]
}

resource "helm_release" "hive-metastore" {
    depends_on       = [helm_release.minio-tenant]
    repository       = "./"
    chart            = "hive-metastore-chart"
    name             = "hive-metastore"
    namespace        = "metastore"
    create_namespace = true
}

resource "helm_release" "trino" {
    depends_on       = [helm_release.hive-metastore]
    repository       = "https://trinodb.github.io/charts"
    chart            = "trino"
    name             = "trino"
    namespace        = "trino"
    create_namespace = true
    values           = [file("values/trino.yaml")]
}

resource "null_resource" "gitsync-credentials" {
    depends_on  = [helm_release.trino]
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
    create_namespace = true
    values           = [file("values/airflow.yaml")]
    timeout          = 600
}
