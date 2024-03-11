resource "helm_release" "minio-operator" {
    repository       = "https://operator.min.io"
    chart            = "operator"
    name             = "operator"
    namespace        = "deepstorage"
    create_namespace = true
    values           = [file("values/minio-operator.yaml")]
}

resource "helm_release" "minio-tenant" {
    repository       = "https://operator.min.io"
    chart            = "tenant"
    name             = "tenant"
    namespace        = "deepstorage"
    create_namespace = true
    values           = [file("values/minio-tenant.yaml")]
    depends_on       = [helm_release.minio-operator]
}

resource "helm_release" "hive-metastore" {
    repository       = "./"
    chart            = "hive-metastore-chart"
    name             = "hive-metastore"
    namespace        = "metastore"
    create_namespace = true
    depends_on       = [helm_release.minio-tenant]
}

resource "helm_release" "trino" {
    repository       = "https://trinodb.github.io/charts"
    chart            = "trino"
    name             = "trino"
    namespace        = "trino"
    create_namespace = true
    values           = [file("values/trino.yaml")]
    depends_on       = [helm_release.hive-metastore]
}

resource "helm_release" "airflow" {
    repository       = "https://airflow.apache.org"
    chart            = "airflow"
    name             = "airflow"
    namespace        = "orchestration"
    create_namespace = true
    values           = [file("values/airflow.yaml")]
}
