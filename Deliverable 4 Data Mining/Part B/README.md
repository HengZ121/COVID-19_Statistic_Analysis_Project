The goal of data mining in this project, is to predict the age group (under 40 or above 40) of covid-19 cases based on the city mobility info., weather, and measures during the onset dates. 

After applying the 3 different algorithms, I am sure that 
				1. different age groups have different patterns of lives during covid-19 pandemic and 
				2. they have different opinion and reactions toward covid-19.

In order to run programs properly, users need to install scikit module for python: https://scikit-learn.org/stable/install.html


I am also confident there are more information can be revealed by applying different algorithms in this project :D

The output of 3 datamining algorithm on my computer:

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining\Part B>python decision_tree.py
Accuracy Rate:  0.6699201036493198
Precision Rate:  0.736649467503749
Recall Rate:  0.8547497566874097
Model Construction Time:  0.20943999290466309  sec

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining\Part B>python random_forest.py
Accuracy Rate:  0.7272805544793146
Precision Rate:  0.7297829521109692
Recall Rate:  0.9946028843601616
Model Construction Time:  1.747328758239746  sec

C:\Users\Heng\Desktop\COVID-19_Statistic_Analysis_Project\Deliverable 4 Data Mining\Part B>python boosting.py
Accuracy Rate:  0.7176584734799483
Precision Rate:  0.7318937469358648
Recall Rate:  0.9686200489574425
Model Construction Time:  43.0341534614563  sec
