resource "helm_release" "minio-operator" {
    repository       = "https://operator.min.io"
    chart            = "operator"
    name             = "operator"
    namespace        = "minio-operator"
    create_namespace = true
    values           = [file("values/minio-operator.yaml")]
}

resource "helm_release" "minio-tenant" {
    repository       = "https://operator.min.io"
    chart            = "tenant"
    name             = "tenant"
    namespace        = "minio-tenant"
    create_namespace = true
    values           = [file("values/minio-tenant.yaml")]
    depends_on       = [helm_release.minio-operator]
}

resource "helm_release" "hive-metastore" {
    repository       = "./"
    chart            = "hive-metastore-chart"
    name             = "metastore"
    namespace        = "hive-metastore"
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