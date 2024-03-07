resource "helm_release" "argocd" {
    repository       = "https://argoproj.github.io/argo-helm/"
    chart            = "argo-cd"
    name             = "argocd"
    namespace        = "gitops"
    create_namespace = true
    version          = "5.38.0"
    verify           = false
    values           = [file("values.yaml")]
}