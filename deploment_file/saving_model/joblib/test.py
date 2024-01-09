import joblib
# loading model
model=joblib.load("diabeties_84.pkl")

result=model.predict([[1,1,1,1,1,1,1,1]])

if result[0]==1:
    print('diabetic')
else:
    print('not diabetic')