# Predict Customer Churn

- Project **Predict Customer Churn** of ML DevOps Engineer Nanodegree Udacity

## Project Description
This project aims to identify customers that are most likely to churn based on credit card. This is a clean version of `churn_notebook.ipynb`. The completed project will include a Python package that follows coding (PEP8) and engineering best practices.

## Files and data description
1. ***churn_library.py***: 
- A library of functions to find customers who are likely to churn.
2. ***churn_script_logging_and_tests.py***:
- Contain unit tests for the *churn_library.py* functions. 
- Log any errors and INFO messages. 

## Running Files
1. Create environment:
```bash
conda create --name churn_predict python=3.6 
conda activate churn_predict
```
2. Install packages:
```bash
conda install --file requirements.txt
```
3. Run churn prediction:
```bash
python churn_library.py
```
4. Test churn prediction:
```bash
python churn_script_logging_and_tests.py
```




