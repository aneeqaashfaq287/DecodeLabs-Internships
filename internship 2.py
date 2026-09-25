import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


data = {
    "Hours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass"]
}


df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFirst rows of dataset:")
print(df.head())


X = df[["Hours", "Attendance"]]
y = df["Result"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


model = DecisionTreeClassifier(random_state=42)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("\nActual Results:")
print(list(y_test))

print("\nPredicted Results:")
print(list(y_pred))


accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy * 100, "%")


new_student = [[7, 88]]

prediction = model.predict(new_student)

print("\nNew Student:")
print("Hours:", new_student[0][0])
print("Attendance:", new_student[0][1])

print("Predicted Result:", prediction[0])