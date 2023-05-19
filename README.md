# webserver-deployment

This repo hosts a basic html page and complete automated infra and ci management


# HTML code taken from `https://github.com/daviddias/static-webpage-example.git`


# NOTE:
The repo has terraform ansible code embedded inside it. Ideally terraform and ansible code will be in seperate repositories.
However for interview purpose embedded inside same repo


The application is deployed through jenkins and the jenkinsfile is present in `main` branch. the deployment is triggered through github webhooks.



# Docker usage

The docker file exists in that repo and even in the compose file.

When ever a new tag is created the jenkins pipeline will run and deploy in machine where docker swarm ins running.

While doing so that latest image tag is updated using script `update_image_tag.py` and copies the latest compose file to swarm machine and deploys

The docker swarm has already have the network `frontend` created manaully

```

docker network create   --driver overlay  frontend

```


The gitlab ci is an example created for standalone deployment by looking into docs.
