## Key Points

- We are going to talk now about the product of the train and validation step. Let's start with this definition:
    - An inference pipeline is an ML pipeline that contains everything that needs to run in production at inference time: a pre-processing step that transforms the data input to the data expected by the model, and then the model.
    - An inference artifact is a serialized (i.e., saved to disk) static version of the inference pipeline containing the preprocessing as well as a trained model.

- So how do we bring order exactly?
    - Version our data
    - Version our code
    - Track every experiment

- Hydra can be used to perform parameter sweeps: given a grid of parameter values, hydra will generate multiple jobs and go through the grid automatically.
    - If we want our jobs to run in parallel, we can just add the hydra/launcher=joblib specification, like:
    ```
    mlflow run . -P hydra_options="hydra/launcher=joblib parameters.a=3,4 parameters.b=range(2,4,1) -m"
    ```

- MLflow provides several flavors out of the box, and can natively export models from sklearn, pytorch, Keras, ONNX and also a generic python function flavor that can be used for custom things. When generating the model export we can provide two optional but important elements:
    - A signature, which contains the input and output schema for the data. This allows downstream tools to catch obvious schema problems.
    - Some input examples: these are invaluable for testing that everything works in downstream task

## Key Terms

- Experiment Tracking: The process of recording all the necessary pieces of information needed to inspect and reproduce a run. We need to track the code and its version, the dependencies and their versions, all the metrics of interests, all the produced artifacts (images, model exports, etc.), as well as the environment where the experiment runs.

- Hyperparameter Optimization: The process of varying one or more hyperparameter of a run in order to optimize a metric of interest (for example, Accuracy or Mean Absolute Error).

- Inference Artifact: An instance of the Inference Pipeline containing a trained model.

- Inference Pipeline: A pipeline constituted of two steps: the pre-processing step and the model. The pre-processing step can be a pipeline on its own, and it manipulates the data and prepares them for the model. The inference pipeline should contain all the pre-processing that needs to happen during model development as well as during production. When the inference pipeline is trained (i.e., it contains a trained model) it can be exported to disk. The export product is called an Inference Artifact.