## Key Points

- ETL: extract, transform, load
- The 3 Levels of MLops:
    - Level 0: This is the level where there is no MLops process. It is ok for personal projects, when learning something new, or for demos and MVPs. In all these cases the overhead of a proper MLops process might be sacrificed because of deadlines and time budget. The main features of this stage are:
        - The code is monolithic - one or few scripts or Jupyter notebooks, with limited reusability
        - The target of the development is a model, and not a ML pipeline (we will see later what this means)
        - There is limited concern for production during development, hence the model needs to be reimplemented for production, maybe by a different team
        - No awareness of the need for model monitoring and retraining
    - Level 1: As soon as you are past the proof of concept stage and you are targeting production, you should consider a more mature process, starting with level 1. These are its features:
        - The target of the development is a ML pipeline that can produce a model at any time. This makes it easy to re-train on new data, for example.
        - The pipeline is made with reusable components
        - You are tracking code, artifacts and experiments for reproducibility and transparency
        - The output of the ML pipeline is an inference artifact that contains the pre-processing steps, so these do not need to be reimplemented for production (more on this later)
        - The model is monitored in production
        - With respect to level 0, level 1 produces the following advantages:
            - Process standardization
            - Rapid prototyping
            - Faster go-to-market with new products
            - Avoid model drift
    - Level 2: This is the process for mature, large scale ML companies. Here we shift our focus from developing ML pipelines to improving the pipeline components. This assumes we already have several ML pipelines in production. The automation at this level is much higher, and we have processes for:
        - Continuous integration: every time a component is changed integration tests are run to ensure that the component works as expected
        - Continuous deployment: each component passing the tests is automatically deployed and starts running as part of the ML pipelines in production
        - Continuous Training: when a component changes or when new data arrives the ML pipelines are triggered and new models are trained, tested and deployed automatically
        - With respect to level 1, level 2 features:
            - Rapid iteration on prod pipelines and models
            - Easy A/B testing of changes
            - Easy collaboration and improvements across large teams
            - Continuous improvements in production. The customer sees a continuously-improving product

## Key Terms

- Artifact: The product of a pipeline component. It can be a file (an image, a model export, model weights, a text file...) or a directory.
- Component: One step in a Machine Learning Pipeline. In MLflow, a component is characterized by an environment file (conda.yml if you are using conda), an entry point definition file (MLproject) and one or more scripts or commands to be executed and their supporting code.
- Container: A technology to package together the entire runtime of a software, i.e., the code itself and all its dependencies and data files. Containers can be spun up quickly, and they run identically across different environments.
- Data Segregation: The process of splitting the data, for example into train and test sets.
- Environment (runtime): The environment where a software runs. In mlflow it is described by the conda.yml file (or the equivalent Dockerfile if using Docker).
- Experiment: A tracked and controlled execution of one or more related software components, or an entire pipeline. In W&B the experiment is called group.
- Hyperparameters: The parameters of a model that are set by the user and do not vary during the optimization or fit. They cannot be estimated from the data.
- Job Type: Used by W&B to distinguish different components when organizing the ML pipeline. It is mostly used for the visualization of the pipeline.
- Machine Learning Pipeline: A sequence of one or more components linked together by artifacts, and controlled by hyperparameters and/or configurations. It should be tracked and reproducible.
- Project: All the code, the experiments and the data that are needed to reach a particular goal, for example, a classification of cats vs dogs.
- Run: The minimal unit of execution in W&B and in all tracking software. It usually represents the execution of one script or one notebook, but it can sometimes contain more; for example, one script that spawns other scripts.