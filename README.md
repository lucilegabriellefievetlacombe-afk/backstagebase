
# Learn Platform Engineering, Backstage, Kubernetes, ArgoCD, Docker, GitOps, Helm, GitHub Actions & CI/CD to build IDPs

*To get a personalized course, create or/and get your ids of dockerhub and github; create a branch with my_course__%YourDockerHubLogin%__%your_login_in_github%.
Replace your-own-github-account with your account name on github.
Replace YourDockerHubLogin with your account in dockerhub.
wait for your branch pipeline.*

## Glossary

**IDP**
: **I**nternal **D**eveloper **P**latform

**Backstage**
: CNF open-source **Platform Engineering framework** developed by **Spotify**, and integrating it with modern **DevOps tools** to build a fully functional **Internal Developer Platform**(IDP)

**Docker File**
: A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

**Docker Containers**
: A Docker container is a lightweight, standalone, and executable unit of software that encapsulates an application along with all its dependencies, such as libraries, runtime, system tools, and configurations.

**Kubernetes - k8s**
: Open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Originally developed by Google, it has become the de-facto standard for running containers at scale.

**Kind**
: kind is a tool for running local Kubernetes clusters using Docker container "nodes". kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

**kubectl**
: **Command line tool** for communicating with a **Kubernetes cluster's control plane**, using the Kubernetes API.

**Helm**
: Helm is a **package manager for Kubernetes** that simplifies the deployment and management of applications within Kubernetes clusters. It bundles Kubernetes resources into a single Helm chart.

**Helm Chart**
: Reusable package which includes all necessary code and resources needed to deploy an application.

**ArgoCD**
: Argo CD is a **declarative, GitOps continuous delivery tool for Kubernetes**.

**Ingress Controller**
: Component in Kubernetes that manages external access to services within a cluster, typically through HTTP and HTTPS. It is responsible for fulfilling the Ingress resource, which defines rules for routing traffic to different services based on the request's host and path. Common ingress controllers include NGINX and Traefik, and they often work with load balancers to handle incoming traffic effectively.

**Flask API**
: Flask API is primarily built using the Flask framework, a lightweight and flexible **micro-framework for Python**. Flask itself was created by Armin Ronacher as part of the Pallets Projects.

<details> <summary>Glossary details</summary>

**ARC**
: Actions Runner Controller is a Kubernetes operator that orchestrates and scales self-hosted runners for GitHub Actions.

**ArgoCD**
: Argo CD is a **declarative, GitOps continuous delivery tool for Kubernetes**.

**Backstage**
: CNF open-source **Platform Engineering framework** developed by **Spotify**, and integrating it with modern **DevOps tools** to build a fully functional **Internal Developer Platform**(IDP)

**Backstage Auth & Identity**
: The authentication system in Backstage serves two distinct purposes: **sign-in** and **identification** of **users**, as well as delegating access to **third-party resources**. It is possible to configure Backstage to have any number of authentication providers, but only one of these will typically be used for sign-in, with the rest being used to provide access to external resources. Built-in Athentication providers : Auth0, Atlassian, Azurz, BitBucket, Cloudflare, GitHub, GitLab, Google, Google IAP, Okta, OAuth2, OneLogine, OpenShift, VMware Cloud

**Backstage Configuration**
: Backstage ships with a flexible configuration system that provides a simple way to configure Backstage apps and plugins for both local development and production deployments. Configuration is stored in YAML files where the defaults are app-config.yaml and app-config.local.yaml for local overrides and app-config.<BACKSTAGE_ENV>.yaml for BACKSTAGE_ENV environment variable.

**Backstage Framework CLI**
: **build system and tooling**, delivered primarily through the @backstage/cli package. When creating an app using @backstage/create-app, you receive a project that's already prepared with a typical setup and package scripts for executing the most common commands. *Under the hood the CLI uses **Webpack** for bundling, **Rollup** for building packages, **Jest** for testing, and **eslint** for linting*. It also includes tooling for working within Backstage apps, for example for keeping the app up to date and verifying static configuration. For a more in-depth look into the tooling, see the build system page, and for a list of commands, see the commands page.

**Backstage Framework Backend System**
: Provides a flexible foundation for building and extending Backstage backends. It uses a modular architecture where you can create and customize plugins, modules, and service implementations.

**Backstage Framework Frontend System**
: Provides high-level building blocks upon which this new system is built.

**Backstage Framework User Interface (UI)**
: built-in support for both light and dark themes, making it easy to get started with a professional look and feel. But many teams want to go further—tailoring the interface to reflect their organization’s unique brand, identity, and experience.

**Backstage Integration**
: Integrations allow Backstage to **read or publish data** using **external providers** such as *GitHub, GitLab, Gitea, Bitbucket, LDAP, or cloud providers*.

**Backstage Kubernetes**
: Tool that's designed around the **needs of service owners**, not cluster admins. Now developers can easily **check the health of their services** no matter how or where those services are deployed — whether it's on a local host for testing or in production on dozens of clusters around the world.

**Backstage Notifications**
: System that provides a way for plugins and external services to send notifications to Backstage users. These notifications are displayed in the dedicated page of the Backstage frontend UI or by frontend plugins per specific scenarios. Additionally, notifications can be sent to external channels (like email) via "processors" implemented within plugins.

**Backstage Permissions**
: Backstage can also authorize specific data, APIs, or interface actions - meaning that Backstage has the ability to enforce rules about what type of access is allowed for a given user of a system.

**Backstage Plugins**
: Backstage orchestrates a cohesive single-page application by seamlessly integrating various plugins.

**Backstage Software Catalog**
: **Centralized system** that keeps track of ownership and metadata **for all the software in your ecosystem** (services, websites, libraries, data pipelines, etc). The catalog is built around the concept of metadata YAML files stored together with the code, which are then harvested and visualized in Backstage.

**Backstage Resolver**
: Function that is responsible for creating this **user identity mapping**. Signing in a user into Backstage requires a mapping of the user identity *from* the **third-party auth provider** to a Backstage user identity.

**Backstage Search**
: Backstage Search lets you find the right information you are looking for in the Backstage ecosystem.

**Backstage TechDocs**
: Spotify’s homegrown docs-like-code solution built directly into Backstage. Engineers write their documentation in **Markdown** files which live together with their **code** - and with little configuration get a nice-looking doc site in Backstage.

**Backstage Software Templates**
: **Tool** that can help you **create Components** inside Backstage. By default, it has the ability to **load skeletons of code**, template in some **variables**, and then **publish** the template to some locations like GitHub or GitLab.

**CD**
: **C**ontinuous **D**elivery||**D**eployment, CD refers to the practice of continuous delivery and/or continuous deployment software. Both are about automating further stages of the pipeline.

   > * **Continuous delivery** automates the release of validated code to a repository following the automation of builds and unit and integration testing in CI.
   > * **Continuous deployment** is an extension of continuous delivery, and can refer to automating the release of a developer’s changes from the repository to production, where it is usable by customers. It can concern development and testing envronnements.
   > * A **multi-env-branches gitflow** pipeline can use continuous deployment for developpement feature or fix branches, for QA integration branch and PPD future release branch and then use either continuous delivery or deployment for production.
   > * **CD features&fix DEV > CD integration QA > CD version-X.X.X PPD > CD PROD**

**CI**
: **C**ontinuous **I**ntegration, CI always refers to continuous integration, an automation process for developers that facilitates more frequent merging of code changes back to a shared branch, or “trunk.” As these updates are made, automated testing steps are triggered to ensure the reliability of merged code changes.

**CRDs**
: Custom Resource Definitions, CRDs are a powerful feature in Kubernetes that lets you extend its native API, enabling you to create your own resource types.

**DevOps**
: DevOps is a set of practices, tools, and a cultural philosophy that integrates and automates the work of software development (Dev) and IT operations (Ops) to improve and shorten the systems development life cycle. It emphasizes team empowerment, cross-team communication, collaboration, and technology automation.

**Docker**
: Docker is a platform designed to help developers build, share, and run container applications. We handle the tedious setup, so you can focus on the code.

**Docker File**
: A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

**Docker Containers**
: A Docker container is a lightweight, standalone, and executable unit of software that encapsulates an application along with all its dependencies, such as libraries, runtime, system tools, and configurations.

**Flask API**
: Flask API is primarily built using the Flask framework, a lightweight and flexible **micro-framework for Python**. Flask itself was created by Armin Ronacher as part of the Pallets Projects.

**IaC**
: **I**nfrastructure **a**s **C**ode, is the practice of keeping all infrastructure configuration stored as code. 

