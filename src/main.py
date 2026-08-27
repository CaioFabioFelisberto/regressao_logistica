import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('data/base_hardware.csv')

X = df.drop('status_crash', axis=1)
y = df['status_crash']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled,y_train)

y_pred = model.predict(X_test_scaled)

print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Matriz de Confusão:\n{confusion_matrix(y_test, y_pred)}\n")
print(f"Relatório:\n{classification_report(y_test, y_pred)}")
