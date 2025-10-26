from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)

print(f"Accuracy: {clf.score(X_test, y_test):.2%}")
print(f"\nPredictions: {clf.predict(X_test[:5])}")
print(f"Actual: {y_test[:5]}")

plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree for Iris Classification")
plt.savefig('decision_tree.png', dpi=150, bbox_inches='tight')
print("\nDecision tree saved as 'decision_tree.png'")
