# 1. Supervised Learning :- Supervised Learning में हमारे पास इनपुट और उसके संबंधित आउटपुट (Label) दोनों होते हैं। मशीन को बताया जाता है कि कौन-सा उत्तर सही है, और मशीन उसी के आधार पर सीखती है।

# Types:-
# 1.Classification (वर्गीकरण) – जब आउटपुट कोई श्रेणी हो।
# जैसे: ईमेल Spam है या नहीं।

# 2.Regression (प्रतिगमन) – जब आउटपुट एक संख्या हो।
# जैसे: घर की कीमत का अनुमान।
'''
उदाहरण: Classification (Iris Dataset)
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # डेटा लोड करें
# iris = load_iris()
# X = iris.data
# y = iris.target

# # ट्रेन और टेस्ट सेट में बाँटना
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # मॉडल ट्रेन करें
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # भविष्यवाणी करें और सटीकता देखें
# predictions = model.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, predictions))
'''


'''
उदाहरण: Regression (California Housing Dataset)
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# डेटा लोड करें
data = fetch_california_housing()
X = data.data
y = data.target

# बाँटना
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# मॉडल बनाना
model = LinearRegression()
model.fit(X_train, y_train)

# भविष्यवाणी और त्रुटि निकालना
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
'''



# 2. Unsupervised Learning :- इसमें डाटा लेबल नहीं किया गया होता। मशीन को यह नहीं बताया जाता कि कौन सा आउटपुट सही है, वह खुद से पैटर्न पहचानती है।

# Types :- 
# 1. Clustering (समूह बनाना) – एक जैसे डेटा को एक समूह में डालना।
# 2. Dimensionality Reduction (आयाम घटाना) – अनावश्यक फीचर्स को हटाना (जैसे PCA)।


# उदाहरण: K-Means Clustering

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

# KMeans मॉडल
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Visualization
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
