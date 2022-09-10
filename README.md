# MTA Daily Subway Ridership Estimator 

I. Abstract 

The Mass transit Authority of New York City has been sharing its ridership and traffic data online each day during the coronavirus pandemic. Available to download is all the data for all the agency's transport services. About the subway data: Subway ridership figures are determined from MetroCard and OMNY swipes and taps and include ridership on the Staten Island Railway. Figures from recent days may be revised as data reconciliation processes are carried out. This project aims to implement the available data provided by the MTA and other data resources to train an artificial neural network to predict the MTA's daily subway ridership. An ANN is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain. 
  
II. Introduction 

The MTA has been sharing the ridership and traffic data each day to help you understand how many people are using the services in and around New York City. All the agency's services are updated to provide an estimated ridership number for each specific date. The data provided for all transit services is compared to a percent of a comparable pre-pandemic day. The project will utilize the available ridership data by the agency and contributing factors that affect overall ridership such as weather, public school session calendar, and holidays. All the factors chosen are shown to affect the overall ridership on a daily occasion. 

III. Materials and Methods 

The contributing factors that will be used to train the ANN are chosen based on direct correlation to overall ridership and for its ease of availability. The weather data used will be sourced from the National Centers for Environmental Information website, which allows users to download reported weather conditions for a selected city/region (Central Park/New York City). The public-school calendar will also be used as a ridership factor considering in 2021-22, there were 1,058,888 students in the NYC school system, the largest school district in the United States. Lastly, holidays will be considered for the reduced ridership impact of schools being closed and employer's workday closures. 

Data Preprocessing 

Upon receiving the MTA's ridership data and the NOAA (National Oceanic and Atmospheric) daily summaries for the NY region data, the data was compiled into a relevant daily summary csv file. The NYC public school academic calendar was used to extract school recess, as well as holidays were incorporated into the file. The category contributing ridership factors are either represented as a decimal numeral (average wind speed, average temperature, etc.) or a Boolean logic number (weekend, holiday, etc.) in which a value of 1 represents meeting the criteria for the category and a value of 0 does not meet the criteria. 
 
Artificial Neural Network Model  

A sequential model consisting of a linear stack of layers in Keras will be used for the program. Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. The script allows the user to train a new ANN model or load an existing model. By selecting to train a model, the appropriate data file is read, and the inputs and output are selected for the model. The model can be configured to have the appropriate desired number of neurons per hidden layer, as well as the desired number of hidden layers. The model's activation function is responsible for transforming the summed weighted input from the node into the activation of the node or output for that input. 

The piecewise linear function/rectified linear activation function (Relu) is chosen for the model, ensuring to output the input directly if it is positive, otherwise, it will output zero. The model consists of a arbitrary configuration consisting of two hidden layers with four neurons and three neurons respectfully. The first hidden layer has a input shade consisting of ten inputs, while the second hidden layer has three neurons, both consisting of a Relu activation function. The output layer has a linear activation function, also known as "no activation," or "identity function" (multiplied x1. 0), is where the activation is proportional to the input. Optimizer that implements the Adam algorithm. 

Compiling the model, the optimizer implements the Adam algorithm and computes the mean of squares of error between labels and predictions. Adam optimization is a stochastic gradient descent method that is based on adaptive estimation of first order and second-order moments. The purpose of loss functions is to compute the quantity that a model should seek to minimize during training. Mean squared error is calculated as the average of the squared differences between the predicted and actual values. The squaring means that larger mistakes result in more errors than smaller mistakes, meaning that the model is punished for making larger mistakes. Lastly, the epoch for the model is arbitrary chosen at a value of 2000 iterations. 

IV. Results 
  
Once the ANN model has been trained, four predictions were made which consisted of two weekdays in the immediate future and two weekend days in the immediate past to test the accuracy of the model.   

Weekday in the immediate future (September 1 & September 2):   

Sep. 1 

![3](https://user-images.githubusercontent.com/112568703/189488376-9dff6fc8-55a2-47c0-84e1-4d55d84f0449.png) 

![7](https://user-images.githubusercontent.com/112568703/189488466-ff9686b9-4f80-44db-94ee-e62eedd7cfc6.png) 

![5](https://user-images.githubusercontent.com/112568703/189488408-2b38b628-fbc8-46a5-aaed-38966e6319fd.png)  

Results show a 99% accuracy for the recorded data on Sep. 1.  

Sep. 2 

![9](https://user-images.githubusercontent.com/112568703/189488497-01f542cd-4e47-4e34-9610-8e4bd32d2cdb.png) 

![10](https://user-images.githubusercontent.com/112568703/189488523-5306f5c8-2b67-458f-9f38-ead735ffbfe3.png) 
  
Results show a 99% accuracy for the recorded data on Sep. 2.  

Weekend in the immediate past (August 27 & September 28): 
  
Aug. 27 

![14](https://user-images.githubusercontent.com/112568703/189488608-94448239-f00c-49f4-bfad-91311dc7ebb6.png) 

![15](https://user-images.githubusercontent.com/112568703/189488612-26d03fdf-4542-4d8f-81ab-b840951582b0.png) 
  
Results show a 96% accuracy for the recorded data on Aug. 27. 
  
Aug. 28  

![16](https://user-images.githubusercontent.com/112568703/189488622-a173ba73-a4f7-44e4-845f-ae173f8acd7f.png) 

![17](https://user-images.githubusercontent.com/112568703/189488635-75839776-c16f-4936-ac9c-7cad86f478f5.png) 

Results show a 90% accuracy for the recorded data on Aug. 28.   

Discussion  

Numerically, the model was a greater accuracy when estimating daily weekday ridership. The model was consistent in weekday accuracy vs. weekend accuracy in both the immediate future and past. This project focused on subway ridership, however the data used in the model can also be used to estimate bus ridership and other transport services provided by the MTA. 

Potential Issues 

1. Bias 

The data used to train the model does not consider many biases that have also been shown to affect transit ridership and or momentum/trends in the data.  

Example 1: Consider a holiday falling in the middle of a week and the effects it may have on ridership versus a holiday falling at the start or end of a weekend. The data presented into the model will fail to distinguish the relationship/bias of a holiday to ridership. 

Example 2: Consider the end/return of the school year, where the momentum of ridership will increase/decrease appropriately. The data presented to the model will fail to accurately estimate ridership based on solely previous data. 

2. Lack of data 

The model's training data set includes widely available metrics provided by the MTA, NOAA, & DOE (Department of Education). Other forms of data that have shown to influence ridership can be implemented to build a more accurate model such as employment in the local area, crime/safety statistics, traffic statistics, population trends, and much more. 

Closing thoughts 

In conclusion, this project was made possible by the availability of public data provided. The project allowed me to undergo the process of reaching a unique project statement by gathering data, training a model, and considering the biases and improvement of the program.  

  

  

 

 
