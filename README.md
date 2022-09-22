# dev-u22-workspace

This template project implements a devcontainer for use as a workspace
for multiple projects.

It also includes VSCode workspace settings files and a vscode devcontainer
definition file. The default workspace settings will work well with python
projects that use https://github.com/DiamondLightSource/python3-pip-skeleton,
but other python projects and other languages will also work.

Use cases:

- Allows for personalized container environment / VSCode settings that
  don't contaminate the individual projects.
- Provides a devcontainer that can manage more than one project in
  a workspace (skeleton based projects or otherwise)
- Provides a devcontainer wrapper for projects that do not have their own
  devcontainer. Useful for collaboration projects where upstream is not
  adopting devcontainers or skeleton.
- Provides VSCode settings at the level of the Workspace

# Features

 ## Containers in Containers
Docker and Podman CLI and API are supported inside the container. They all
connect to the user podman instance running on the host.
## Global VirtualEnv
- The virtualenv /venv is already in the path and pre-populated with the
  skeleton dev dependencies.
- You are free to create additional venvs inside the container if the projects
  inside have conflicting dependencies, but this should not usually be needed.

## .bashrc_dev
- This file is mounted as /root/.bashrc and provides a starting point for
  your bash profile inside the container. Includes:
  - autocompletion for git and bash
  - shared bash history with the host
  - will also execute a personal run commands file if found at
    - $HOME/.bashrc_dev

# How to adopt
- Take a copy of the template project
  - go to https://github.com/epics-containers/vscode-python3-workspace
  - click "Use this template"
  - choose a name and organization for your workspace project
- Clone the new repo as a peer to the project or projects that it will manage
- cd into the project folder and launch vscode
  - code dev-u22.code-workspace
- Click "Reopen in a Container" when prompted
- "File -> Add Folder to Workspace" for as many peer projects as you wish
- choose ``Python: Select interpreter`` command (access via ctrl-shift-P)
  choose ``select at workspace level`` and select /venv/bin/python.

# Adopting updates

Changes you make can be committed back to your own repo. You can re-adopt
updates to the original template with the following commands.
Merge conflicts will need to be resolved where you have changed files.

```bash
cd <workspace repo folder>
# first update
git pull git@github.com:epics-containers/dev-u22-workspace.git --allow-unrelated-histories
# subsequent updates
git pull git@github.com:epics-containers/dev-u22-workspace.git
```
