# -*- coding: utf-8 -*-
"""
Karl Roush
Wells Fargo Campus Analytics Challenge 2018
"""
import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
names1= ['Household heating => 70F',
        'Household heating < 70F',
        'Use of heat pump',
        'Use of air conditioner',
        'shower - short',
        'shower - long (> 3 min)',
        'bath',
        'wash-up',
        'use of dishwasher',
        'use of clothes washer',
        'use of clothes dryer',
        'use of cooking range',
        'use of  oven',
        'use of self-clean feature of electric oven',
        'Small kitchen appliance in the home',
        'TV/computer use',
        'air travel - large plane',
        'air travel - small  plane (<50 seats)',
        'car trips- self only',
        'car trips - driver and self',
        'car trips - 2+ people with multiple end points',
        'trips using public ground transportation',
        'bags of garbage disposed',
        'bags of recycling deposited (negative CF)',
        'bags of compost deposited (negative CF)',
        'hazardous or electric items disposed',
        'Total CFP']
dataset1 = pandas.read_csv('ML_data.csv', names=names) #change this to whatever data you want
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#visualizing data set
## box and whisker plots
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()
#
## histograms
#dataset.hist()
#plt.show()
#
## scatter plot matrix
#scatter_matrix(dataset)
#plt.show()

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model
results = []
names = []
print('Model: Mean Acc. (Std. dev)')
for name, model in models:
    kfold = model_selection.KFold(n_splits=120, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    #msg=cv_results.std()
    print(msg)
    
## Compare Algorithms
#fig = plt.figure()
#fig.suptitle('Algorithm Comparison')
#ax = fig.add_subplot(111)
#plt.boxplot(results)
#ax.set_xticklabels(names)
#plt.show()

# Make predictions on validation dataset
#knn = KNeighborsClassifier()
#knn.fit(X_train, Y_train)
#predictions = knn.predict(X_validation)
#final_accuracy2=accuracy_score(Y_validation, predictions)
#print('KNN acc:',final_accuracy2)

svm = SVC()
svm.fit(X_train, Y_train)
predictions = svm.predict(X_validation)
final_accuracy=accuracy_score(Y_validation, predictions)
print('SVM acc:',final_accuracy)
#print(confusion_matrix(Y_validation, predictions))
#print(classification_report(Y_validation, predictions))