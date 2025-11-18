
# Learn Platform Engineering, Backstage, Kubernetes, ArgoCD, Docker, GitOps, Helm, GitHub Actions & CI/CD to build IDPs

*To get a personalized course, create or/and get your ids of dockerhub and github; create a branch with my_course__%your_login_in_dockerhub%__%your_login_in_github%, wait for your branch pipeline, your personalized course is in the artifacts.*

## Glossary

ArgoCD
: Argo CD is a **declarative, GitOps continuous delivery tool for Kubernetes**.

**Backstage**
: CNF open-source **Platform Engineering framework** developed by **Spotify**, and integrating it with modern **DevOps tools** to build a fully functional **Internal Developer Platform**(IDP)

Backstage Auth & Identity
: The authentication system in Backstage serves two distinct purposes: **sign-in** and **identification** of **users**, as well as delegating access to **third-party resources**. It is possible to configure Backstage to have any number of authentication providers, but only one of these will typically be used for sign-in, with the rest being used to provide access to external resources. Built-in Athentication providers : Auth0, Atlassian, Azurz, BitBucket, Cloudflare, GitHub, GitLab, Google, Google IAP, Okta, OAuth2, OneLogine, OpenShift, VMware Cloud

Backstage Configuration
: Backstage ships with a flexible configuration system that provides a simple way to configure Backstage apps and plugins for both local development and production deployments. Configuration is stored in YAML files where the defaults are app-config.yaml and app-config.local.yaml for local overrides and app-config.<BACKSTAGE_ENV>.yaml for BACKSTAGE_ENV environment variable.

Backstage Framework CLI
: **build system and tooling**, delivered primarily through the @backstage/cli package. When creating an app using @backstage/create-app, you receive a project that's already prepared with a typical setup and package scripts for executing the most common commands. *Under the hood the CLI uses **Webpack** for bundling, **Rollup** for building packages, **Jest** for testing, and **eslint** for linting*. It also includes tooling for working within Backstage apps, for example for keeping the app up to date and verifying static configuration. For a more in-depth look into the tooling, see the build system page, and for a list of commands, see the commands page.

Backstage Framework Backend System
: Provides a flexible foundation for building and extending Backstage backends. It uses a modular architecture where you can create and customize plugins, modules, and service implementations.

*Backstage Framework Frontend System*
: Provides high-level building blocks upon which this new system is built.

Backstage Framework User Interface (UI)
: built-in support for both light and dark themes, making it easy to get started with a professional look and feel. But many teams want to go further—tailoring the interface to reflect their organization’s unique brand, identity, and experience.

Backstage Integration
: Integrations allow Backstage to **read or publish data** using **external providers** such as *GitHub, GitLab, Gitea, Bitbucket, LDAP, or cloud providers*.

Backstage Kubernetes
: Tool that's designed around the **needs of service owners**, not cluster admins. Now developers can easily **check the health of their services** no matter how or where those services are deployed — whether it's on a local host for testing or in production on dozens of clusters around the world.

Backstage Notifications
: System that provides a way for plugins and external services to send notifications to Backstage users. These notifications are displayed in the dedicated page of the Backstage frontend UI or by frontend plugins per specific scenarios. Additionally, notifications can be sent to external channels (like email) via "processors" implemented within plugins.

Backstage Permissions
: Backstage can also authorize specific data, APIs, or interface actions - meaning that Backstage has the ability to enforce rules about what type of access is allowed for a given user of a system.

Backstage Plugins
: Backstage orchestrates a cohesive single-page application by seamlessly integrating various plugins.

**Backstage Software Catalog**
: **Centralized system** that keeps track of ownership and metadata **for all the software in your ecosystem** (services, websites, libraries, data pipelines, etc). The catalog is built around the concept of metadata YAML files stored together with the code, which are then harvested and visualized in Backstage.

Backstage Resolver
: Function that is responsible for creating this **user identity mapping**. Signing in a user into Backstage requires a mapping of the user identity *from* the **third-party auth provider** to a Backstage user identity.

