"""Modeling utilities: pipelines and evaluation helpers."""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import joblib
from pathlib import Path

MODELS_DIR = Path('models')
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def make_baseline_model():
    """Create a baseline logistic regression pipeline."""
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    return pipe


def train_and_evaluate(X, y, model=None, test_size=0.2, random_state=42):
    """Train a model and evaluate it."""
    if model is None:
        model = make_baseline_model()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'f1_macro': f1_score(y_test, y_pred, average='macro')
    }
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return model, metrics, report, cm


def save_model(model, path='models/best_model.joblib'):
    """Save a trained model to disk."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)

