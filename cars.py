import re
import pandas as pd               
import numpy as np
import pickle
import mysql.connector
import sys, json
import numpy

'''
Index(['symboling', 'normalized-losses', 'fuel-type', 'wheel-base', 'length',
       'width', 'height', 'curb-weight', 'engine-size', 'bore', 'stroke',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg'],
      dtype='object')
'''
data = json.loads(sys.argv[1])

parameter1 = float(data['symboling'])
parameter2= float(data['normalized-losses'])
parameter3= float(data['fuel_system'])
parameter4= float(data['wheel-base'])
parameter5 = float(data['length'])
parameter6 = float(data['width'])
parameter7 = float(data['height'])
parameter8 = float(data['curb-weight'])
parameter9 = float(data['engine-size_'])
parameter10 = float(data['bore'])
parameter11 = float(data['stroke'])
parameter12 = float(data['compression-ratio'])
parameter13= float(data['horsepower'])
parameter14 = float(data['peak_rpm'])
parameter15 = float(data['city_mg'])
parameter16 = float(data['highway-mpg'])
parameter = [parameter1,parameter2,parameter3,parameter4,parameter5,parameter6,parameter7,parameter8,parameter9,parameter10,parameter11,parameter12,parameter13,parameter14,parameter15,parameter16]



input_array=np.array(parameter) 


# Loading the model pickle
lm_model_pkl = open("lm_model.pkl", 'rb')

lm_model = pickle.load(lm_model_pkl)


#  Predict on new data

y_pred=lm_model.predict(input_array)

round_ypred = y_pred.astype(int)

result = numpy.array_str(round_ypred)

result_str =  ' '.join(map(str, round_ypred))

print("Predicted Car price:$",result_str.strip("[]"))


