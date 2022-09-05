## Key Points

- Software Engineering Principle: Automation
    - Automation is the principle where we set up processes to do rote tasks for us routinely, such as on a schedule or when another action happens.
    - Automation can take many forms. For instance:
        - Code formatters such as Black which remove the need to fiddle with exact placement of spaces, parenthesis, etc. in code.
        - Editor features which vary depending on the text editor or IDE you use. For example, I have Vim set to remove EOL whitespace when saving a file since that clutters Git diffs and can break things like line continuation characters in shell scripts.
        - Pre-Commit hooks allow us to run code, like formatters, before we commit a change. Since we're going to commit our code, this saves us from having to run a formatter separately.
    Collectively, using automation helps you save time and reduces the risk of errors.
    - A related principle to automation is Don't Repeat Yourself (DRY). While not automation per se, it's a close cousin. We write functions instead of copy and pasting or rewriting code, and with automation, we set up processes instead of needing to retype or copy commands into the development environment.

- Software Engineering Principle: Testing
    - When writing code we expect it to function as we planned, but often there can be unforeseen situations or edge cases. Testing is the principle we leverage to ensure our code functions as intended and is reproducible. A robust testing suite allows us to harden our code and make us more confident that, e.g., a function that does X actually does X instead of Y.
    - If we design our tests well, it can also help us catch edge cases that otherwise would have slipped through. Furthermore, if we tweak our code it ensures that we don't alter behavior unexpectedly.
    - Tests build trust. This trust is both for yourself but also for anyone you collaborate with. A robust testing suite should be developed alongside your code such that nearly every piece of functionality has a corresponding unit test.
    - As covered in a previous course, do not forget that machine learning models are inherently stochastic and built on data. The approach to testing these may be different and rely on tools such as Great Expectations.
    - Tests are like seat belts and safety bags. Their presence is not a guarantee that harm will not befall your code, but it is a best practice that mitigates harm in case something goes awry.

- Software Engineering Principle: Versioning
    - Software projects are by their nature complex with many dependencies and constant evolution. We manage this using versioning. Versioning is how we track our finished projects (e.g. version 1.0 of our code base may have 5 features, but a subsequent version 2.0 may have 10 features).
    - A popular approach to manage this is Semantic Versioning. Using this scheme a version number contains three parts, X.Y.Z:
        - X is the major version, increment this when you have introduced API breaking changes.
        - Y is the minor version, increment this when you make backward-compatible changes.
        - Z is the patch version, increment this when you squash bugs or make smaller features.
    For example, NumPy 1.20.0 released on January 30, 2021, before that was version 1.19.2. Going from 1.19.1 to 1.19.2 there were a handful of bug fixes. The jump to 1.20.0 included entirely new functions, type annotations throughout the code base, and deprecation of some old functions. By time you read this there might even be a NumPy 1.20.1 or beyond!
    - While semantic versioning is typically used to specify software, it can also be used for the model itself. Sometimes you make small adjustments to preprocessing and then retrain a model, other times you may entirely change the training data or underlying model. These changes would represent a change in the patch version and major version, respectively.

- Continuous Integration with GitHub Actions
    - GitHub Actions is CI/CD built right into GitHub and comes with a plethora of pre-built workflows such as running your test suite or checking in if your code has any flake8 errors.
    - Setting up a GitHub Action is as straightforward as specifying when the action occurs, such as on push, what sort of VM it runs on, what programs and packages it installs, and then ultimately what commands get run. Here is a portion of the template workflow for Python that GitHub provides:
```
name: Python package # Name of the Action.

on: [push] # When this action runs.

jobs:
  build:

    runs-on: ubuntu-latest # Which OS this runs on, you can also build on Windows or MacOS.
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8] # You can build against multiple Python versions.

    steps:
    - uses: actions/checkout@v2 # Calling a pre-built GitHub Action which allows your Action to access your repository.
    - name: Set up Python ${{ matrix.python-version }} # Name of an action that sets up Python.
      uses: actions/setup-python@v2 # A pre-built GitHub Action that sets up a Python environment.
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies # The first step that isn't just calling another action.
      run: |
        python -m pip install --upgrade pip # Upgrade pip to the latest version.
        pip install pytest # Install pytest.
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi # If we have a requirements.txt, then install it.
    - name: Test with pytest # Final action which runs pytest. If any test fails, then this Action fails.
      run: |
        pytest
```
    - See the inline comments for details on the steps in this workflow.
    - Beyond CI/CD GitHub Actions can also automate actions such as greeting users when they submit their first pull request to your repository.
    - Other popular platforms for CI/CD include CircleCI, TravisCI, and Jenkins.

- Continuous Deployment with Heroku
    - Heroku is a cloud Platform-as-a-Service (PaaS) that supports a variety of languages and allows users to deploy apps. For our purposes, we will use Heroku to run a Python application that consists of an API for machine learning inference.
    - Heroku is built around the concept of lightweight containers called dynos that are easily scalable and adaptable to a variety of tasks. For our work, we will be using one web dyno to run our API.
    - The instructions for launching an app are contained in a Procfile that resides in the highest level of your project directory. This file declares the dyno type and the associated command on each line, e.g.:
```
web: uvicorn main:app
```
    - This Procfile specifies a web dyno that runs the command uvicorn which is then running a web app cleverly called app that resides in main.py.
    H- eroku makes it easy to do CD. It provides multiple different deployment options with the two most common being Git and Docker based deployments. We will leverage the GitHub connection.
    - You can connect an existing repository to Heroku either using the web GUI or the CLI and from there you can enable continuous delivery so that all changes to your code automatically get deployed to your Heroku app. Furthermore, you can specify that the CD only occurs when your continuous integration (e.g. your unit tests) succeeds. Doing this tightly couples our CI and CD processes which will help us avoid deploying a broken app.
    - When creating apps on Heroku, it's important to think of your slug and its limitations. The slug is your app and all of its dependencies, and it has a size limit of 500 MB. For light use cases all of your code, model, and even data could fit within that limit. However large models or frameworks (such as TensorFlow 2) can easily exceed the limit. Where possible, trim what is included in your slug using a .slugignore file, and in our case, we can leverage our remote DVC storage to contain our model and data and access them in our app when we need them.

## Key Terms