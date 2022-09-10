# MTA Daily Subway Ridership Estimator
I. Abstract

The Mass transit Authority of New York City has been sharing its ridership and traffic data online each day during the coronavirus pandemic. Available to download is all the data for all of the agency's transport services. About the subway data: Subway ridership figures are determined from MetroCard and OMNY swipes and taps, and include ridership on the Staten Island Railway. Figures from recent days may be revised as data reconciliation processes are carried out. This project aims to implement the available data provided by the MTA and other data resources to train a artificial neural network to predict the MTA's dailiy subway ridership. An ANN is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain.

II. Introduction

The MTA has been sharing the ridership and traffic data each day to help you understand how many people are using the services in and around New York City. All of the agency's services are updated to provide an estimated ridership number for each specific date. The data provided for all transit services is compared to a percent of a comparable pre-pandemic day. The project will utilize the available ridership data by the agency and contributing factors that effect overall ridership such as weather, public school session calendar, and holidays. All of the factors chosen have been shown to effect the overall ridership on a daily occasion.

III. Materials and Methods

The contributing factors that will be used to train the ANN is chosen based on direct correlation to overall ridership and for its ease of availablity. The weather data used will be sourced from the National Centers for Environmental Information website, which allows users to download reported weather conditions for a selected city/region (Central Park/New York City). The public school calendar will also be used as a ridership factor considering in 2021-22, there were 1,058,888 students in the NYC school system, the largest school district in the United States. Lastly, holidays will be taken into account considering the reduced ridership impact of schools being closed and employeer's workday closures.

Data Preprocessing

Upon receiving the MTA's ridership data and the NOAA daily summaries for the NY region data, the data was compiled into a relevant daily summary csv file. The NYC public school academic calendar was used to extract school recess, aswell as holidays were incorporated into the file. The category contributing ridership factors are either represented as a decimal numeral (average wind speed, average temperature, etc.) or a Boolean logic number (weekend, holiday, etc.) inwhich a value of 1 represents meeting the criteria for the category and a value of 0 doesn't meet the criteria.

Artifical Neural Network Model

A sequential model consisting of a linear stack of layers in Keras will be used for the program. Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow. The script allows the user to train a new ANN model or load an existing model. By selecting to train a model, the appropriate data file is read and the inputs and output is selected for the model. The model can be configured to have the appropriate desired number of neueron per hidden layer, aswell as the desired number of hidden layers. The model's activation function is responsible for transforming the summed weighted input from the node into the activation of the node or output for that input.
The piecewise linear function/rectified linear activation function (relu) is chosen for the model, ensuring to output the input directly if it is positive, otherwise, it will output zero.

The model consist of a arbituary configuration consisting of two hidden layers with four neurons and three neurons respectfully. The first hidden layer has a input shade consisting of the ten inputs, while the second hidden layer has three neurons, both consisting of a relu activation function. The output layer has a  linear activation function, also known as "no activation," or "identity function" (multiplied x1. 0), is where the activation is proportional to the input. Optimizer that implements the Adam algorithm.

Compiling the model, the optimizer implements the Adam algorithm and computes the mean of squares of error between labels and predictions. Adam optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments. The purpose of loss functions is to compute the quantity that a model should seek to minimize during training. Mean squared error is calculated as the average of the squared differences between the predicted and actual values. The squaring means that larger mistakes result in more error than smaller mistakes, meaning that the model is punished for making larger mistakes.
