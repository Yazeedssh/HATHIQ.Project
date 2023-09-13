import os 
import pickle
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import numpy as np 
from sklearn.metrics import accuracy_score

''' Data preperation '''

data_dir = 'C:\\Users\\alshu\\Documents\\Hathiq_project\\mydataset'
categories = ['good', 'scrap']

data = []
label = []

for category_ind , category in enumerate(categories): 
    for file in os.listdir(os.path.join(data_dir,category)):
        imgpath = os.path.join(data_dir , category , file)
        img = imread(imgpath)
        img = resize(img, (450,250))
        data.append(img.flatten())
        label.append(category_ind)      
data = np.asarray(data)
label = np.asarray(label)

''' data split and training '''

x_train , x_test , y_train , y_test = train_test_split(data, label, test_size=0.2 , shuffle=True , stratify=label)

classifier = SVC()
parameters = [{'gamma':[0.1, 0.01, 0.001], 'C' : [1, 10, 100, 1000] }]

GSearch = GridSearchCV(classifier, parameters)
GSearch.fit(x_train, y_train)

''' model performance '''

best_model = GSearch.best_estimator_

y_pred = best_model.predict(x_test)

score = accuracy_score(y_pred, y_test)
print('{}% of the samples were correct'.format(str(score*100)))

''' save the model '''
pickle.dump(best_model, open('.\Hathiq_model.p','wb'))