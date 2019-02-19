# Discoteque

A little application to manage a vinyl collection and intended to practice an IDD approach on a Python application

## Requirements

- Python 3.6
- [Pipenv](https://github.com/pypa/pipenv)

## Installation

On your command line run:

`pipenv install --dev && pipenv shell`

to create a virtualenv for the project and install dependencies

## Architecture

There are two main folders on this project, `api` and `discoteque`.

As you may imagine, `api` is where the delivery mechanism lives, in this case a JSON API using Flask.

Inside `discoteque` is where domain assumes the business rules decoupled from the outer world.  It MUST NOT have any knowlede about infrastructure, delivery mechanisms, etc.  If we can achieve that, we would be able to even install our domain as a dependency inside the API project!

## Tests

There are two main levels of testing here.  Acceptance tests are written with Behave and perform requests over the Flask API.  Domain tests are written in Mamba inside the `discoteque/spec` folder.

### Running the suite
From the root folder:

- Domain tests `mamba app/discoteque/`
- Acceptance tests: PENDING


