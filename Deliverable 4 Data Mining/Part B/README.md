The goal of data mining in this project, is to predict the age group (under 40 or above 40) of covid-19 cases based on the city mobility info., weather, and measures during the onset dates. 

After applying the 3 different algorithms, I am sure that 
				1. different age groups have different patterns of lives during covid-19 pandemic and 
				2. they have different opinion and reactions toward covid-19.

In order to run programs properly, users need to install scikit module for python: https://scikit-learn.org/stable/install.html


I am also confident there are more information can be revealed by applying different algorithms in this project :D

The output of 3 datamining algorithm on my computer:

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining>python decision_tree.py
Accuracy Rate:  0.6915600038494851
Precision Rate:  0.8203834817223252
Recall Rate:  0.7962367652697083
Model Construction Time:  0.2124323844909668  sec

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining>python random_forest.py
Accuracy Rate:  0.8120729477432393
Precision Rate:  0.8158863119159444
Recall Rate:  0.993924558350783
Model Construction Time:  1.888056993484497  sec

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining>python boosting.py
Accuracy Rate:  0.7837311134635743
Precision Rate:  0.8173620663304295
Recall Rate:  0.9463532603887103
Model Construction Time:  46.21404552459717  sec