Backstage Search
: Backstage Search lets you find the right information you are looking for in the Backstage ecosystem.


**Backstage TechDocs**
: Spotify’s homegrown docs-like-code solution built directly into Backstage. Engineers write their documentation in **Markdown** files which live together with their **code** - and with little configuration get a nice-looking doc site in Backstage.

**Backstage Software Templates**
: **Tool** that can help you **create Components** inside Backstage. By default, it has the ability to **load skeletons of code**, template in some **variables**, and then **publish** the template to some locations like GitHub or GitLab.

CD
: Continuous Deployment

CI
: Continuous Integration

DevOps
: Mouvement en ingénierie informatique et une pratique technique visant à l'unification du développement logiciel (dev) et de l'administration des infrastructures informatiques (ops), notamment l'administration système.

Docker
: Docker is a platform designed to help developers build, share, and run container applications. We handle the tedious setup, so you can focus on the code.

Docker File
: A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

Docker Containers
: A Docker container is a lightweight, standalone, and executable unit of software that encapsulates an application along with all its dependencies, such as libraries, runtime, system tools, and configurations.

Flask API
: Flask API is primarily built using the Flask framework, a lightweight and flexible **micro-framework for Python**. Flask itself was created by Armin Ronacher as part of the Pallets Projects.

IaC
: **I**nfrastructure **a**s **C**ode, is the practice of keeping all infrastructure configuration stored as code. 

**IDP**
: **I**nternal **D**eveloper **P**latform

**Ingress Controller**
: Component in Kubernetes that manages external access to services within a cluster, typically through HTTP and HTTPS. It is responsible for fulfilling the Ingress resource, which defines rules for routing traffic to different services based on the request's host and path. Common ingress controllers include NGINX and Traefik, and they often work with load balancers to handle incoming traffic effectively.

GitHub
: GitHub is a web-based platform that hosts Git repositories, providing developers with tools for version control and collaboration. It combines Git, a powerful version control system, with features that facilitate collaboration and project management.

**GitOps**
: GitOps is an operational framework that takes DevOps best practices used for application development such as version control, collaboration, compliance, and CI/CD, and applies them to infrastructure automation.

Helm
: Helm is a **package manager for Kubernetes** that simplifies the deployment and management of applications within Kubernetes clusters. It bundles Kubernetes resources into a single Helm chart.

Helm Chart
: Reusable package which includes all necessary code and resources needed to deploy an application.

kubectl
: **Command line tool** for communicating with a **Kubernetes cluster's control plane**, using the Kubernetes API.

Kubernetes
: Open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Originally developed by Google, it has become the de-facto standard for running containers at scale.

**Kubernetes local Cluster**
: A Kubernetes cluster is a **collection of machines (nodes) designed to run containerized applications**. It is the core of Kubernetes' functionality, *enabling the orchestration, scaling, and management of containers* across multiple machines, whether they are physical, virtual, on-premises, or in the cloud.
   * **Control Plane**: This is the **brain of the cluster**, responsible for **managing the desired state** of the **system**. It includes: 
        * **kube-apiserver**: Exposes the Kubernetes API for communication. 
        * **etcd**: A key-value store for cluster data persistence.
        * **kube-scheduler**: Assigns pods to nodes based on resource availability and constraints. 
        * **kube-controller-manager**: Manages controllers like node health, job completion, and replication.
   * **Nodes**: These are the **worker machines** (physical or virtual) that run the actual workloads. Each node contains:
       * **kubelet**: Ensures containers in pods are running and healthy. 
       * **kube-proxy**: Manages networking rules for communication between pods. Container 
       * **Runtime**: Executes containers (e.g., containerd, CRI-O).
   * **Pods**: The **smallest deployable unit** in Kubernetes, **containing one or more containers** that share resources like storage and networking.

Services and Networking
: Service: Exposes pods as a network service, enabling communication. Ingress: Manages external access to services, such as HTTP routing

