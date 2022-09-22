"""
Example docker API client.

This is a demonstrator of the use of the docker API from inside the
devcontainer provided by dev-u22-workspace

To try this, start the podman_service listening on docker API socket,
install python docker, run this script and then exec a shell in the
container it launches. i.e.:

pip install docker
python demo/docker_test.py
podman exec -it python_docker sh
exit
podman rm -f python_docker
"""

from docker import from_env

docker_client = from_env()

container = docker_client.containers.run(
    "docker.io/alpine",
    detach=True,
    restart_policy={"Name": "unless-stopped"},
    volumes={"/home": {"bind": "/home2", "mode": "rw"}},
    name="python_docker",
    command="sleep 10000",
    environment={"PS1": "You are in a python created container! > "},
)
