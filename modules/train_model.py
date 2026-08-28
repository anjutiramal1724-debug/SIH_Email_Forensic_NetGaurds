# Member 1 - Anjali - Model Training Script
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from modules.advanced_features import extract_features

emails = [
    "Urgent wire transfer needed from CEO to new account bit.ly/payment",
    "Team meeting tomorrow at 10am",
    "Your PayPal account locked verify password immediately",
    "Invoice overdue #123 please pay attachment invoice.exe",
    "Hi Anjali, project report attached",
    "Boss here, transfer 50000 urgently emergency"
]
labels = [4, 0, 3, 4, 0, 4]

X_list = [list(extract_features(m).values()) for m in emails]
X = pd.DataFrame(X_list)
y = labels

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("Model Trained Successfully!")
