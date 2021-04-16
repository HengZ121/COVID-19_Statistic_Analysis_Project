import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import psycopg2
from scipy import stats

from sklearn import svm
from sklearn.covariance import EllipticEnvelope

# Default settings
n_samples = 200
outliers_fraction = 0.25
clusters_separation = [0, 1, 2]

#establishing the connection to database
conn = psycopg2.connect(
   database="CSI4142",
   user='CSI4142',
   password='uOttawa1234!',
   host='lileyao1998.synology.me',
   port= '15432'
)  
cursor = conn.cursor()

### Load dataset
cursor.execute(
'''SELECT m.grocery_pharmacy, m.parks, m.transit_stations, m.retail_recreation, m.residential, m.workplaces,
		CASE s.keyword1
			WHEN 'Protect' THEN 25
			WHEN 'Restrict' THEN 5
			WHEN 'Control' THEN 75
			WHEN 'Stay-at-home' THEN 100
			ELSE 0
			END,
	w.daily_high_temperature, w.daily_low_temperature, 
		CASE c.gender
			WHEN 'M' THEN 1
			ELSE 0
			END, 
	c.age as label
	FROM covid_fact_table f, mobility m, 
		specialmeasures s, weather w, positivecase c
	WHERE f.mobility_key = m.mobility_key AND
		f.special_measures_key = s.special_measures_key AND
		f.weather_key = w.weather_key AND f.case_number = c.case_number''')

# algo & variables to define outliers
classifier =  [("One-Class SVM", svm.OneClassSVM(nu=0.25, kernel="rbf",
                                      gamma=0.1))]
xx, yy = np.meshgrid(np.linspace(-7, 7, 500), np.linspace(-7, 7, 500))
n_inliers = int((1. - outliers_fraction) * n_samples)
n_outliers = int(outliers_fraction * n_samples)
ground_truth = np.ones(n_samples, dtype=int)
ground_truth[-n_outliers:] = 0

### Divide instances into training and testing
training = []
label_of_training = []
testing = []
label_of_testing = []
counter = 0

age_of20 = 0

for record in cursor:
	if record[10] == 20:
		age_of20 = age_of20 + 1
	if (counter % 3 == 0):
		if record[10] >= 60:
			training.append(record[5])
			label_of_training.append(record[10])
		else:
			testing.append(record[5])
			label_of_testing.append(record[10])
	else:
		### age distributing in training class without controlling imbalance: 10s - 21874, 20s - 32157, 30s - 25066, 40s - 22550, 50s - 22945, 60s - 14257
		if record[10] != 20 or age_of20 < 25000:
			training.append(record[5])
			label_of_training.append(record[10])
	counter = counter + 1




# Fit the problem with varying cluster separation
for i, offset in enumerate(clusters_separation):
    X = np.r_['1,2,0' ,training, label_of_training]

    # Fit the model with the One-Class SVM
    n_errors = 0
    plt.figure(figsize=(10, 5))
    for i, (clf_name, clf) in enumerate(classifier):
        # fit the data and tag outliers
        clf.fit(X)
        y_pred = clf.decision_function(X).ravel()
        threshold = stats.scoreatpercentile(y_pred,
                                            100 * outliers_fraction)
        y_pred = y_pred > threshold
        if y_pred != ground_truth:
        	n_errors = n_errors + 1
        # plot the levels lines and the points
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        subplot = plt.subplot(1, 2, i + 1)
        subplot.set_title("Outlier detection")
        subplot.contourf(xx, yy, Z, levels=np.linspace(Z.min(), threshold, 7),
                         cmap=plt.cm.Blues_r)
        a = subplot.contour(xx, yy, Z, levels=[threshold],
                            linewidths=2, colors='red')
        subplot.contourf(xx, yy, Z, levels=[threshold, Z.max()],
                         colors='orange')
        b = subplot.scatter(X[:-n_outliers, 0], X[:-n_outliers, 1], c='white')
        c = subplot.scatter(X[-n_outliers:, 0], X[-n_outliers:, 1], c='black')
        subplot.axis('tight')
        subplot.legend(
            [a.collections[0], b, c],
            ['learned decision function', 'true inliers', 'true outliers'],
            prop=matplotlib.font_manager.FontProperties(size=11))
        subplot.set_xlabel("%d. %s (errors: %d)" % (i + 1, clf_name, n_errors))
        subplot.set_xlim((-7, 7))
        subplot.set_ylim((-7, 7))
    plt.subplots_adjust(0.04, 0.1, 0.96, 0.94, 0.1, 0.26)

plt.show()