**IDP**
: **I**nternal **D**eveloper **P**latform

**Ingress Controller**
: Component in Kubernetes that manages external access to services within a cluster, typically through HTTP and HTTPS. It is responsible for fulfilling the Ingress resource, which defines rules for routing traffic to different services based on the request's host and path. Common ingress controllers include NGINX and Traefik, and they often work with load balancers to handle incoming traffic effectively.

**GitHub**
: GitHub is a web-based platform that hosts Git repositories, providing developers with tools for version control and collaboration. It combines Git, a powerful version control system, with features that facilitate collaboration and project management.

**GitOps**
: GitOps is an operational framework that takes DevOps best practices used for application development such as version control, collaboration, compliance, and CI/CD, and applies them to infrastructure automation.

**Helm**
: Helm is a **package manager for Kubernetes** that simplifies the deployment and management of applications within Kubernetes clusters. It bundles Kubernetes resources into a single Helm chart.

**Helm Chart**
: Reusable package which includes all necessary code and resources needed to deploy an application.

**kubectl**
: **Command line tool** for communicating with a **Kubernetes cluster's control plane**, using the Kubernetes API.

**Kubernetes**
: Open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Originally developed by Google, it has become the de-facto standard for running containers at scale.

**Kubernetes local Cluster**
: A Kubernetes cluster is a **collection of machines (nodes) designed to run containerized applications**. It is the core of Kubernetes' functionality, *enabling the orchestration, scaling, and management of containers* across multiple machines, whether they are physical, virtual, on-premises, or in the cloud.

   > * **Control Plane**: This is the **brain of the cluster**, responsible for **managing the desired  > > > state** of the **system**. It includes: 
   >     * **kube-apiserver**: Exposes the Kubernetes API for communication. 
   >     * **etcd**: A key-value store for cluster data persistence.
   >     * **kube-scheduler**: Assigns pods to nodes based on resource availability and constraints. 
   >     * **kube-controller-manager**: Manages controllers like node health, job completion, and     replication.
   >* **Nodes**: These are the **worker machines** (physical or virtual) that run the actual workloads. 
   > Each node contains:
   >    * **kubelet**: Ensures containers in pods are running and healthy. 
   >    * **kube-proxy**: Manages networking rules for communication between pods. Container 
   >    * **Runtime**: Executes containers (e.g., containerd, CRI-O).
   > * **Pods**: The **smallest deployable unit** in Kubernetes, **containing one or more containers** that > share resources like storage and networking.

**Services and Networking**
: Service: Exposes pods as a network service, enabling communication. Ingress: Manages external access to services, such as HTTP routing

**Kind**
: kind is a tool for running local Kubernetes clusters using Docker container "nodes". kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

**Kubernetes local Cluster**
: A local Kubernetes cluster is a versatile tool for developers and learners to experiment with Kubernetes features.

**Kubernetes Service**
: A Kubernetes service is a **logical abstraction that exposes a group of Pods running in a cluster to clients over the network**. It provides a stable endpoint and load balancing features, allowing applications to communicate reliably without tracking individual Pod IPs. Services enable seamless communication between different parts of an application, ensuring that clients can interact with the application consistently, regardless of the underlying Pods' ephemeral nature.

**Pip**
: pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.

**Python**
: Python is a programming language that lets you work quickly
and integrate systems more effectively

**Runner**
: A GitHub Runner is a machine that executes the jobs defined in a GitHub Actions workflow. It acts as the environment where the workflow's steps are carried out, such as running scripts, building code, or deploying applications. Runners can be either GitHub-hosted or self-hosted, depending on the level of control and customization required.

**self-service workflows**
: System or process that allows users to access information, perform tasks, or resolve issues independently without direct assistance from staff.

**streamline software delivery**
: Process of optimizing and simplifying the entire software development lifecycle, from conceptualization to deployment.

**Workflow**
: Workflow procedures describe temporal and causal dependencies among activities represented as steps.

