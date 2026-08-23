import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from ml.data import process_data
from ml.model import compute_model_metrics, train_model


def test_one_train_model_returns_expected_algorithm_random_forest():
    """
    # Test that train_model return RandomForestClassifier
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])
    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_two_compute_model_metrics_returns_expected_values():
    """
    Test that compute_model_metrics returns float values between 0 and 1
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fb = compute_model_metrics(y, preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fb, float)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fb <= 1


def test_three_process_data_returns_expected_types():
    """
    Test that process_data returns the expected output type
    """
    data = pd.DataFrame(
        {
            "age": [16, 27, 38, 59, 72],
            "race": [
                "White",
                "Asian-Pac-Islander",
                "Amer-Indian-Eskimo",
                "Other",
                "Black"
            ],
            "sex": ["Female", "Male", "Female", "Male", "Female"],
            "salary": ["<50K", "<=50K", ">50K", ">=50K", "<50K"],
        }
    )

    categorical_features = ["race", "sex"]

    X, y, encoder, lb = process_data(
        data,
        categorical_features=categorical_features,
        label="salary",
        training=True,
    )

    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert encoder is not None
    assert lb is not None
