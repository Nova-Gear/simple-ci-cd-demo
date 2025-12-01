# hapus cluster dev
kind delete cluster --name dev 2>$null
# ubah context ke default
kubectl config current-context 2>$null
# hapus kubeconfig lokal supaya pasti bersih (backup dulu jika mau)
if (Test-Path $env:USERPROFILE\.kube\config) {
  Copy-Item $env:USERPROFILE\.kube\config $env:USERPROFILE\.kube\config.backup -Force
  Remove-Item $env:USERPROFILE\.kube\config -Force
}
# restart shell supaya env bersih (close/reopen PS jika perlu)

# buat cluster dev
kind create cluster --name dev --config C:\Kind\kind-cluster.yaml
# cek cluster
kubectl get nodes
# cek pod di semua namespace
kubectl get pods -A

# install argocd
# buat namespace argocd
kubectl create namespace argocd
# install argocd di namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
# cek pod di namespace argocd
kubectl -n argocd get pods
# apply argo-cd-server.yaml
kubectl apply -f ./argo-cd-server.yaml
# cek svc di namespace argocd
kubectl -n argocd get svc
# get password argocd-initial-admin-secret
$pw = kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($pw))

# apply argo-cd-app.yaml
kubectl apply -f k8s/argo-cd-app.yaml
# cek application di namespace argocd
kubectl -n argocd get applications
# cek pod di namespace default
kubectl get pods -n default
# cek svc di namespace default
kubectl get svc -n default

# Verify that the application is deployed
kubectl get nodes
kubectl -n argocd get pods
kubectl -n argocd get svc
kubectl -n argocd get applications
kubectl get pods -n default


