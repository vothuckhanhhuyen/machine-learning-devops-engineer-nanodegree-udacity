## Key Points

- A release is a static copy of the code that reflects the state of the code at a particular point in time. It has a version attached to it, and a tag. The tag can be used to restore the repository (or a local copy of the code in the repository) to the state it was when the release was cut.

- A common schema for versioning release is called Semantic Versioning: a release is made of 3 numbers, like 1.3.8. The first number is called the major version. We only increment the major version when we are making changes that break backward compatibility (i.e., a code that was running with the previous version is likely to break with the new version). The second number is called minor. We increment it when we make a significant change that is backward-compatible, i.e., code that was running with the previous version is not expected to break with the new one. And finally, we have a path number. We increment it for bug fixes and small changes that do not significantly change the behavior of the code (excluding the bugs fixed).

- Anybody can use your pipeline at version 1.0.0 with mlflow and w&b:
```
mlflow run [github URL] -v [version] -P ...
```

- There are two ways of using a model in production: Real-time and Batch.
    - Real-time (online): Here, we are interested in providing answers one at the time, typically through an API. Most of the time the performance metric that matters here is latency, i.e., the time needed to process one entity (from request to answer). An example of a real-time inference application is providing movie recommendations on a website: we want to provide the answer as quickly as possible, so that the user is not left hanging waiting for the page to load.
    - Batch (offline): Here, we are receiving several requests at once (a batch), and we want to process the entire batch in the shortest possible time. Therefore, our metric of reference here is throughput, i.e., the amount of requests per unit time that we can process. We are willing to sacrifice latency if that means that we can process more requests, in say, a second. For example, when we have a deep learning model on a GPU, we might wait until we accumulate a certain number of requests, and then send the entire batch to the GPU. Therefore, the latency for the first request that we receive will be pretty large because this request will hang until other requests are received.

- Inference artifacts in the "MLflow models" format can be used with several tools beyond MLflow itself. Some examples are:
    - Spark for offline inference (see the mlflow documentation)
    - Online inference with Seldon Core, Algorithmia, and any tool that supports pure-python inference functions (like BentoML, cnvrg.io, valohai, clearML, and more). You can also dockerize your MLflow API and deploy it directly as a REST API, such as in Kubernetes.

## Key Terms

- Release: A static copy of the code that reflects the state at a particular point in time. It has a version attached to it, and a tag. The tag can be used to restore the repository (or a local copy of the code in the repository) to the state it was when the release was cut.

- Semantic Versioning: A common schema for versioning releases. A release version is made of 3 numbers, like 1.3.8, called respectively major, minor, and patch. The major number should be incremented for large, backward-incompatible changes. The minor number should be incremented when new features are added in a backward-compatible way. The patch number should be incremented for bug fixes and other small backward-compatible changes.

- Deployment: The operation of taking an inference artifact and putting it into production, so it can serve results to stakeholders and customers.