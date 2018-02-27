import numpy as np
from sklearn.svm import SVR
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import xml.etree.ElementTree

# #############################################################################
config = xml.etree.ElementTree.parse("settings.xml").getroot()
for atype in config.findall('output_csv'):
        model_csv = atype.text
        print model_csv
# Read data from csv
X = []
y = []

with open(model_csv, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        y.append([(int(row[0]))])
        X.append([int(float(row[1]))])

print X
print y
X = np.array(X)
y = np.array(y).ravel()


# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)

# #############################################################################
# Look at the results
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
