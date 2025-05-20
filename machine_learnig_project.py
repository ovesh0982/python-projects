# 1. Supervised Learning

'''
# *Without User Input*
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# डेटा लोड करें
data = pd.read_csv("Marks.csv")  # CSV में डेटा होना चाहिए
X = data[['Hours_Studied', 'Attendance']]  # फीचर्स
y = data['Pass']  # लेबल

# डेटा बाँटना
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# मॉडल बनाना
model = LogisticRegression()
model.fit(X_train, y_train)

# भविष्यवाणी
predictions = model.predict(X_test)
print("सटीकता (Accuracy):", accuracy_score(y_test, predictions))

# नया छात्र का अनुमान
new_student = [[4, 75]]  # 4 घंटे पढ़ाई, 75% उपस्थिति
result = model.predict(new_student)
print("छात्र पास होगा?" , "हाँ" if result[0]==1 else "नहीं")
'''

'''
# *With User Input*
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# डेटा लोड करें
data = pd.read_csv("Marks.csv")
X = data[['Hours_Studied', 'Attendance']]
y = data['Pass']

# ट्रेनिंग
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# ⚡️ यूज़र से इनपुट लेना
hours = float(input("कृपया पढ़ाई के घंटे दर्ज करें (जैसे 4.5): "))
attendance = float(input("कृपया अटेंडेंस प्रतिशत दर्ज करें (जैसे 75): "))

# 📦 इनपुट को DataFrame बनाना
new_student = pd.DataFrame([[hours, attendance]], columns=['Hours_Studied', 'Attendance'])

# भविष्यवाणी करना
result = model.predict(new_student)

# ✅ परिणाम दिखाना
print("\n🔍 भविष्यवाणी:")
print("छात्र पास होगा?" , "✅ हाँ" if result[0]==1 else "❌ नहीं")
'''


# 2. Unsupervised Learning
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. डेटा लोड करें
iris = load_iris()
X = iris.data  # सिर्फ फीचर्स

# 2. K-Means मॉडल बनाएं
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# 3. परिणाम (Labels) देखें
print("क्लस्टर लेबल:", kmeans.labels_)

# 4. Visualization (2 features से)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.xlabel("पंखुड़ी की लंबाई")
plt.ylabel("पंखुड़ी की चौड़ाई")
plt.title("K-Means Clustering (Iris)")
plt.show()
