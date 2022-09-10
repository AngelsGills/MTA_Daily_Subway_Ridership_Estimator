# MTA Daily Subway Ridership Estimator
I. Abstract

The Mass transit Authority of New York City has been sharing its ridership and traffic data online each day during the coronavirus pandemic. Available to download is all the data for all of the agency's transport services. About the subway data: Subway ridership figures are determined from MetroCard and OMNY swipes and taps, and include ridership on the Staten Island Railway. Figures from recent days may be revised as data reconciliation processes are carried out. This project aims to implement the available data provided by the MTA and other data resources to train a artificial neural network to predict the MTA's dailiy subway ridership.

II. Introduction

The MTA has been sharing the ridership and traffic data each day to help you understand how many people are using the services in and around New York City. All of the agency's services are updated to provide an estimated ridership number for each specific date. The data provided for all transit services is compared to a percent of a comparable pre-pandemic day. The project will utilize the available ridership data by the agency and contributing factors that effect overall ridership such as weather, public school session calendar, and holidays. All of the factors chosen have been shown to effect the overall ridership on a daily occasion.

Materials and Methods
The contributing factors that will be used to train the ANN is chosen based on direct correlation to overall ridership and for its ease of availablity. The weather data used will be sourced from the National Centers for Environmental Information website, which allows users to download reported weather conditions for a selected city/region (Central Park/New York City). The public school calendar will also be used as a ridership factor considering in 2021-22, there were 1,058,888 students in the NYC school system, the largest school district in the United States. Lastly, holidays will be taken into account considering the reduced ridership impact of schools being closed and employeer's workday closures.

Data Preprocessing
Upon receiving the MTA's ridership data and the NOAA daily summaries for the NY region data, the data was compiled into a relevant daily summary csv file. The NYC public school academic calendar was used to extract school recess, aswell as holidays were incorporated into the file. The category contributing ridership factors are either represented as a decimal numeral (average wind speed, average temperature, etc.) or a Boolean logic number (weekend, holiday, etc.) inwhich a value of 1 represents meeting the criteria for the category and a value of 0 doesn't meet the criteria.
