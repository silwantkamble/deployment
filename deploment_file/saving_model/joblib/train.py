import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

name=['preg','plas','pres','skin','test','mass','predi','age','class']
dataframe=pd.read_csv(url,names=name)
print(dataframe)

# seprate the independant and target model

array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
# spliting into train and test
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=102)

# model
model=LogisticRegression()
model.fit(x_train,y_train)

accu=model.score(x_test,y_test)
print(accu)

# saving the model
filename="diabeties_84.pkl"
joblib.dump(model,filename)