# Dash Component Boilerplate

This repository contains a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create your own Dash components.

## Usage

To use this boilerplate:

1. Install the requirements:
    ```
    $ pip install cookiecutter
    $ pip install virtualenv
    ```
   [Node.js/npm is also required.](https://nodejs.org/en/)
2. Run cookiecutter on the boilerplate repo:
    ```
    $ cookiecutter git@github.com:plotly/dash-component-boilerplate.git
    ```
3. Answer the questions about the project.
    - project name: Clean project name, can contains spaces and special characters.
    - component name: derived from project_name, lowercase, spaces and '-' are replaced by '_', ascii only.
    - author info: author_name and author_email for package.json metadata.
    - description: the project description, included in package.json.
    - version: The initial version.
    - license: License type for the component lib.
    - publish_on_npm: Set to false to only serve locally from the package data.
    - install_dependencies: Set to false to only generate the project structure.
4. The project will be generated in the folder of `project_shortname`.
5. Follow the directions in the generated README to start developing your new Dash component.

Installing the dependencies can take a long time. They will be installed in a
folder named `venv`, created by virtualenv. This ensures that dash is installed
to generate the components in the `build:py` script of the generated 
`package.json`.
