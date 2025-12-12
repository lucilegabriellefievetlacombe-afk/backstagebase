# Documents for python-app

This application has two endpoints:
- `/`
- `/api/json/v1/info`
- `/api/html/v1/greetings`
- `/api/json/v1/greetings`
- `/api/json/v1/healthz`

Here you could expand on what each of these endpoints do.
- `/` : landing page
- `/api/json/v1/info` : server info & greetings in json
- `/api/html/v1/greetings` : greetings
- `/api/json/v1/greetings` : greetings in json
- `/api/json/v1/healthz` : server health in json

# How to access the app?
http://python-app.test.com/

# Hos I configure the application
* edit /etc/hosts or /Windows/System32/drivers/etc/hosts with priviledges elevation
* add the url

```powershell /Windows/System32/drivers/etc/hosts
127.0.0.1 python-app.test.com
```

# How do I run the app ?

* simple deployment

```bash
docker build -t python-app:v2 .
docker run -dp 8080:5000 python-app:v2
```

* k8s deployments

[k8s](https://github.com/lucilegabriellefievetlacombe-afk/backstagebase/tree/main?tab=readme-ov-file#1---get-kind-our-kubernetes-local-cluster)
You can check the app health by accessing this URL: `python-app.test.com/api/v1/healthz` 
