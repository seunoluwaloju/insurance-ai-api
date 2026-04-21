from pathlib import Path
import pickle

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA = [
    {"age": 19, "bmi": 27.9, "smoker": "yes", "region": "southwest", "children": 0, "risk_score": 0.80},
    {"age": 18, "bmi": 33.8, "smoker": "no", "region": "southeast", "children": 1, "risk_score": 0.30},
    {"age": 28, "bmi": 33.0, "smoker": "no", "region": "southeast", "children": 3, "risk_score": 0.35},
    {"age": 33, "bmi": 22.7, "smoker": "no", "region": "northwest", "children": 0, "risk_score": 0.20},
    {"age": 32, "bmi": 28.9, "smoker": "no", "region": "northwest", "children": 0, "risk_score": 0.25},
    {"age": 46, "bmi": 33.4, "smoker": "yes", "region": "southeast", "children": 1, "risk_score": 0.85},
    {"age": 37, "bmi": 27.7, "smoker": "no", "region": "northwest", "children": 3, "risk_score": 0.40},
    {"age": 60, "bmi": 25.8, "smoker": "yes", "region": "southwest", "children": 0, "risk_score": 0.90},
]

def main() -> None:
    df = pd.DataFrame(DATA)

    X = df[["age", "bmi", "smoker", "region", "children"]]
    y = df["risk_score"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["smoker", "region"]),
        ],
        remainder="passthrough",
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(random_state=42, n_estimators=50)),
        ]
    )

    model.fit(X, y)

    output_path = Path("app/ml/model.pkl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("wb") as f:
        pickle.dump(model, f)

    print(f"Saved model to {output_path}")

if __name__ == "__main__":
    main()