Kind
: kind is a tool for running local Kubernetes clusters using Docker container "nodes". kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

Kubernetes local Cluster
: A local Kubernetes cluster is a versatile tool for developers and learners to experiment with Kubernetes features.

Kubernetes Service
: A Kubernetes service is a **logical abstraction that exposes a group of Pods running in a cluster to clients over the network**. It provides a stable endpoint and load balancing features, allowing applications to communicate reliably without tracking individual Pod IPs. Services enable seamless communication between different parts of an application, ensuring that clients can interact with the application consistently, regardless of the underlying Pods' ephemeral nature.

Pip
: pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.

Python
: Python is a programming language that lets you work quickly
and integrate systems more effectively

Runner
: A GitHub Runner is a machine that executes the jobs defined in a GitHub Actions workflow. It acts as the environment where the workflow's steps are carried out, such as running scripts, building code, or deploying applications. Runners can be either GitHub-hosted or self-hosted, depending on the level of control and customization required.

self-service workflows
: System or process that allows users to access information, perform tasks, or resolve issues independently without direct assistance from staff.

streamline software delivery
: Process of optimizing and simplifying the entire software development lifecycle, from conceptualization to deployment.

Workflow
: Workflow procedures describe temporal and causal dependencies among activities represented as steps.

YAML
: YAML (YAML Ain't Markup Language) is a human-readable data serialization language commonly used for configuration files and data exchange between languages with different data structures. It is designed to be easy to read and write, making it a popular choice for configuration files and data serialization.

[Ricardo Andrea Gonzalez Gomez](https://squad.udemy.com/user/ricardo-andre-gonzalez-gomez/)
* DevOps Engineer & SysAdmin.

* Cloud Architect & Linux Specialist.

* Red Hat Certified Engineer.

* Red Hat Certified System Administrator.

## Intro

This course requires you to download docker from the official Docker Repositories as well as images from Docker Hub. If you are a Udemy Business user, please check with your employer before downloading software.

Are you a DevOps engineer looking to take your career to the next level? Are you curious about Platform Engineering and how **Internal Developer Portals (IDPs)** can revolutionize the way teams develop, deploy, and manage applications? If so, this course is designed for you!

This course will take you from DevOps to Platform Engineering by mastering Backstage, an open-source framework developed by Spotify, and integrating it with modern DevOps tools to build a fully functional Internal Developer Platform (IDP).

In this hands-on, project-based course, you will work on real-world DevOps projects, implementing automation and self-service workflows to streamline software delivery. By the end of this course, you will have gained practical experience in:

* Building and deploying applications using Docker, Kubernetes, and ArgoCD

* Automating CI/CD pipelines with GitHub Actions

* Creating an Internal Developer Platform (IDP) using Backstage

* Writing Documentation as Code with Backstage TechDocs

* Implementing Software Templates for faster application deployments

* Deploying Backstage in a production environment

This course is practical, hands-on, and beginner-friendly, ensuring that you learn by doing rather than just theory. No prior Platform Engineering experience is required, but a basic understanding of DevOps, CI/CD, and infrastructure management will be beneficial.

Join now and get ahead in the future of DevOps & Platform Engineering!

[UDEMY course](https://squad.udemy.com/course/from-devops-to-platform-engineering-master-backstage-idps)

## Requirements & steps 

### Requirements

* docker is working
* pyhon 3 and pip are working
* we create a project repository on github

### Steps

* write a basic flask application
* push into github repository
* make a Dockerfile for this app
* build the docker image
* push it to docker app
* make a pipeline to do build and push automaticly
* deploy to kubernetes, 3 ways :
  * kubernetes files
  * helm charts
  * argo cd
* automate de deployment of the application through a CD pipeline DNS using GitHub actions

## Application Code

https://github.com/ricardoandre97/python-app


  
### writing code

using flask, jsonify, datetime, socket

```python
from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/json/v1/info')
def info():
    """get time, hostname and blabla"""
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p on %A %d %B, %Y"),
    	'hostname': socket.gethostname(),
      'message': '1 Bless U <3',
    })

if __name__ == '__main__':
    app.run() # works with python only
```

### debug

```bash
$ python src/app.py # works on localhost:5000
$ docker build -t python-app:v1 .
$ docker images
$ docker run -dp 8080:5000 python-app:v1
$ docker ps
$ docker exec -ti 68c20a82c9db sh # try on localhost:8080, doesn't work
/ # apk add curl
/ # curl http://localhost:5000
always ok
/ # ip a
...
inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
/ # curl http://172.17.0.2:5000 # works with app.run(host="0.0.0.0")
```

### fix

```python
if __name__ == '__main__':
    # app.run() # works with python only
    app.run(host="0.0.0.0") # works with docker and python
```

### rebuild v2

```bash
$ python src/app.py # works on localhost:5000 and docker with app.run(host="0.0.0.0")
$ docker build -t python-app:v2 .
$ docker images
$ docker run -dp 8080:5000 python-app:v2
$ docker ps
$ docker exec -ti 68c20a82c9db sh # works on localhost:8080 with app.run(host="0.0.0.0")
```

## share in repo

* create repo (see DCA images)

* **tag** the image with your Docker Hub login
  
```bash
docker tag pyhton-app:v2 ${TheLogin}/pyhton-app:v2
```

* Get logged in your Docker Hub account

```bash
docker login -u ${TheLogin}
    enter TheAccessToken
```

* Push your image
* Build for amd64
* Push amd64 image

```bash
docker push ${TheLogin}/pyhton-app:v2
docker build --platform linux/amd64 -t ${TheLogin}/getting-started .
docker push ${TheLogin}/pyhton-app
```

## Kubernetes local Cluster

### install kind

* get in [wsl2](https://kind.sigs.k8s.io/docs/user/using-wsl2/)
* check architecture

```bash
uname -m
 x86_64
```

* get kind bin
* add exec right
* mv kind into /usr/local/bin

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-$(uname)-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

* check kind :
  * check version

```bash
kind --version
    kind version 0.30.0
```

### Create local cluster

* try kind :
  * create cluster

```bash
kind --version
    kind version 0.30.0
kind create cluster
    Creating cluster "kind" ...
      ✓ Ensuring node image (kindest/node:v1.34.0) 🖼
      ✓ Preparing nodes 📦
      ✓ Writing configuration 📜
      ✓ Starting control-plane 🕹️
      ✓ Installing CNI 🔌
      ✓ Installing StorageClass 💾
    Set kubectl context to "kind-kind"
    You can now use your cluster with:

    kubectl cluster-info --context kind-kind

      Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
      lucile@ubuntu-manager:~$ kubectl cluster-info --context kind-kind
      Kubernetes control plane is running at https://127.0.0.1:41881
      CoreDNS is running at https://127.0.0.1:41881/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

      To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

* try it in your brower : 
  * https://127.0.0.1:41881/
  * https://127.0.0.1:41881/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

* *to delete it :*

```bash
kind delete cluster
```

## kubectl control plane command line

### Install

* get bin
* check sha256 checksum

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
```

* check it works, and version

```bash
kubectl version
kubectl version --output=yaml
```

### Syntax
  
```bash
kubectl [command] [RESOURCE TYPE] [NAME] [flags]
```

- **command** :
  - alpha : kubectl **alpha** SUBCOMMAND [flags] : List available alpha commands.
  - annotate : kubectcl **annotate** (-f FILENAME | TYPE) K0=V0 K1=V1.. [--overwrite] [--all] [--resource-version=VX] [flags] : Add or update the annotations of n resources.
  - api-resources : kubectl **api-resource** [flags] : List available API resources.
  - api-versions : kubectl **api-versions** [flags] : List available API versions.
  - apply : kubectl **apply** -f FILENAME [flags] : Apply configuration from a file or stin
  - attach : kubectl **attach** POD -c CONTAINER [-i] [-t] [falgs] : Attach to a running container stdin.
  - auth : kubectl **auth** [flags] [options] : Inspect authorization.
  - autoscale : kubectl **autoscale** (-f FILENAME | TYPE) [--min|max=NBPODS] [--cpu-percent=CPU] [flags] : Automatically scale the set of pods that are managed by a replication controller.
  - certificate : kubectl **certificate** SUBCOMMAND [options] : Modify certificate resource.
  - cluster-info : kubectl **cluster-info** [flags] : Display endpoint informations of master and srvices in the cluster.
  - completion : kubectl **completion** SHELL [options] : Output shell completion code for the specified shell (bash or zsh).
  - config : kubectl **config** SUBCOMMAND [flags] : Modify kube config files.
  - cordon : kubectl **cordon** NODE [options] : Mark node as unschedulable.
  - uncordon : kubectl **uncordon** NODE [options] : Mark node as schedulable.
  - cp : kubectl cp <file-spec-src> <file-spec-dest> [options] : Copy files and directories from to containers.
  - **create** : kubectl **create** -f FILENAME [flags] : Create resources from file or stdin
  - **delete** : kubectl **delete** (-f FILENAME | TYPE) -l label [flags]: Delete resources from file or stdin or/and label selectors, names, resource selectors, resource id.
  - **describe** : kubectl **describe** (-f FILENAME | TYPE) -l label [flags]: Display detailed states of one or more resources.
  - **diff** : kubectl **diff** -f FILENAME [flags]: Diff file or stdin against live configuration.
  - **drain** : kubectl **drain** NODE [options]: Drain node in prepartion of maintenance.
  - **edit** :  kubectl **edit** (-f FILENAME | TYPE) [flags] : Edit and update the definition of resources on the serveur by using the default editor.
  - **events** : kubectl **events** : List events.
  - **exec** : kubectl **exec** POD [-c CONTAINER] [-i] [-t] [flags] [--COMMAND] [args...] : Execute a command against a container in a POD.
  - explain : kubectl **explain** TYPE [--recursive=false] [flags] : Get documentations of various resources. For instance pods, nodes, services etc.
  - **expose** : kubectl **expose** (-f FILENAME | TYPE) --port=PORT --protocole=TCP|UDP --target-port=NAME|PORT --name=NAME --extarnal-ip=IP --type=TYPE [flags] : Expose a replication controller, service, or pod as a new k8s service.
  - **get** : kubectl get (-f FILENAME | TYPE) [--watch] [--sort-by=FIELD] [-o=OUTPUT_FORMAT] [flags] : List resources.
  - kustomize : kubectl **kustomize** <dir> [flags] [options] : List a set of API resources generated from kustomization.yaml instruction file.
  - **label** : kubectl **label** (-f FILENAME | TYPE) K0=V0 K1=V1.. [--overwrite] [--all] [--resource-version=VX] [flags]: Add or update the labels of n resources.
  - **logs** : kubectl **logs** POD [-c CONTAINER] [--follow] [flags] : Print the logs for a container in a pod or specified resource. If the pod has only one container, the container name is optional.
  - **options** : kubectl **options** : List of global command-line options, witch apply to all commands.
  - patch : kubectl **patch** (-f FILENAME | TYPE) --patch PATCH [flags] : Update fields of a resource using strategic merge patch, a JSON merge patch, or a JSON patch..
  - plugin : kubectl **plugin** [flags] [options] : Provides utilities for interacting with plugins.
  - port-forward : kubectl ***port-forward** POD [LOCAL_PORT:] REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N] [flags]: Forward one or more local ports to a pod.
  - proxy : kubectl **proxy** [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [api--prefix=prefix] [flags] : Creates a proxy server or application-level gateway between localhost and the Kubernetes API server. It also allows serving static content over specified HTTP path. All incoming data enters through one port and gets forwarded to the remote Kubernetes API server port, except for the path matching the static content path.
  - replace : kubectl **replace** -f FILENAME : Replace a resource from a file or stdin.
  - rollout : kubectl **rollout** SUBCOMMAND [options] : Manage the rollout of a resource like deployments, daemonsets and statefulsets.
  - **run** : kubectl **run** NAME --image=image [--env="K=V"] [--port=PORT] [--dry-run=server|client|none] [--overrides=inline-json] [flags] : Run a specified image on the cluster.
  - **scale** : kubectl **scale** (-f FILENAME | TYPE) --replicas=COUNT [--resource-version=VERSION] [--current-replicas=count] [flags] : Set a new size for a deployment, replica set, replication controller, or stateful set.
  - set : kubectl **set** SUBCOMMAND [options] : Configure application resource.
  - taint : kubectl **taint** NODE NAME K0=V0:T0 K1=V1:T1 [options] : Update the taints on one or more nodes. Ex Add a taint with key 'dedicated' on nodes having label myLabel=X :
  kubectl taint node -l myLabel=X  dedicated=foo:PreferNoSchedule
  - **top** : kubectl **top** (POD | NODE) [flags] [options] : Display CPU/MEM/Storage usage for a pod or node.
  - version : kubectl **version** [--client] [flags] : Display the kubernetes version running on the client and server.
  - wait : kubectl **wait** ([-f FILENAME] | resource.group/resource.name | resource.group [(-l label | --all)]) [--for=delete|--for condition=available] [options] : Experimental: Wait for a specific condition on one or many resources.
  
  
- RESSOURCE TYPE
  - bindings : Binding
  - componentstatuses - **cs** : ComponentStatus
  - **configmaps - cm** : ConfigMap
  - endpoints - **ep** : Endpoints
  - events - **ev** (events) : Event
  - limitranges - **limits** : LimitRange
  - namespaces - **ns** : Namespace
  - **nodes - no** : Node
  - persistantvolumeclaims - **pvc** : PersistantVolumeClaim
  - **persistantvolumes - pv** : PersistantVolume
  - **pods - po** : Pod
  - podtemplates : PodTemplate
  - replicationcontrollers - **rc** : ReplicationController
  - resourcequotas - **quota** : ResourceQuotas
  - **secrets** : Secret
  - serviveaccounts - sa : ServiceAccount
  - services - **svc** : Service
  - customeresourcedefinitions - **crd**, cdrs (apiextensions) : CustomResourceDefinition
  - apiservices (apiregistration) : APIService
  - controllerrevisions (apps) : ControllerRevision
  - **daemonset - ds** (apps) : DaemonSet
  - **deployments - deploy** (apps) : Deployment
  - **replicasets - rs** (apps) : ReplicaSet
  - **statefulsets - sts** (apps) : StatefulSet
  - tokenreviews (authentication) : TokenReview
  - [local|self|-]subject[access|rule]reviews (authorization) : *Subject*Review
  - horizontalpodautoscalers - **hpa** (autoscalling) : HorizontalPodAutoscaler
  - cronjobs - **cj** (batch) : CronJob
  - **jobs** (batch) : Job
  - certificatesigningrequests - **csr** (certificates) : CertificateSigningRequest
  - flowschemas (flowcontrol) : FlowSchema
  - ingressclasses (networking) : IngressClass
  - **ingress - ing** (networking) : Ingress
  - networkpolicies - **netpol** (networking) : NetworkPolicies
  - runtimeclasses (node) : RuntimeClass
  - poddisruptionbudgets - **pdb** (policy) : PodDisruptionBudget
  - podsecuritypolicies - **psp** (policy) : PodSecurityPolicy
  - clusterrolebindings (rbac) : ClusterRoleBiding
  - clusterroles (rbac) : ClusterRole
  - roles (rbac) : RoleBinding
  - priorityclasses - **pc** (sheduling) : PriorityClass
  - csidrivers (storage) : CSIDriver
  - csinodes (storage) : CSIStorageCapacity
  - storageclasses - **sc** (storage) : StorageClass
  - volumeattachements (storage) : VolumeAttachement  



* ex

```bash
kubectl get pods pod1
```
