This is the sample for using Helm 

## Task

Let's install the helm - first download it 

`curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.8.2-linux-amd64.tar.gz`{{execute}}

So before we can use helm with a kubernetes cluster, you need to install tiller on it. It's as easy as running :


`helm init`{{execute}}

verify you get the : * Happy Helming!*
