Docker & Docker Compose Restful API
====

## What is it

A restful API service for Docker Compose.

Base on [francescou/docker-compose-ui](https://github.com/francescou/docker-compose-ui)

[RESTful API documentation](https://francescou.github.io/docker-compose-ui/api.html)

## Compose file format compatibility matrix

| Compose file format  | Docker Engine |
| ------------- | ------------- |
| 3.0 ; 3.1| 1.13.0+ |
| 2.1	| 1.12.0+ |
| 2.0	| 1.10.0+ |
| 1.0	| 1.9.1+ |

## Getting started

Run the following command in terminal:

    docker run \
    --name docker-compose-ui \
    -p 5000:5000 \
    -w /opt/docker-compose-projects/ \
    -v /var/run/docker.sock:/var/run/docker.sock \
    francescou/docker-compose-ui:1.4.1

or, if you already have docker-compose installed, just `docker-compose up`.

You have to wait while Docker pulls the container from the Docker Hub: <https://hub.docker.com/r/francescou/docker-compose-ui/>

Then open your browser to `http://localhost:5000`

### Add your own docker-compose projects

to use use your own docker-compose projects run this command from the directory containing your docker-compose.yml files:

    docker run \
        --name docker-compose-ui \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        -p 5000:5000 \
        -v /var/run/docker.sock:/var/run/docker.sock \
        francescou/docker-compose-ui:1.4.1

you can download my example projects into */home/user/docker-compose-ui/demo-projects/* from https://github.com/francescou/docker-compose-ui/tree/master/demo-projects

### Load projects from a git repository (experimental)

    docker run \
    --name docker-compose-ui \
    -p 5000:5000 \
    -w /opt/docker-compose-projects-git/ \
    -v /var/run/docker.sock:/var/run/docker.sock  \
    -e GIT_REPO=https://github.com/francescou/docker-compose-ui.git \
    francescou/docker-compose-ui:1.4.1

### Note about scaling services

Note that some of the services provided by the demo projects are not "scalable" with `docker-compose scale SERVICE=NUM` because of published ports conflicts.

Check out this project if you are interested in scaling up and down a docker-compose service without having any down time: <https://github.com/francescou/docker-continuous-deployment>


### Note about volumes

since you're running docker-compose inside a container you must pay attention to volumes mounted with relative paths, see [Issue #6](https://github.com/francescou/docker-compose-ui/issues/6)

## Remote docker host

You can also run containers on a remote docker host, e.g.

    docker run \
        --name docker-compose-ui \
        -p 5000:5000 \
        -v $(pwd):$(pwd) \
        -w $(pwd) \
        -e DOCKER_HOST=remote-docker-host:2375 \
        francescou/docker-compose-ui:1.4.1


### Docker Swarm or HTTPS Remote docker host

The project has been tested against a Docker Engines 1.12 cluster ([swarm mode](https://docs.docker.com/engine/swarm/swarm-tutorial/)).

You need to add two environment properties to use an HTTPS remote docker host: `DOCKER_CERT_PATH` and `DOCKER_TLS_VERIFY`, see [example by @ymote](https://github.com/francescou/docker-compose-ui/issues/5#issuecomment-135697832)

### Authenticated docker registries

If your projects require you to pull images from a private docker registry that requires authentication, you will need to provide a `config.json` file with the necessary configuration options to the docker-compose-ui container at `/root/.docker/config.json`. You can generate the file on any host by performing `docker login [your private registry address]` and copying the resulting file from your ~/.docker directory to where it is needed.

For example:

    docker run \
        --name docker-compose-ui \
        -p 5000:5000 \
        -w /opt/docker-compose-projects/ \
        -v /home/user/.docker/config.json:/root/.docker/config.json:ro \
        francescou/docker-compose-ui:1.4.1

## Technologies

Docker Compose UI has been developed using Flask (python microframework) to provide RESTful services and AngularJS to implement the Single Page Application web ui.

The application uses [Docker Compose](https://docs.docker.com/compose) to monitor and edit the state of a set of docker compose projects (*docker-compose.yml* files).


## API

API docs at <https://francescou.github.io/docker-compose-ui/api.html>

## Issues

If you have any problems with or questions about this image, please open a GitHub issue on https://github.com/francescou/docker-compose-ui

## License - MIT

The Docker Compose UI code is licensed under the MIT license.

Docker Compose UI: Copyright (c) 2016 Francesco Uliana. www.uliana.it/francesco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


