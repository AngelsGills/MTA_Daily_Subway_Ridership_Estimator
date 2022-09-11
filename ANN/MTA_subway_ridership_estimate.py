import numpy as np
import pandas as pd
import time
from tensorflow import keras

# import print_weights as pw
# call: pw.print_weights()

def print_weights(weights):
    # weights = model.get_weights();
    print('\n******* WEIGHTS OF ANN *******\n') 
    for i in range(int(len(weights)/2)):
        print('Weights W%d:\n' %(i), weights[i*2])
        print('Bias b%d:\n' %(i), weights[(i*2)+1])
#END print_weights()

#%% ANN TRAINING
print('\n')
print('**********************************************************')     
print('****  WELCOME TO NYC MTA RIDERSHIP SERVICE ****')
print('**********************************************************')

# prompt user to train or load an ANN model
option_list = ['1','2']
option = ''
while option not in option_list:  
    print('\nOPTIONS:')
    print('1 - Train a new ANN model')
    print('2 - Load an existing model')
    
    option = input('\nSelect an option by entering a number: \n')
    if option not in option_list:
        message = 'Invalid input: Input must be one of the following - '
        print(message, option_list)
        time.sleep(2)
        
if option == '1':
    ## OPTION 1: TRAIN A NEW ANN MODEL
    train_data_file = 'MTA_Daily_Ridership_Data__Beginning_2022.csv'
    
    print('\n********* NOW TRAINING ANN USING', train_data_file,'*********')
    time.sleep(3)
    
    ## load the training data
    df = pd.read_csv(train_data_file)
   
    ## define input matrix X (get rid of columns not needed for model)
    X = np.array(df.drop(['Date','Subways_Total_Estimated_Ridership','Subways_%_of_Comparable_Pre-Pandemic_Day','Buses_Total_Estimated_Ridership','Buses_%_of_Comparable_Pre-Pandemic_Day','STATION','TMAX','TMIN'],axis=1))
    ## Alternative method using TMAX & TMIN instead of TAVG
    #X = np.array(df.drop(['Date','Subways_Total_Estimated_Ridership','Subways_%_of_Comparable_Pre-Pandemic_Day','Buses_Total_Estimated_Ridership','Buses_%_of_Comparable_Pre-Pandemic_Day','STATION','TAVG'],axis=1))
    ## define expected output matrix Y
    Y = np.array(df['Subways_Total_Estimated_Ridership'])
    
    ## create a model for the ANN
    model=keras.Sequential()
    ## add a hidden layer that accepts input features
    ## Dense means every neuron in the layer connects to every neuron in the previous layer.
    model.add(keras.layers.Dense(4,activation='relu',input_shape=(10,)))
    ## add additional hidden layers (if any) here:
    model.add(keras.layers.Dense(3,activation='relu'))
    ## Alternative method using 1 additional hidden layer
    ## model.add(keras.layers.Dense(3,activation='relu'))
    ## add an output layer with a single output (Subways_Total_Estimated_Ridership)
    model.add(keras.layers.Dense(1,activation='linear'))
    ## set the optimization algorithm used for minimizing loss function
    ## use gradient descent (adam) to minimize error (loss)
    model.compile(optimizer='adam',loss='mean_squared_error')
    ## train the ANN model using 2000 iterations
    model.fit(X,Y,epochs=2000)
    print('\n\n********** ANN training complete **********\n\n')    
elif option == '2':
    ## OPTION 2: LOAD ANN MODEL FROM FILE
    
    message = 'Enter the file name of the ANN Model you want to load: \n'
    load_file = input(message)
    #load_file = input('It must be a .h5 file')
    
    ## if file name does not end with '.h5', add '.h5' to the file name
    if load_file[-3:] != '.h5':
        load_file += '.h5'
    ## load the ANN model from load_file
    model = keras.models.load_model(load_file)
    
    print('\n\n****** SUCCESSFULLY LOADED ANN MODEL FROM', load_file,'******')   
else:
    print('ERROR: INVALID OPTION SELECTED')
    ## raise an exception to terminate the program
    raise ValueError()

weights = model.get_weights();
print_weights(weights)

#%% BIKE SHARING PREDICTION USING ANN
input('\n\n********** Press ENTER to start using the ANN **********\n\n')
finished = False
while not finished:
    ## prompt user for inputs
    is_weekend = input('Is it the weekend? (y/n): \n')
    if is_weekend == 'y':
        is_weekend = input('Is it Saturday? (y/n): \n')
        if is_weekend == 'y':
            is_weekend = 1
        else: 
    ## is_weekend = 1 for Saturday & is_weekend = 2 for Sunday
            is_weekend = 2 
    else:
        is_weekend = 0
    is_school_closed = input('Are public schools closed? (y/n): \n')
    if is_school_closed == 'y':
        is_school_closed = 1
    else:
        is_school_closed = 0
    holiday = input('Is a holiday observed? (y/n): \n')
    if holiday == 'y':
        holiday = 1
    else:
        holiday = 0    
    fog = input('Is there fog? (y/n): \n')
    if fog == 'y':
         fog = 1
    else:
         fog = 0   
    thunder = input('Is there thunder or lighting today? (y/n): \n')
    if thunder == 'y':
         thunder = 1
    else:
         thunder = 0   
    haze = input('Is there haze today? (y/n): \n')
    if haze == 'y':
         haze = 1
    else:
         haze = 0   
    temp_f = float(input('\n\nEnter mean temperature in Fahrenheit: \n'))
    #temp_max = float(input('\n\nEnter high temperature in Fahrenheit: \n'))
    #temp_min = float(input('\n\nEnter low temperature in Fahrenheit: \n'))
    avg_wind_speed = float(input('Enter wind speed: (mph) \n'))
    precipitation = float(input('Enter chance of precipitation: % \n'))
    snowfall = float(input('Enter snowfall: (inches) \n'))
    user_input = np.array([[is_weekend, is_school_closed, holiday, avg_wind_speed, temp_f, snowfall, fog, thunder, haze, precipitation]])
    #user_input = np.array([[is_weekend, is_school_closed, holiday, avg_wind_speed, temp_max, temp_min, snowfall, fog, thunder, haze, precipitation]])
    prediction = model.predict(user_input)
    
    ## restrict prediction to non-negative values
    if prediction < 0:
        prediction = 0;
    else:
        pass

    ## display prediction
    print('\n*****************************************')
    print('ANN Predicted number of MTA daily subway ridership: ', int (prediction))
    print('*****************************************')
    ## ask user if they would like to continue
    choice = ''
    while choice not in ['y','n']:
        choice = input('\n\nWould you like to continue? (y/n): \n')
        if choice == 'y':
            pass
        elif choice == 'n':
            finished = True
        else:
            print("Invalid input: Input must be 'y' or 'n'")
    #END WHILE
#END WHILE

## ask user if they would like to save the ANN model
choice = ''
while choice not in ['y','n']:
    choice = input('\n\nWould you like to save the ANN model? (y/n): \n')
    if choice == 'y':
        save_name = input('\n\nEnter a name for the save file: \n')
        ## if file name does not end with '.h5', add '.h5' to the file name
        if save_name[-3:] != '.h5':
            save_name += '.h5'
        model.save(save_name)
        print('\n\n')
        print('***** ANN MODEL SUCCESSFULLY SAVED AS '+save_name+' *****')
    elif choice == 'n':
        pass
    else:
        print("Invalid input: Input must be 'y' or 'n'")
#END WHILE

