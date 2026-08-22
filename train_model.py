import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import (
    train_model,
    save_model,
    load_model,
    inference,
    compute_model_metrics,
    performance_on_categorical_slice,
)

project_path = "."
data_path = os.path.join(project_path, "data", "census.csv")
print(data_path)
data = pd.read_csv(data_path, skipinitialspace=True)

train, test = train_test_split(data, train_size=0.75, random_state=1)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    training=True,
    label="salary",
)

X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

model = train_model(X_train, y_train)

model_path = os.path.join(project_path, "model", "model.pkl")
save_model(model, model_path)

encoder_path = os.path.join(project_path, "model", "encoder.pkl")
save_model(encoder, encoder_path)

model = load_model(model_path)

preds = inference(model, X_test)

p, r, fb = compute_model_metrics(y_test, preds)
print(f"Precision: {p:.4f} | Recall: {r:.4f} | F1: {fb:.4f}")

with open("slice_output.txt", "w") as f:
    for col in cat_features:
        for slicevalue in sorted(test[col].unique()):
            count = test[test[col] == slicevalue].shape[0]
            p, r, fb = performance_on_categorical_slice(
                test,
                col,
                slicevalue,
                cat_features,
                "salary",
                encoder,
                lb,
                model,
            )

            print(f"{col}: {slicevalue}, Count: {count:,}", file=f)
            print(
                f"Precision: {p:.4f} | Recall: {r:.4f} | F1: {fb:.4f}",
                file=f)