**YAML**
: YAML (YAML Ain't Markup Language) is a human-readable data serialization language commonly used for configuration files and data exchange between languages with different data structures. It is designed to be easy to read and write, making it a popular choice for configuration files and data serialization.

</details>


<details> <summary>[Ricardo Andrea Gonzalez Gomez](https://squad.udemy.com/user/ricardo-andre-gonzalez-gomez/)</summary>

* DevOps Engineer & SysAdmin.
* Cloud Architect & Linux Specialist.
* Red Hat Certified Engineer.
* Red Hat Certified System Administrator.

</details>

## Intro

Ricardo Andrea Gonzalez Gomez course requires you to download docker from the official Docker Repositories as well as images from Docker Hub. If you are a Udemy Business user, please check with your employer before downloading software.

Are you a DevOps engineer looking to take your career to the next level? Are you curious about Platform Engineering and how **Internal Developer Portals (IDPs)** can revolutionize the way teams develop, deploy, and manage applications? If so, this course is designed for you!

This course will take you from DevOps to Platform Engineering by mastering Backstage, an open-source framework developed by Spotify, and integrating it with modern DevOps tools to build a fully functional Internal Developer Platform (IDP).

In this hands-on, project-based course, you will work on real-world DevOps projects, implementing automation and self-service workflows to streamline software delivery. By the end of this course, you will have gained practical experience in:

* Building and deploying applications using **Docker**, **Kubernetes**, and **ArgoCD**

* Automating **CI/CD pipelines with GitHub Actions**

* Creating an **Internal Developer Platform (IDP) using Backstage**

* Writing Documentation as Code with **Backstage TechDocs**

* Implementing **Software Templates** for faster application deployments

* **Deploying Backstage in a production environment**

This course is practical, hands-on, and beginner-friendly, ensuring that you learn by doing rather than just theory. No prior Platform Engineering experience is required, but a basic understanding of DevOps, CI/CD, and infrastructure management will be beneficial.

Join now and get ahead in the future of DevOps & Platform Engineering!

[UDEMY course](https://squad.udemy.com/course/from-devops-to-platform-engineering-master-backstage-idps)

## Requirements & steps 

### Requirements

* docker is working
* pyhon3 and pip are working
* a linux ubuntu, on wsl2, docker somewhere, wmare... or on bare-metal
* we have your own account on github (*your-own-github-account*)
* an editor, like vs code or vim (*examples are given with vim to make it old seems old school*)

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

## Original Application Code

https://github.com/ricardoandre97/python-app

### Create your repository from scatch or from course

```bash
mkdir -p ~/src/backstage; cd ~/src/backstage
git clone https://github.com/ricardoandre97/python-app.git .
cd python-app
git remote -v
git remote remove origin
git remote add origin https://github.com/your-own-github-account/backstage.git
```

### writing Application Dockerfile in ${PROJ}/Dockerfile

<details> <summary>Dockerfile</summary>

```dockerfile

FROM python:3.11-alpine

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

CMD python /src/app.py

```

</details>

### Writing Application Python Code in ${PROJ}/src/app.py

*Using flask, jsonify, datetime and sockets*

<details> <summary>app.py Code</summary>

```python app.py

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
    app.run() # will works with python only
```

</details>

### try on directly on host

```bash
python src/app.py 
```

* works on host [localhost:5000](http://localhost:5000)

### build image, see it

```bash
docker build -t python-app:v1 .
docker images
```

<details> <summary>results</summary>

```bash result
IMAGE                                                                                  ID             DISK USAGE   CONTENT SIZE   EXTRA

python-app:v1                                                                          69e0e97ff0a2        109MB         26.7MB    U
python:3.11-alpine                                                                     610ede222c1f       83.3MB         20.2MB
```

</details>

### start the container, see it

```bash
docker run -dp 8080:5000 python-app:v1
docker ps
```

* try on localhost:8080, it doesn't work, debug

### debug

* get in the container

```bash
docker exec -ti 68c20a82c9db sh 
```

<details> <summary>results</summary>

```bash result
   / #
```

*you are in the pod term*

</details>



* add curl to check 5000 from the container

```bash
apk add curl
curl http://localhost:5000
```

* it is ok
* check container IP

```bash
ip a
```

<details> <summary>results</summary>

```bash result
   ...
   inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
```

</details>

```bash
curl http://172.17.0.2:5000 
```

* open host browser on http://172.17.0.2:5000, it works
* the server is ok, but not on the 8080, we extend the publishing

### fix host filter, allow all

```python

if __name__ == '__main__':
    # app.run() # works with python only
    app.run(host="0.0.0.0") # will works with docker and python
```

```bash
$ python src/app.py # still works on localhost:5000 and docker 
```

### rebuild v2

```bash
$ docker build -t python-app:v2 .
$ docker images
```

### re-run v2

```bash
$ docker run -dp 8080:5000 python-app:v2
$ docker ps
```

* try on localhost:8080, it works

## share in repo

```bash
cd ~/src/backstage/pyhton-app/
```

* Create a repo (see DCA images) in Docker Hub

* **tag** the image with your Docker Hub login ${YourDockerHubLogin}
  
```bash
docker tag pyhton-app:v2 ${YourDockerHubLogin}/pyhton-app:v2
```

* Get logged in your Docker Hub account

```bash
docker login -u ${YourDockerHubLogin}
```

<details> <summary>results</summary>

```bash result
   Password: # enter TheAccessToken
      Login Succeeded
```

</details>

* Push your image
* Build for amd64
* Push amd64 image

```bash
docker push ${YourDockerHubLogin}/pyhton-app:v2
docker build --platform linux/amd64 -t ${YourDockerHubLogin}/python-app .
docker push ${YourDockerHubLogin}/pyhton-app
docker images
```

<details> <summary>results</summary>

```bash result
IMAGE                                                                                  ID             DISK USAGE   CONTENT SIZE   EXTRA
luspokvenus/python-app:v2                                                              69e0e97ff0a2        109MB         26.7MB    U
python-app:v2                                                                          69e0e97ff0a2        109MB         26.7MB    U
python:3.11-alpine
```
</details>

## 1 - Get Kind our Kubernetes Local Cluster

### Install Kind on WSL2 linux Ubuntu

* get in [wsl2](https://kind.sigs.k8s.io/docs/user/using-wsl2/)
* check architecture

```bash
uname -m
```

<details> <summary>results</summary>

```bash result
   x86_64
```

*depending on your host*

</details>

* get kind bin
* check sha256 signature
* add exec right
* mv kind into /usr/local/bin

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-$(uname)-amd64
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-$(uname)-amd64.sha256sum
echo "$(cat kind.sha256)  kind" | sha256sum --check
```

* if ok, give rights and move it in user binairies

```bash
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

* check kind, check version

```bash
kind --version
```

<details> <summary>results</summary>

```bash result
   kind version 0.30.0
```

</details>

### Create local k8s cluster

* try kind :
  * create cluster

```bash
kind create cluster
```

<details> <summary>results</summary>

```bash result
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
```

</details>

```bash
   kubectl cluster-info --context kind-kind
```

<details> <summary>results</summary>

```bash result
  Not sure what to do next? 😅  Check out https://kind.sigs.k8s.io/docs/user/quick-start/
```

</details>

```bash
kubectl cluster-info --context kind-kind
```

<details> <summary>results</summary>

```bash result
   Kubernetes control plane is running at https://127.0.0.1:41881
      CoreDNS is running at https://127.0.0.1:41881/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'
```

</details>

* try it in your brower : 
  * https://127.0.0.1:41881/
  * https://127.0.0.1:41881/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy


## 2 - Get kubectl control plane command line

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

<details> <summary>commands</summary>

* alpha : kubectl **alpha** SUBCOMMAND [flags] : List available alpha commands.
* annotate : kubectcl **annotate** (-f FILENAME | TYPE) K0=V0 K1=V1.. [--overwrite] [--all] [--resource-version=VX] [flags] : Add or update the annotations of n resources.
* api-resources : kubectl **api-resource** [flags] : List available API resources.
* api-versions : kubectl **api-versions** [flags] : List available API versions.
* **apply** : kubectl **apply** -f FILENAME [flags] : Apply configuration from a file or stin
* attach : kubectl **attach** POD -c CONTAINER [-i] [-t] [falgs] : Attach to a running container stdin.
* auth : kubectl **auth** [flags] [options] : Inspect authorization.
* **autoscale** : kubectl **autoscale** (-f FILENAME | TYPE) [--min|max=NBPODS] [--cpu-percent=CPU] [flags] : Automatically scale the set of pods that are managed by a replication controller.
* certificate : kubectl **certificate** SUBCOMMAND [options] : Modify certificate resource.
* **cluster-info** : kubectl **cluster-info** [flags] : Display endpoint informations of master and srvices in the cluster.
* completion : kubectl **completion** SHELL [options] : Output shell completion code for the specified shell (bash or zsh).
* config : kubectl **config** SUBCOMMAND [flags] : Modify kube config files.
* cordon : kubectl **cordon** NODE [options] : Mark node as unschedulable.
* uncordon : kubectl **uncordon** NODE [options] : Mark node as schedulable.
* cp : kubectl cp <file-spec-src> <file-spec-dest> [options] : Copy files and directories from to containers.
* **create** : kubectl **create** -f FILENAME [flags] : Create resources from file or stdin
* **delete** : kubectl **delete** (-f FILENAME | TYPE) -l label [flags]: Delete resources from file or stdin or/and label selectors, names, resource selectors, resource id.
* **describe** : kubectl **describe** (-f FILENAME | TYPE) -l label [flags]: Display detailed states of one or more resources.
* **diff** : kubectl **diff** -f FILENAME [flags]: Diff file or stdin against live configuration.
* **drain** : kubectl **drain** NODE [options]: Drain node in prepartion of maintenance.
* **edit** :  kubectl **edit** (-f FILENAME | TYPE) [flags] : Edit and update the definition of resources on the serveur by using the default editor.
* **events** : kubectl **events** : List events.
* **exec** : kubectl **exec** POD [-c CONTAINER] [-i] [-t] [flags] [--COMMAND] [args...] : Execute a command against a container in a POD.
* explain : kubectl **explain** TYPE [--recursive=false] [flags] : Get documentations of various resources. For instance pods, nodes, services etc.
* **expose** : kubectl **expose** (-f FILENAME | TYPE) --port=PORT --protocole=TCP|UDP --target-port=NAME|PORT --name=NAME --extarnal-ip=IP --type=TYPE [flags] : Expose a replication controller, service, or pod as a new k8s service.
* **get** : kubectl get (-f FILENAME | TYPE) [--watch] [--sort-by=FIELD] [-o=OUTPUT_FORMAT] [flags] : List resources.
* kustomize : kubectl **kustomize** <dir> [flags] [options] : List a set of API resources generated from kustomization.yaml instruction file.
* **label** : kubectl **label** (-f FILENAME | TYPE) K0=V0 K1=V1.. [--overwrite] [--all] [--resource-version=VX] [flags]: Add or update the labels of n resources.
* **logs** : kubectl **logs** POD [-c CONTAINER] [--follow] [flags] : Print the logs for a container in a pod or specified resource. If the pod has only one container, the container name is optional.
* **options** : kubectl **options** : List of global command-line options, witch apply to all commands.
* patch : kubectl **patch** (-f FILENAME | TYPE) --patch PATCH [flags] : Update fields of a resource using strategic merge patch, a JSON merge patch, or a JSON patch..
* plugin : kubectl **plugin** [flags] [options] : Provides utilities for interacting with plugins.
* port-forward : kubectl ***port-forward** POD [LOCAL_PORT:] REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N] [flags]: Forward one or more local ports to a pod.
* proxy : kubectl **proxy** [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [api--prefix=prefix] [flags] : Creates a proxy server or application-level gateway between localhost and the Kubernetes API server. It also allows serving static content over specified HTTP path. All incoming data enters through one port and gets forwarded to the remote Kubernetes API server port, except for the path matching the static content path.
* replace : kubectl **replace** -f FILENAME : Replace a resource from a file or stdin.
* **rollout** : kubectl **rollout** SUBCOMMAND [options] : Manage the rollout of a resource like deployments, daemonsets and statefulsets.
* **run** : kubectl **run** NAME --image=image [--env="K=V"] [--port=PORT] [--dry-run=server|client|none] [--overrides=inline-json] [flags] : Run a specified image on the cluster.
* **scale** : kubectl **scale** (-f FILENAME | TYPE) --replicas=COUNT [--resource-version=VERSION] [--current-replicas=count] [flags] : Set a new size for a deployment, replica set, replication controller, or stateful set.
* set : kubectl **set** SUBCOMMAND [options] : Configure application resource.
* taint : kubectl **taint** NODE NAME K0=V0:T0 K1=V1:T1 [options] : Update the taints on one or more nodes. Ex Add a taint with key 'dedicated' on nodes having label myLabel=X :
kubectl taint node -l myLabel=X  dedicated=foo:PreferNoSchedule
* **top** : kubectl **top** (POD | NODE) [flags] [options] : Display CPU/MEM/Storage usage for a pod or node.
- version : kubectl **version** [--client] [flags] : Display the kubernetes version running on the client and server.
* wait : kubectl **wait** ([-f FILENAME] | resource.group/resource.name | resource.group [(-l label | --all)]) [--for=delete|--for condition=available] [options] : Experimental: Wait for a specific condition on one or many resources.

</details>

<details> <summary>RESSOURCE TYPES</summary>

* bindings : Binding
* componentstatuses - **cs** : ComponentStatus
* **configmaps - cm** : ConfigMap
* endpoints - **ep** : Endpoints
* events - **ev** (events) : Event
* limitranges - **limits** : LimitRange
* namespaces - **ns** : Namespace
* **nodes - no** : Node
* persistantvolumeclaims - **pvc** : PersistantVolumeClaim
* **persistantvolumes - pv** : PersistantVolume
* **pods - po** : Pod
* podtemplates : PodTemplate
* replicationcontrollers - **rc** : ReplicationController
* resourcequotas - **quota** : ResourceQuotas
* **secrets** : Secret
* serviveaccounts - sa : ServiceAccount
* **services - svc** : Service
* customeresourcedefinitions - **crd**, cdrs (apiextensions) : CustomResourceDefinition
* apiservices (apiregistration) : APIService
* controllerrevisions (apps) : ControllerRevision
* **daemonset - ds** (apps) : DaemonSet
* **deployments - deploy** (apps) : Deployment
* **replicasets - rs** (apps) : ReplicaSet
* **statefulsets - sts** (apps) : StatefulSet
* tokenreviews (authentication) : TokenReview
* [local|self|-]subject[access|rule]reviews (authorization) : *Subject*Review
* **horizontalpodautoscalers - hpa** (autoscalling) : HorizontalPodAutoscaler
* cronjobs - **cj** (batch) : CronJob
* **jobs** (batch) : Job
* certificatesigningrequests - **csr** (certificates) : CertificateSigningRequest
* flowschemas (flowcontrol) : FlowSchema
* ingressclasses (networking) : IngressClass
* **ingress - ing** (networking) : Ingress
* networkpolicies - **netpol** (networking) : NetworkPolicies
* runtimeclasses (node) : RuntimeClass
* poddisruptionbudgets - **pdb** (policy) : PodDisruptionBudget
* podsecuritypolicies - **psp** (policy) : PodSecurityPolicy
* clusterrolebindings (rbac) : ClusterRoleBiding
* clusterroles (rbac) : ClusterRole
* **roles** (rbac) : RoleBinding
* priorityclasses - **pc** (sheduling) : PriorityClass
* csidrivers (storage) : CSIDriver
* csinodes (storage) : CSIStorageCapacity
* storageclasses - **sc** (storage) : StorageClass
* volumeattachements (storage) : VolumeAttachement  

</details>

* check kubectl

```bash
kubectl get pods pod1
```

* check **Kind** with **kubectl** :

```bash
kind delete cluster
kind create cluster
kubectl get pods
```

<details> <summary>results</summary>

```bash result
   No resources found in default namespace.
```

</details>

```bash
kubectl cluster-info
```

<details> <summary>results</summary>

```bash result
   Kubernetes control plane is running at https://127.0.0.1:XXXXX
   CoreDNS is running at https://127.0.0.1:XXXXX/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

</details>

* check url in the browser (allow exeption)
  * https://127.0.0.1:XXXX
  * https://127.0.0.1:XXXX/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

```bash
docker ps
```

<details> <summary>results</summary>

```bash result
   CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                       NAMES
   8c5b3017face   kindest/node:v1.34.0   "/usr/local/bin/entr…"   26 minutes ago   Up 25 minutes   127.0.0.1:36447->6443/tcp   kind-control-plane
```

</details>

* Get namespaces

```bash
kubectl get ns
```

<details> <summary>results</summary>

```bash result
   NAME                 STATUS   AGE
   default              Active   25m
   kube-node-lease      Active   25m
   kube-public          Active   25m
   kube-system          Active   25m
   local-path-storage   Active   25m
```

</details>

### [Ingress 4 Kind](https://kind.sigs.k8s.io/docs/user/ingress/) | [4 k8s](https://kubernetes.io/docs/concepts/services-networking/ingress/ ) | [ 4 k8s & flask ](https://github.com/SamanBarahoie/IngressFlask/tree/main/k8s)

## 3 - Create our local cluster with Kind

* delete previous one
  
```bash
kind delete cluster
```

* Create cluste kind with configuration as controle-plane

```bash
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
```

<details> <summary>results</summary>

```bash result
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
```

</details>

```bash
kubectl cluster-info --context kind-kind
```

<details> <summary>results</summary>

```bash result
   Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
```

</details>

* Check kindest/node mapping

```bash
docker ps # check mapping 80->80 443->443 38275->6443
```

<details> <summary>results</summary>

```bash result
   CONTAINER ID   IMAGE                  COMMAND                  CREATED       STATUS       PORTS                                                                 NAMES
   685317923bcd   kindest/node:v1.34.0   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours   0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 127.0.0.1:38275->6443/tcp   kind-control-plane
```

</details>

## 4 - Deploy our nginx pod

```bash
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
```

<details> <summary>results</summary>

```bash result
   namespace/ingress-nginx created # our namspace created
   serviceaccount/ingress-nginx created
   serviceaccount/ingress-nginx-admission created
   role.rbac.authorization.k8s.io/ingress-nginx created
   role.rbac.authorization.k8s.io/ingress-nginx-admission created
   clusterrole.rbac.authorization.k8s.io/ingress-nginx created
   clusterrole.rbac.authorization.k8s.io/ingress-nginx-admission created
   rolebinding.rbac.authorization.k8s.io/ingress-nginx created
   rolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
   clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx created
   clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
   configmap/ingress-nginx-controller created
   service/ingress-nginx-controller created
   service/ingress-nginx-controller-admission created
   deployment.apps/ingress-nginx-controller created
   job.batch/ingress-nginx-admission-create created
   job.batch/ingress-nginx-admission-patch created
   ingressclass.networking.k8s.io/nginx created
   validatingwebhookconfiguration.admissionregistration.k8s.io/ingress-nginx-admission created
```

</details>

* Check kindest/node mapping
* Check cluster info

```bash
kubectl cluster-info
```

<details> <summary>results</summary>

```bash result
   Kubernetes control plane is running at https://127.0.0.1:XXXXX
   CoreDNS is running at https://127.0.0.1:XXXXX/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

</details>

* Check pods in ingress-nginx name space
* Check ingress nginx controller is running

```bash
kubectl get pods -n ingress-nginx 
```

<details> <summary>results</summary>

```bash result
   NAME                                        READY   STATUS      RESTARTS   AGE
   ingress-nginx-admission-create-8mv4f        0/1     Completed   0          108s
   ingress-nginx-admission-patch-lrhxr         0/1     Completed   0          108s
   ingress-nginx-controller-68697cf9d9-pxg9n   1/1     Running     0          108s
```

</details>

## 5 - Configuration of ingress-nginx

* Copy kubernetes Ingress

  * https://kubernetes.io/docs/concepts/services-networking/ingress/#resource-backend
  * https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment

<details> <summary>Yaml Ingress-Inginx for k8s</summary>

```yaml nginx-ingress
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

</details>

* move it into **k8s/deploy.yam**
* change app name fron *nginx* to **python-app** for example
* extend app name modification in spec selector and template
* set replicas to 1 for the démo
* change container name as well
* use our image from our dockerhub account (${YourDockerHubLogin}/pyhton-app v2)

```bash
vim k8s/deploy.yaml
```

our [k8s/deploy.yaml](k8s/deploy.yaml)

### deploy nginx

```bash
kubectl apply -f k8s/deploy.yaml
```

<details> <summary>results</summary>

```bash result
   deployment.apps/python-app created
```

</details>

* check deployment

```bash
kubectl get deployments
```

<details> <summary>results</summary>

```bash result
   NAME         READY   UP-TO-DATE   AVAILABLE   AGE
   python-app   1/1     1            1           101s
```

</details>

## 6 - Create k8s Services

how do we access our deployed application via broswer ?

* copy definig a service
  * https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service
  * https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/simple-service.yaml


<details> <summary>Yaml kind Application service  for k8s</summary>

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

</details>

* move it inside **k8s/service.yaml**
* change *my-service* *MyApp* by the name of our service **python-app** in deployment.yaml
* set the host "source" port (port forwarded exposed from we look on host) and the container target port (container port to reach)

```bash
vim k8s/service.yaml
```

our [k8s/service.yaml](k8s/service.yaml)

### apply k8s/service.yaml

```bash
kubectl apply -f k8s/service.yaml
```

<details> <summary>results</summary>

```bash result
   service/python-app created
```

</details>

* check service

```bash
kubectl get svc
```

<details> <summary>results</summary>

```bash result
   NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
   kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP    3h7m
   python-app   ClusterIP   10.96.163.6   <none>        8080/TCP   3m20s
```

</details>

* check forwarding, look for endpoints, one is enough

```bash
kubectl describe svc python-app
```

<details> <summary>results</summary>

```bash result
   Name:                     python-app
   Namespace:                default
   Labels:                   <none>
   Annotations:              <none>
   Selector:                 app=python-app
   Type:                     ClusterIP
   IP Family Policy:         SingleStack
   IP Families:              IPv4
   IP:                       10.96.163.6
   IPs:                      10.96.163.6
   Port:                     <unset>  8080/TCP
   TargetPort:               5000/TCP
   Endpoints:                10.244.0.8:5000
   Session Affinity:         None
   Internal Traffic Policy:  Cluster
   Events:                   <none>
```

</details>

## 7 - Expose the application

* copy definig a ingress resource sample
  * https://kind.sigs.k8s.io/docs/user/ingress/
  * https://kubernetes.io/docs/concepts/services-networking/ingress/#the-ingress-resource


<details> <summary>Yaml ingress networking for k8s</summary>

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx-example
  rules:
  - http:
      paths:
      - path: /testpath
        pathType: Prefix
        backend:
          service:
            name: test
            port:
              number: 80
```

</details>

* move it inside **k8s/ingress.yaml**
* change *my-service* *MyApp* by the name of our service **python-app** in deployment.yaml
* check ingressClassName with kubectl get ingressclassname (not really necessary because we have just one - can remove this line) 
* set the host "source" port (port forwarded exposed), check in service.yaml  targetPort
* set the host at "python-app.test.com"

```bash
kubectl get ingressclass
```

<details> <summary>results</summary>

```bash result
   NAME    CONTROLLER             PARAMETERS   AGE
   nginx   k8s.io/ingress-nginx   <none>       23h
```

</details>

* it is nginx

```bash
vim k8s/ingress.yaml
```

our [k8s/ingress.yaml](k8s/ingress.yaml)

* edit [/etc/hosts](/Windows/System32/drivers/etc/hosts) as admin (ex blocnotes), add our host at the end

<details> <summary>[/etc/hosts](/Windows/System32/drivers/etc/hosts)</summary>

```txt
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
....
127.0.0.1 python-app.test.com
```

</details>

* save the /etc/hosts

### apply k8s/ingress.yaml

```bash
kubectl apply -f k8s/ingress.yaml
```

<details> <summary>results</summary>

```bash result
   ingress.networking.k8s.io/python-app created
```

</details>

* check our ingress

```bash
kubectl get ing
```

<details> <summary>results</summary>

```bash result
   NAME         CLASS   HOSTS                 ADDRESS   PORTS   AGE
   python-app   nginx   python-app.test.com             80      18s
```

</details>

* check our aplication
* **it is created on port 80, and visible in our host browser at http://python-app.test.com/**

## Clean k8s hand made ingress, service and deployment

```bash
cd k8s
kubectl delete -f ingress.yaml
```


<details> <summary>results</summary>

```bash result
  ingress.networking.k8s.io "python-app" deleted from default namespace
```

</details>

```bash
kubectl delete -f service.yaml
```

<details> <summary>results</summary>

```bash result
  service "python-app" deleted from default namespace
```

</details>

```bash
kubectl delete -f deploy.yaml
```

<details> <summary>results</summary>

```bash result
  deployment.apps "python-app" deleted from default namespace
```

</details>

# Helm

### pre-requisites

* we are looged in docker hub

```bash 
docker login -u ${YourDockerHubLogin}
```

* k8s resources set applied with files are deleted

```bash
cd ~/src/backstage/pyhton-app/
```

```bash
kubectl delete -f k8s/ingress.yaml -f k8s/service.yaml -f k8s/deploy.yaml
```

<details> <summary>results</summary>

```bash result
  ingress.networking.k8s.io "python-app" deleted from default namespace
  service "python-app" deleted from default namespace
  deployment.apps "python-app" deleted from default namespace
```

</details>

* 127.0.0.1 python-app.test.com is still configured in [etc/hosts](/Windows/System32/drivers/etc/hosts)

* kindest/node mapping is working

```bash
docker ps # check mapping 80->80 443->443 38275->6443
```

<details> <summary>results</summary>

```bash result
  CONTAINER ID   IMAGE                  COMMAND                  CREATED       STATUS       PORTS                                                                 NAMES
  685317923bcd   kindest/node:v1.34.0   "/usr/local/bin/entr…"   2 hours ago   Up 2 hours   0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 127.0.0.1:38275->6443/tcp   kind-control-plane
```

</details>

* Local cluster kind is running

```bash
kubectl cluster-info --context kind-kind
```

<details> <summary>results</summary>

```bash result
  Kubernetes control plane is running at https://127.0.0.1:XXXXX
  CoreDNS is running at https://127.0.0.1:XXXXX/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

  To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

</details>

* Ingress nginx controller is running

```bash
kubectl get pods -n ingress-nginx
```

<details> <summary>results</summary>

```bash result
  NAME                                        READY   STATUS      RESTARTS   AGE
  ingress-nginx-admission-create-8mv4f        0/1     Completed   0          108s
  ingress-nginx-admission-patch-lrhxr         0/1     Completed   0          108s
  ingress-nginx-controller-68697cf9d9-pxg9n   1/1     Running     0          108s
```

</details>

## Helm Installation

* https://github.com/helm/helm/releases checksum
* https://helm.sh/docs/intro/install/#from-apt-debianubuntu

```bash
sudo apt-get install curl gpg apt-transport-https --yes
curl -fsSL https://packages.buildkite.com/helm-linux/helm-debian/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/helm.gpg] https://packages.buildkite.com/helm-linux/helm-debian/any/ any main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

*wait for update and then helm installation*

```bash
helm version
```

<details> <summary>results</summary>

```bash result
  version.BuildInfo{Version:"v3.19.2", GitCommit:"8766e718a0119851f10ddbe4577593a45fadf544", GitTreeState:"clean", GoVersion:"go1.24.9"}
```

</details>

### Create our Chart under wls2 ubuntu

```bash
cd ~/src/backstage/pyhton-app/
```

```bash
mkdir charts; cd charts
helm create python-app
```

<details> <summary>results</summary>

```bash result
   Creating python-app
```

</details>

*It has created a directory with a charts directory, it is our python-app charts.*

```bash
cd python-app
ls
```

<details> <summary>results</summary>

```bash result
   Chart.yaml  charts  templates  values.yaml
```

</details>

* we need the three files Chart.yaml  templates  values.yaml
* we look the template directory

```bash
charts/python-app-wsl2/$ ls -al templates
```

<details> <summary>results</summary>

```bash result
   total 24
   drwxrwxrwx 1 lucile lucile  512 Nov 19 15:11 .
   drwxrwxrwx 1 lucile lucile  512 Nov 19 15:17 ..
   -rwxrwxrwx 1 lucile lucile 2850 Nov 19 15:11 NOTES.txt
   -rwxrwxrwx 1 lucile lucile 1862 Nov 19 15:11 _helpers.tpl
   -rwxrwxrwx 1 lucile lucile 2420 Nov 19 15:11 deployment.yaml
   -rwxrwxrwx 1 lucile lucile 1015 Nov 19 15:11 hpa.yaml
   -rwxrwxrwx 1 lucile lucile  969 Nov 19 15:11 httproute.yaml
   -rwxrwxrwx 1 lucile lucile 1112 Nov 19 15:11 ingress.yaml
   -rwxrwxrwx 1 lucile lucile  385 Nov 19 15:11 service.yaml
   -rwxrwxrwx 1 lucile lucile  405 Nov 19 15:11 serviceaccount.yaml
   drwxrwxrwx 1 lucile lucile  512 Nov 19 15:11 tests
```

</details>

### Configure

we must have the same sort of configuration we did in k8s/, we adapt the values.yaml to respect the our k8s/ files :

* change image repository: luspokvenus/python-app
* change image appVersion: tag: "v2"
* change service ports: 5000 (because they assume container target is identical to host source port in the deployment templates)
* change ingress: enabled: true
* set the ingress hosts host at "python-app.test.com"
* set the ingress hosts pathType at Prefix
* set tge serviceAccount create at false
* set resources requests cpu and memory at 30m and 30Mi
* config livenessProbe paths at /api/v1/healthz
* check ingressClassName with kubectl get ingressclassname (not really necessary because we have just one - can remove this line)

```bash
# get className of ingress
kubectl get ingressclass
```

<details> <summary>results</summary>

```bash result
  NAME    CONTROLLER             PARAMETERS   AGE
  nginx   k8s.io/ingress-nginx   <none>       23h
  # it is nginx
```

</details>

* Edit python-app chart values.yaml

```bash
charts/python-app$ vim values.yaml
```

our [charts/python-app/values.yaml](charts/python-app/values.yaml)

## Install our helm chart service, deployment and ingress with heml

```bash
charts/python-app$ helm install python-app --create-namespace -n python .
```

<details> <summary>results</summary>

```bash result
  NAME: python-app
  LAST DEPLOYED: Fri Nov 21 15:43:04 2025
  NAMESPACE: python
  STATUS: deployed
  REVISION: 1
  TEST SUITE: None
  NOTES:
  1. Get the application URL by running these commands:
    http://python-app.test.com/
```

</details>

* Got python name space now

```bash
kubectl get ns
```

<details> <summary>results</summary>

```bash result
   NAME                 STATUS   AGE
   default              Active   9h
   ingress-nginx        Active   9h
   kube-node-lease      Active   9h
   kube-public          Active   9h
   kube-system          Active   9h
   local-path-storage   Active   9h
   python               Active   3m30s
```

</details>

* Got nginx

```bash
kubectl get ing -n python
```

<details> <summary>results</summary>

```bash result
   NAME         CLASS   HOSTS                 ADDRESS     PORTS   AGE
   python-app   nginx   python-app.test.com   localhost   80      4m43s
```

</details>

* Got 1/1 ready and Running pod in python namespace

```bash
kubectl get pods -n python
```

<details> <summary>results</summary>

```bash result
   NAME                        READY   STATUS    RESTARTS        AGE
   python-app-d9b9cd5f-22cx6   1/1     Running   7 (2m54s ago)   11m
```

</details>

* Got kind-control-plane  Ready in in python namespace

```bash
kubectl get nodes -n python
```

<details> <summary>results</summary>

```bash result
   NAME                 STATUS   ROLES           AGE   VERSION
   kind-control-plane   Ready    control-plane   26h   v1.34.0
```

</details>

* Got python-app service on port 5000

```bash
kubectl get services -n python
```

<details> <summary>results</summary>

```bash result
   NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
   python-app   ClusterIP   10.96.86.124   <none>        5000/TCP   10m
```

</details>

* Got deployment READY 1/1 & Available

```bash
kubectl get deployment -n python
```

<details> <summary>results</summary>

```bash result
   NAME         READY   UP-TO-DATE   AVAILABLE   AGE
   python-app   1/1     1            1           8m18s
```

</details>

* Got all : ingress,pods,nodes,services,deploments and secrets at once

```bash
kubectl get ing,po,no,svc,deployments,secrets -n python
```

## Clean helm chart deployment

```bash
cd ~/charts/python-app
helm uninstall python-app -n python
```

<details> <summary>results</summary>

```bash result
   release "python-app" uninstalled
```

</details>

* Verify, it is gone, pod terminated

```bash
kubectl get ing,po,no,svc,deployment,secrets -n python
```

<details> <summary>results</summary>

```bash result
   NAME                            READY   STATUS        RESTARTS   AGE
   pod/python-app-d9b9cd5f-85m6l   1/1     Terminating   0          34s
   
   NAME                      STATUS   ROLES           AGE    VERSION
   node/kind-control-plane   Ready    control-plane   2d8h   v1.34.0
```

</details>

```bash
kubectl get no --context kind-kind
```

<details> <summary>results</summary>

```bash result
   NAME                      STATUS   ROLES           AGE    VERSION
   node/kind-control-plane   Ready    control-plane   2d8h   v1.34.0  
```

</details>

## ArgoCD

[Argo Proj - helm](https://github.com/argoproj/argo-helm)
[Argo-helm argo-cd charts](https://github.com/argoproj/argo-helm/blob/main/charts/argo-cd/README.md)

### ArgoCD Install

#### Add Heml Argo Repo

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

<details> <summary>results</summary>

```bash result
   "argo" has been added to your repositories
```

</details>

```bash
helm repo ls
```

<details> <summary>results</summary>

```bash result
   NAME    URL
   argo    https://argoproj.github.io/argo-helm
```

</details>

#### Create ArgoCD Heml Chart

```bash
cd ~/src/backstage/pyhton-app/
```

```bash
cd charts; mkdir argocd; cd argocd
vim values-argo.yaml
```

<details> <summary>charts/argocd/values-argo.yaml</summary>

```yaml values-argo.yaml
redis-ha:
  enabled: false

controller:
  replicas: 1

server:
  replicas: 1

repoServer:
  replicas: 1

applicationSet:
  replicas: 1

# adding ingress stuff
global:
  domain: argocd.test.com

certificate:
  enabled: true

server:
  ingress:
    enabled: true
    ingressClassName: nginx
    tls: true
```

</details>

#### Install ArgoCD Heml Chart

```bash
 helm upgrade --install argocd argo/argo-cd -n argocd --create-namespace -f values-argo-org.yaml
```

<details> <summary>results</summary>

```bash result
   
   Release "argocd" has been upgraded. Happy Helming!
   NAME: argocd
   LAST DEPLOYED: Sun Nov 23 12:50:26 2025
   NAMESPACE: argocd
   STATUS: deployed
   REVISION: 2
   TEST SUITE: None
   NOTES:
   In order to access the server UI you have the following options:

   1. kubectl port-forward service/argocd-server -n argocd 8080:443
      and then open the browser on http://localhost:8080 and accept the certificate

   2. enable ingress in the values file `server.ingress.enabled` and either

         - Add the annotation for ssl passthrough: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-1-ssl-passthrough

         - Set the `configs.params."server.insecure"` in the values file and terminate SSL at your ingress: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-2-multiple-ingress-objects-and-hosts

   After reaching the UI the first time you can login with username: admin and the random password generated during the installation. You can find the password by running:
   
   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
   
   (You sh ould delete the initial secret afterwards as suggested by the Getting Started Guide: https://argo-cd.readthedocs.io/en/stable/getting_started/#4-login-using-the-cli)
```

</details>

#### Check ArgoCD Install

* Look ArgoCD pods :

```bash
kubectl get pods -n argocd
```

<details> <summary>results</summary>

```bash result
   NAME                                                READY   STATUS    RESTARTS       AGE
   argocd-**application-controller-**0                     1/1     Running   0              3h22m
   argocd-**applicationset-controller**-5bd4b9d9c8-sgz7j   1/1     Running   0              3h22m
   argocd-**dex-server**-86679756f6-8pf8k                  1/1     Running   0              3h22m
   argocd-**notifications-controller**-6555f94d8b-96l7n    1/1     Running   0              3h22m
   argocd-**redis**-57986d4b7d-zdhw7                       1/1     Running   0              3h22m
   argocd-**repo-server**-65f76988cf-2hwn2                 1/1     Running   1 (122m ago)   3h22m
   argocd-**server**-84d8757478-7dzwh                      1/1     Running   0              3h22m
```

</details>

* Look ArgoCD ingress :

```bash
kubectl get ing -n argocd
```

<details> <summary>results</summary>

```bash result
   NAME            CLASS   HOSTS             ADDRESS     PORTS     AGE
   argocd-server   nginx   argocd.test.com   localhost   80, 443   3h22m
```

</details>

* Look ingress, podsn nodesn services and deploments for argocd namespace [!NOTE] :

```bash
kubectl get ing,po,no,svc,deployment,secrets -n argocd
```

<details> <summary>results</summary>

```bash result
   NAME                                      CLASS   HOSTS             ADDRESS     PORTS     AGE
   ingress.networking.k8s.io/argocd-server   nginx   argocd.test.com   localhost   80, 443   3d22h
   
   NAME                                                    READY   STATUS    RESTARTS       AGE
   pod/argocd-application-controller-0                     1/1     Running   2 (21h ago)    3d22h
   pod/argocd-applicationset-controller-5bd4b9d9c8-sgz7j   1/1     Running   2 (21h ago)    3d22h
   pod/argocd-dex-server-86679756f6-8pf8k                  1/1     Running   2 (21h ago)    3d22h
   pod/argocd-notifications-controller-6555f94d8b-96l7n    1/1     Running   2 (21h ago)    3d22h
   pod/argocd-redis-57986d4b7d-zdhw7                       1/1     Running   2 (21h ago)    3d22h
   pod/argocd-repo-server-65f76988cf-2hwn2                 1/1     Running   71             3d22h
   pod/argocd-server-84d8757478-7dzwh                      1/1     Running   11 (49m ago)   3d22h

   NAME                      STATUS   ROLES           AGE     VERSION
   node/kind-control-plane   Ready    control-plane   6d20h   v1.34.0

   NAME                                       TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
   service/argocd-applicationset-controller   ClusterIP   10.96.67.204    <none>        7000/TCP            3d22h
   service/argocd-dex-server                  ClusterIP   10.96.254.118   <none>        5556/TCP,5557/TCP   3d22h
   service/argocd-redis                       ClusterIP   10.96.170.5     <none>        6379/TCP            3d22h
   service/argocd-repo-server                 ClusterIP   10.96.107.155   <none>        8081/TCP            3d22h
   service/argocd-server                      ClusterIP   10.96.51.228    <none>        80/TCP,443/TCP      3d22h

   NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/argocd-applicationset-controller   1/1     1            1           3d22h
   deployment.apps/argocd-dex-server                  1/1     1            1           3d22h
   deployment.apps/argocd-notifications-controller    1/1     1            1           3d22h
   deployment.apps/argocd-redis                       1/1     1            1           3d22h
   deployment.apps/argocd-repo-server                 1/1     1            1           3d22h
   deployment.apps/argocd-server                      1/1     1            1           3d22h
   
   NAME                                  TYPE                 DATA   AGE
   secret/argocd-initial-admin-secret    Opaque               1      3d22h
   secret/argocd-notifications-secret    Opaque               0      3d22h
   secret/argocd-redis                   Opaque               1      3d22h
   secret/argocd-secret                  Opaque               5      3d22h
   secret/creds-731608270                Opaque               4      26m
   secret/repo-3812325848                Opaque               4      37m
   secret/sh.helm.release.v1.argocd.v1   helm.sh/release.v1   1      3d22h
   secret/sh.helm.release.v1.argocd.v2   helm.sh/release.v1   1      3d22h
   secret/sh.helm.release.v1.argocd.v3   helm.sh/release.v1   1      3d18h
```

</details>

* look directly https//argocd.test.com on our host won't work
* add it in [etc/hosts](/Windows/System32/drivers/etc/hosts) as admin
* ArgoCD is publihsed https//argocd.test.com on our host

* Recall - See all
  
```bash
kubectl cluster-info
kubectl cluster-info --context kind-kind
kubectl get ing,po,no,svc,deploy,secrets,rs,ep,jobs -n ingress-nginx
kubectl get ing,po,no,svc,deploy,secrets,rs,ep,jobs -n python
kubectl get ing,po,no,svc,deploy,secrets,rs,ep,jobs -n argocd
helm repo ls
```

#### Login ArgoCD

* get admin password

```bash
kubectl get secrets -n argocd
kubectl get secrets -n argocd argocd-initial-admin-secret -o yaml
echo "THEPASSWORD:)GIVENINLINE3" | base64 -d
```

<details> <summary>results</summary>

```bash result
TODO
```

</details>

```bash
kubectl get secrets -n argocd argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d
```

* You can log as admin with echoed decoded password

* Commit and push your project on github

```bash 
git status
git add charts
git commit -a -m "argo with https"
git push origin
```

#### In ArgoCD add your repository

* https
* git
* no login/password

|action | repos | create | delete |
|------ |-----  |------  |------  | 
| Argo repo  | ![repos](docs/images/argocd_repos.png)| ![add repo](docs/images/add-argocd-http-repo.png) | ![disconnect](docs/images/disconnect-repo.png)  |
| Argo appli | ![applis](docs/images/argocd_applis.png) | ![create appli](docs/images/create-application.png) | ![delete](docs/images/delete-application.png) |
| CI/CD Action Setting | ![CI/CD Action Settings](docs/images/cicd_action_setting.png) |  |  |


## CI in github

### CI script

https://github.com/docker/build-push-action

* we take an example of build-push for ci

<details> <summary>.github/workflows/ci.yaml</summary>

```yaml
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      -
        name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      -
        name: Build and push
        uses: docker/build-push-action@v6
        with:
          push: true
          tags: user/app:latest
```

</details>


* we create .github/workflows/cicd.yaml (all yaml of this folder will be executed)

* we rename cicd as we group both CI and CD (educ)
* we set the path and branch for **on** contraint CI action : our src folder and main branch - like this only the python code will imply CI/CD (educ)  [!TIP] TO_XTD java ~spring, php ~laravel|symfony, rust ~?, es6 ~nodeJs or newer javascript server framework - extend with BD and ORM + reparated fronts in React, + LLM, Angular and Vue -> POC **0Day**
* we keep ubuntu (educ)  [!TIP] TO_XTD try with alpine or lighter os, or coco os containers...
* we add shorten commit id sample (educ)
* we keep login in docker hub (we have to provid/configure login & pass)
* we remove QEMU and Buildx (educ) [!TIP] TO_XTD proxmox, vmare, qemu, buildx, coco are very interesting - vagrant & packer ?
* change the tags with our git hub image (docker image ls --no-trunc, take repository name)
* add outputs with the commit_id

<details> <summary>.github/workflows/cicd.yaml</summary>

```yaml
name: cicd

on:
  push:
    paths:
      - src/**
    branches:
      - main

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:

      - name: Shorten commit id
        shell: bash
        run: |
          echo "COMMIT_ID=${GITHUB_SHA::6}" >> "$GITHUB_ENV"
      -
        name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      -
        name: Build and push
        uses: docker/build-push-action@v6
        with:
          push: true
          tags: luspokvenus/python-app:${{ env.COMMIT_ID }}
    outputs:
      commit_id: ${{ env.COMMIT_ID }}
```

</details>

### Add CI secrets

| secret names       | url & image |
|-----               |---------    |
| DOCKERHUB_USERNAME | https://github.com/your-own-github-account/backstage/settings/secrets/actions  |
| DOCKERHUB_TOKEN    | ![repository secrets](docs/images/repo_secrets_github.png) |
| Dev Tokens | ![deve_settings_tokens](docs/images/dev_settings_tokens.png) |

* We add a classic token with basic repo + workflow permissions on github developper settings
* We update out .git/config with the token

```yaml
url = https://your-own-github-account:the_long_token_given_at_creationQ@github.com/your-own-github-account/backstage.git
```

## we add CD 

### Add k8s Runners

#### prerequisites

* we have github personnal access tokens for repo, admin:org and  admin:repo_hook
* kubectl works
* helm works
* we have a local cluster (kind)
* have a cert-manager in our cluster

#### UnInstall a Cert-Manager

* Ensure that all cert-manager resources that have been created by users have been deleted
  
```bash
kubectl get Issuers,ClusterIssuers,Certificates,CertificateRequests,Orders,Challenges --all-namespaces
```

* uninstall using regular manifest (ex 1.8.2)
  
```bash
kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml
```

* cowboy uninstall

```bash
for ns in ``kubectl get namespace -o jsonpath='{.items[*].metadata.name}'`; do
   kubectl delete lease -n $ns cert-manager-cainjector-leader-election cert-manager-controller
done
```

* uninstall using helm

```bash 
helm uninstall cert-manager -n cert-manager
```

<details> <summary>results</summary>

```bash result
These resources were kept due to the resource policy:
[CustomResourceDefinition] certificaterequests.cert-manager.io
[CustomResourceDefinition] certificates.cert-manager.io
[CustomResourceDefinition] challenges.acme.cert-manager.io
[CustomResourceDefinition] clusterissuers.cert-manager.io
[CustomResourceDefinition] issuers.cert-manager.io
[CustomResourceDefinition] orders.acme.cert-manager.io

release "cert-manager" uninstalled
```

</details>

#### Install a Cert-Manager in our local cluster

[cert manager](https://cert-manager.io/docs/installation/)

* Cert manager install with kubectl (ex 1.8.2)

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml
```

<details> <summary>results</summary>

```bash result

namespace/cert-manager created
customresourcedefinition.apiextensions.k8s.io/certificaterequests.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/certificates.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/challenges.acme.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/clusterissuers.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/issuers.cert-manager.io created
customresourcedefinition.apiextensions.k8s.io/orders.acme.cert-manager.io created
serviceaccount/cert-manager-cainjector created
serviceaccount/cert-manager created
serviceaccount/cert-manager-webhook created
configmap/cert-manager-webhook created
clusterrole.rbac.authorization.k8s.io/cert-manager-cainjector created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-issuers created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-clusterissuers created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-certificates created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-orders created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-challenges created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-ingress-shim created
clusterrole.rbac.authorization.k8s.io/cert-manager-view created
clusterrole.rbac.authorization.k8s.io/cert-manager-edit created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-approve:cert-manager-io created
clusterrole.rbac.authorization.k8s.io/cert-manager-controller-certificatesigningrequests created
clusterrole.rbac.authorization.k8s.io/cert-manager-webhook:subjectaccessreviews created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-cainjector created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-issuers created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-clusterissuers created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-certificates created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-orders created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-challenges created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-ingress-shim created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-approve:cert-manager-io created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-controller-certificatesigningrequests created
clusterrolebinding.rbac.authorization.k8s.io/cert-manager-webhook:subjectaccessreviews created
role.rbac.authorization.k8s.io/cert-manager-cainjector:leaderelection created
role.rbac.authorization.k8s.io/cert-manager:leaderelection created
role.rbac.authorization.k8s.io/cert-manager-webhook:dynamic-serving created
rolebinding.rbac.authorization.k8s.io/cert-manager-cainjector:leaderelection created
rolebinding.rbac.authorization.k8s.io/cert-manager:leaderelection created
rolebinding.rbac.authorization.k8s.io/cert-manager-webhook:dynamic-serving created
service/cert-manager created
service/cert-manager-webhook created
deployment.apps/cert-manager-cainjector created
deployment.apps/cert-manager created
deployment.apps/cert-manager-webhook created
mutatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook created
validatingwebhookconfiguration.admissionregistration.k8s.io/cert-manager-webhook created
```

</details>

* check pods are ready

  * *long resource names*

```bash
kubectl get nodes,pods,services,deployments -n cert-manager
```

  * *short resource names*

```bash
kubectl get no,deploy,svc,po -n cert-manager
```

<details> <summary>results</summary>

* not ready

```bash result
NAME                      STATUS   ROLES           AGE   VERSION
node/kind-control-plane   Ready    control-plane   10d   v1.34.0

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/cert-manager              0/1     1            0           9m41s
deployment.apps/cert-manager-cainjector   0/1     1            0           9m41s
deployment.apps/cert-manager-webhook      0/1     1            0           9m41s

NAME                           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/cert-manager           ClusterIP   10.96.21.113   <none>        9402/TCP   9m42s
service/cert-manager-webhook   ClusterIP   10.96.197.96   <none>        443/TCP    9m41s

NAME                                           READY   STATUS              RESTARTS   AGE
pod/cert-manager-77fb4684d6-78bxg              0/1     ImagePullBackOff    0          9m41s
pod/cert-manager-cainjector-69cdcd8845-2hb74   0/1     ContainerCreating   0          9m41s
pod/cert-manager-webhook-55499ffd6b-k5lt4      0/1     ContainerCreating   0          9m41s

```

* ok

```bash result ok

NAME                      STATUS   ROLES           AGE   VERSION
node/kind-control-plane   Ready    control-plane   10d   v1.34.0

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/cert-manager              1/1     1            1           50m
deployment.apps/cert-manager-cainjector   1/1     1            1           50m
deployment.apps/cert-manager-webhook      1/1     1            1           50m

NAME                           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/cert-manager           ClusterIP   10.96.21.113   <none>        9402/TCP   50m
service/cert-manager-webhook   ClusterIP   10.96.197.96   <none>        443/TCP    50m

NAME                                           READY   STATUS    RESTARTS   AGE
pod/cert-manager-77fb4684d6-78bxg              1/1     Running   0          50m
pod/cert-manager-cainjector-69cdcd8845-2hb74   1/1     Running   0          50m
pod/cert-manager-webhook-55499ffd6b-k5lt4      1/1     Running   0          50m

```

</details>

* Check with [cmctl](https://cert-manager.io/docs/reference/cmctl/#installation)

```bash
cmctl check api
```

* Cert-manager installation using helm
  
  * **doc** : [cert-manager install with helm](https://cert-manager.io/docs/installation/helm/#installing-with-helm)

  * [!IMPORTANT] cert-manager manages **non-namespaced resources** in your cluster.
  * [!IMPORTANT] check signatures

```bash
curl -LO https://cert-manager.io/public-keys/cert-manager-keyring-2021-09-20-1020CF3C033D4F35BAE1C19E1226061C665DF13E.gpg

helm install \
  cert-manager oci://quay.io/jetstack/charts/cert-manager \
  --version v1.19.1 \
  --namespace cert-manager \
  --create-namespace \
  --verify \
  --keyring ./cert-manager-keyring-2021-09-20-1020CF3C033D4F35BAE1C19E1226061C665DF13E.gpg \
  --set crds.enabled=true
```

#### Custom Resource Definitions (CRDs)

* add CRDs with 

```bash
kubectl apply -f https://github.com/actions-runner-controller/actions-runner-controller/releases/latest/download/actions.runner-controller.crds.yaml
```

<details> <summary>results</summary>

```bash result
TODO
```

</details>

#### Actions Runner Controller (ARC)

* doc [quick start ARC](https://github.com/actions/actions-runner-controller/blob/master/docs/quickstart.md)

* add ARC repository

```bash
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```

<details> <summary>results</summary>

```bash result
"actions-runner-controller" has been added to your repositories
```

</details>

```bash
helm repo update
```

<details> <summary>results</summary>

```bash result
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "actions-runner-controller" chart repository
...Successfully got an update from the "argo" chart repository
Update Complete. ⎈Happy Helming!⎈
```

</details>

* helm install of ARC

```bash
helm upgrade --install --namespace actions-runner-system --create-namespace\
  --set=authSecret.create=true\
  --set=authSecret.github_token="REPLACE_YOUR_TOKEN_HERE"\
  --wait actions-runner-controller actions-runner-controller/actions-runner-controller
```

<details> <summary>results</summary>

```bash result
NAME: actions-runner-controller
LAST DEPLOYED: Tue Dec  2 11:17:09 2025
NAMESPACE: actions-runner-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
1. Get the application URL by running these commands:
  export POD_NAME=$(kubectl get pods --namespace actions-runner-system -l "app.kubernetes.io/name=actions-runner-controller,app.kubernetes.io/instance=actions-runner-controller" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace actions-runner-system $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace actions-runner-system port-forward $POD_NAME 8080:$CONTAINER_PORT
```

</details>

```bash
export POD_NAME=$(kubectl get pods --namespace actions-runner-system -l "app.kubernetes.io/name=actions-runner-controller,app.kubernetes.io/instance=actions-runner-controller" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace actions-runner-system $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")

echo "pod name $POD_NAME, container port $CONTAINER_PORT"
kubectl --namespace actions-runner-system port-forward $POD_NAME 8080:$CONTAINER_PORT
```

* check http://127.0.0.1:8080 in host browser
> Client sent an HTTP request to an HTTPS server.

* verification our ARC is running
 
```bash
 kubectl get pods -n actions-runner-system
```

<details> <summary>results</summary>

```bash result
NAME                                        READY   STATUS    RESTARTS   AGE
actions-runner-controller-5577b667d-9x8rh   2/2     Running   0          11m
```

</details>


#### Deploy runners

* create ARC configuration files arc.yaml

<details> <summary>arc/runnerdeployment.yaml</summary>

```yaml
apiVersion: actions.github.com/v1alpha1
kind: RunnerDeployment
metadata:
 name: self-hosted-runners
spec:
 replicas: 1
 template:
   spec:
     repository: "${YourDockerHubLogin}/pyhton-app"
```

</details>

* apply the ARC configuration in our local cluster

```bash
kubectl apply -n actions-runner-system -f arc/runnerdeployment.yaml
```

* in a single command : 

```bash
cat << EOF | kubectl apply -n actions-runner-system -f -
apiVersion: actions.github.com/v1alpha1
kind: RunnerDeployment
metadata:
 name: self-hosted
spec:
 replicas: 1
 template:
   spec:
     repository: "${YourDockerHubLogin}/pyhton-app"
EOF
```


<details> <summary>results</summary>

```bash result
TODO
```

</details>

* check ARC installation

```bash
kubectl get pods -n actions-runner-system
```