Package and install the helm chart

## Task

run the below command to verify the configuration is correct, navigate to the Helm duirctory where the Chart.yaml exsist:

helm lint{{execute}}

outpot should be as the below:
==> Linting .
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, no failures

in your testapi_chart directory to make sure everything is ok. If everything is good, you can package the chart as a release by running :

helm package testapi-chart --debug {{execute}}

I like to add the --debug flag to see the output of the packaged chart. Output should look similar to the following

Saved /Users/daemonza/testapi/testapi-chart/testapi-chart-0.0.1.tgz to current directory
Saved /Users/daemonza/testapi/testapi-chart/testapi-chart-0.0.1.tgz to /Users/daemonza/.helm/repository/local

From that we can see that the chart is placed in our current directory as well as in our local helm repository. To deploy this release, we can point helm directly to the chart file as follows :

helm install testapi-chart-0.1.0.tgz {{execute}}

And your output should look similar to the following :

NAME:   ordered-quoll
LAST DEPLOYED: Wed Mar  1 09:39:48 2017
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Service
NAME                       CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
ordered-quoll-testapi-ch   10.0.0.133   <none>        80/TCP    0s

==> extensions/Deployment
NAME                       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
ordered-quoll-testapi-ch   2         2         2            0           0s


NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app=ordered-quoll-testapi-ch" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80
  
list the deployed packages with their release versions by running :

helm ls {{execute}}

Which should return output similar to the following

NAME        	REVISION	UPDATED                 	STATUS  	CHART
ordered-quoll	1       	Wed Mar  1 11:48:52 2017	DEPLOYED	testapi-chart-0.1.0
