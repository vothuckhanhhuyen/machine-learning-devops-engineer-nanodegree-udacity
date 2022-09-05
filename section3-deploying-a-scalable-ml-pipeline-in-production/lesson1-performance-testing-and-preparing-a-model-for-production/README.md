## Key Points

- Validation Sets
    - In this approach, we split the training data into a train and validation set. The validation set is used to make decisions on what model to use before finally applying it to a final test set. Commonly, the validation set is between 10-30% of your overall data, but often it can be much less depending on data needs.
    - Conceptually this approach is simple and relatively fast. However, it means that your model does not get to see all the data when you train, and thus potentially leaves value on the table.

- K-Fold Cross-Validation
    - In this method, we split the data into K sets. The model is trained on K-1 then validated on the last. This process occurs K times, each time changing which fold is held out. The final validation score is the average of the metric on each fold. This leads to a more reliable measure of the performance metric since it minimizes the chance of an unlucky validation set that may not fully represent the data.
    - This approach allows your model to see all of the data since the set that is being held out changes on every iteration. However, this is computationally expensive since you must now train your model K times (albeit on a smaller data set size). Due to the cost, typically, K-Fold CV is not used for training neural networks, and instead, a validation set is used.

- Data Slicing
    - Data slicing is when we compute the metrics of our model holding a certain feature fixed.
    - For example, imagine an image classification model trained to recognize different animals. In general, we want to know the model's overall performance, but we may also want to know specifically how well it does on each class. For instance, if the model performs really well on dogs, wolves, and coyotes but performs poorly on cats, lions and tigers then that would indicate a problem. Furthermore, if our data was oversampled towards canines then we might not even notice the underperformance for felines if we were to look at the overall metrics.
    - Typical model validation such as validation sets and K-Fold Cross-Validation can be thought of as looking at horizontal slices of the data, i.e. an overall view of the data and performance. Data slicing can be thought of as looking at vertical slices of the data. This is by no means a rigorous distinction but is helpful to keep in mind.

- Data Slicing Use Cases and Testing
    - Data slicing should be used in the model validation process before deploying a model. Just as you would verify overall performance, you should verify performance on all relevant slices. What counts as "relevant" is highly dependent on the type of model/data, and the domain. For example, slicing on the specialty of medical providers in a disease predictor, or race and gender in a recidivism (repeated criminal offenses) predictor.
    - The same slices that you monitor pre-deployment should also be monitored post-deployment. Of course in post-deployment, you will not have labels to compute exact metrics, but given enough examples, one can compute the output values on a given slice like classification probability and see if it is statistically similar to the same classification probability on the training data.
    ```
    pytest -v
    ```

- Model Bias
    - Commonly, a model may perform well overall but underperform on some slices. Or, insidiously, a model may perform well by every metric you throw at it but still underperform in application. There are many reasons this could happen, but one culprit that has been gaining increased awareness is data bias. This is not to be confused with the bias in "bias-variance trade-off" which is part of the model under or overfitting and model generalization.
    - Data bias can come from a multitude of sources such as human error. A few examples are
        - sampling error - when there is a mismatch between the sample and the intended population, one cause can be too small of a sample or using a biased method of collection.
        - exclusion bias - exclusion of a group from a survey, it could arise from survey methods (such as only using in-person surveys) or perhaps only collecting data from a platform that certain age-groups frequent when instead an all-age sample is desired.
        - recall bias - the human error that occurs when people are asked to recall events from the past. Data could be unreliable or clouded by external perspective.
    - Data bias can also be more systemic and stem from society-level errors such as unjust and unfair systems or stereotypes.
    - Data bias can arise during data collection, data annotation, and/or data preprocessing.

- The Aequitas Package
    - Data bias can take many forms and have many ramifications. There are a growing number of tools to classify, understand, and mitigate data bias such as What-If Tool, FairLearn, FairML, and Aequitas. Here, we will focus on Aequitas. Note, these tools are typically separate from model explainability tools such as SHAP and LIME.
    - Aequitas is used to create a bias audit report using the webapp, CLI, or Python package. In Aequitas you specify the score, label, and at least one categorical (or bucketed numerical) field and then three reports are created comparing against a reference group (often the majority). The three reports are
        - Group Metrics Results
        - Bias Metrics Results
        - Fairness Measures Results
    and collectively drill down in increasing levels of granular detail.

- Model Cards
    - Model cards are a succinct approach for documenting the creation, use, and shortcomings of a model. They should be written such that a non-expert can understand the model card's contents.
    - There is no one way to write a model card! Suggested sections include:
        - Model Details such as who made it, type of model, training/hyperparameter details, and links to any additional documentation like a paper reference.
        - Intended use for the model and the intended users.
        -  Metrics of how the model performs. Include overall performance and also key slices. A figure or two can convey a lot.
        - Data including the training and validation data. How it was acquired and processed.
        - Bias inherent either in data or model. This could also be included in the metrics or data section.
        - Caveats, if there are any.
    - Example:
        - Model Details: Justin C Smith created the model. It is logistic regression using the default hyperparameters in scikit-learn 0.24.2.
        - Intended Use: This model should be used to predict the acceptability of a car based off a handful of attributes. The users are prospective car buyers.
        - Metrics: The model was evaluated using F1 score. The value is 0.8960.
        - Data: 
            - The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Car+Evaluation). The target class was modified from four categories down to two: "unacc" and "acc", where "good" and "vgood" were mapped to "acc".
            - The original data set has 1728 rows, and a 75-25 split was used to break this into a train and test set. No stratification was done. To use the data for training a One Hot Encoder was used on the features and a label binarizer was used on the labels.
        - Bias: According to Aequitas bias is present at the unsupervised and supervised level. This implies an unfairness in the underlying data and also unfairness in the model. From Aequitas summary plot we see bias is present in only some of the features and is not consistent across metrics.

## Key Terms