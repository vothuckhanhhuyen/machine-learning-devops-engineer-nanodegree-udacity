"""
Testing module that will check the churn_library.py procedure.
Artifact produced will be in logs folders.

Author: HuyenVTK1
Date: April 29, 2022
"""

import os
import logging
import pytest

from churn_library import import_data, perform_eda, encoder_helper, perform_feature_engineering, train_models

os.environ['QT_QPA_PLATFORM'] = 'offscreen'

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename="logs/churn_library.log",
    level=logging.INFO,
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s")


@pytest.fixture(name="df_raw")
def test_import():
    '''
    test data import - this example is completed for you to assist with the other test functions
    '''
    try:
        df_raw = import_data("data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert df_raw.shape[0] > 0
        assert df_raw.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err

    return df_raw


def test_eda(df_raw):
    '''
    test perform eda function
    '''
    perform_eda(df_raw)
    path = "images/eda"

    try:
        dir_val = os.listdir(path)
        assert dir_val.count("Customer_Age.jpg")
        assert dir_val.count("Total_Trans_Ct.jpg")
        assert dir_val.count("Churn.jpg")
        assert dir_val.count("Marial_Status.jpg")
        assert dir_val.count("Heatmap.jpg")
        logging.info("Testing perform_eda: SUCCESS")
    except AssertionError as err:
        logging.warning("Testing perform_eda: FAIL, not all images are saved.")
        raise err


@pytest.fixture(name="df_encoded")
def test_encoder_helper(df_raw):
    '''
    test encoder helper
    '''
    category_cols = ["Gender",
                     "Education_Level",
                     "Marital_Status",
                     "Income_Category",
                     "Card_Category"]

    df_encoded = encoder_helper(df_raw, category_cols, "Churn")

    try:
        for element in category_cols:
            assert element in df_encoded.columns
        logging.info("Testing encoder_helper: SUCCESS")
    except AssertionError as err:
        logging.error(
            "Testing encoder_helper: FAIL, some missing colmuns.")
        return err

    return df_encoded


@pytest.fixture(name="df_fe")
def test_perform_feature_engineering(df_encoded):
    '''
    test perform_feature_engineering
    '''
    X_train, X_test, y_train, y_test = perform_feature_engineering(
        df_encoded, "Churn")

    try:
        assert X_train.shape[0] > 0
        assert X_test.shape[0] > 0
        assert len(y_train) > 0
        assert len(y_test) > 0
        logging.info("Testing perform_feature_engineering: SUCCESS")
    except AssertionError as err:
        logging.error(
            "Testing perform_feature_engineering: FAIL, missing output.")
        raise err

    return X_train, X_test, y_train, y_test


def test_train_models(df_fe):
    '''
    test train_models
    '''
    X_train, X_test, y_train, y_test = df_fe[0], df_fe[1], df_fe[2], df_fe[3]
    train_models(X_train, X_test, y_train, y_test)

    path = "images/results/"
    try:
        dir_val = os.listdir(path)
        assert len(dir_val) > 0
    except FileNotFoundError as err:
        logging.error(
            "Testing train_models: FAIL, not all result images are saved")
        raise err

    path = "models/"
    try:
        dir_val = os.listdir(path)
        assert len(dir_val) > 0
        logging.info("Testing train_models: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing train_models: FAIL, not all models are saved")
        raise err


if __name__ == "__main__":
    DF_RAW = test_import()

    test_eda(DF_RAW)

    DF_ENCODED = test_encoder_helper(DF_RAW)

    X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = test_perform_feature_engineering(
        DF_ENCODED)

    test_train_models(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST)
