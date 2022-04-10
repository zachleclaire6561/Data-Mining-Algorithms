import numpy as np
import scipy.io

#get matlab data as nested dictionary
training = scipy.io.loadmat('Classifiers/ECG_train.mat')
testing = scipy.io.loadmat('Classifiers/ECG_test.mat')

#extract data from dictionaries
print(training)
X_normal = training['X_train_normal'].transpose()
X_abnormal = training['X_train_abnormal'].transpose()

X_normal_test = testing['X_test_normal'].transpose()
X_abnormal_test = testing['X_test_abnormal'].transpose()

#mean = sum / # items
mean_normal = np.sum(X_normal, axis=1)/X_normal.shape[1]

mean_abnormal = np.sum(X_abnormal, axis=1)/X_abnormal.shape[1]
# True: normal; False: abnormal
def distance_classifier(item):
    return (distance(item, mean_normal) <= distance(item, mean_abnormal))

def distance(v1, v2):
    return np.norm(v1-v2, 2)

confusion_matrix = np.zeros((2,2))
print(confusion_matrix)
for i in range(0, X_normal_test.shape[0]-1):
    

for j in range(0, X_abnormal_test.shape[1]):
