import pickle
# loading model
model=pickle.load(open("diabeties_84.pkl",'rb'))

result=model.predict([[1,1,1,1,1,1,1,1]])

if result[0]==1:
    print('diabetic')
else:
    print('not diabetic')