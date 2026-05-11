from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

_CSV_PATH = Path(__file__).resolve().parent / "Titanic-Dataset.csv"


class RoseModel:

    def __init__(self):
        self.model = DecisionTreeClassifier()
        self._X_train, self._X_test, self._y_train, self._y_test = self._prepare_data()
        self.model.fit(self._X_train, self._y_train)

    def _prepare_data(self):
        df = pd.read_csv(_CSV_PATH)
        df = df[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]].dropna().copy()
        df["Sex"] = LabelEncoder().fit_transform(df["Sex"])
        X = df.drop("Survived", axis=1)
        y = df["Survived"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def get_model(self) -> str:
        return type(self.model).__name__

    def get_accuracy(self) -> float:
        y_pred = self.model.predict(self._X_test)
        return round(accuracy_score(self._y_test, y_pred), 4)

    def get_tree(self) -> str:
        return export_text(self.model, feature_names=self._X_train.columns.tolist())
