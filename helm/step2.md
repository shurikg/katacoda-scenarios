Building a Helm chart

## Task

Let's see Helm in action, using a small little Go test api I created specifically for testing use cases like this, let's build a helm chart of it.



git clone `https://github.com/daemonza/testapi.git; cd testapi`{{execute}}


First create a skeleton structure chart


helm create testapi-chart{{execute}}

This will create a testapi-chart directory. Inside this directory the three files we are the most interested in for is Chart.yaml, values.yaml and NOTES.txt.

Chart.yaml describes the chart, as in it's name, description and version.
values.yaml is stores variables for the template files templates directory. If you have more complex deployment needs, that falls outside the default templates capability, edit the files in this directory. They are normal Go templates, Hugo (https://gohugo.io) which btw powers this blog, have a nice Go template primer (https://gohugo.io/templates/go-templates/), if you need more information on how to work with Go templates.
NOTES.txt is used to give information after deployment to the user that deployed the chart. For example it might explain how to use the chart, or list default settings, etc. For this post I will keep the default message in it.
Open Chart.yaml and fill out the details of the application your deploying. Using the testapi as a example, this is how my Chart.yaml looks like :

apiVersion: v1
description: A simple api for testing and debugging
name: testapi-chart
version: 0.0.1

Now open values.yaml and edit it as needed. Again, using the testapi as a example this is how my values.yaml file looks like.

 replicaCount: 2
image:
  repository: daemonza/testapi
  tag: latest
  pullPolicy: IfNotPresent
service:
  name: testapi
  type: ClusterIP
  externalPort: 80
  internalPort: 80
resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
