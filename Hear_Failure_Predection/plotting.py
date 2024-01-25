import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from matplotlib import rcParams
import pickle


#load dataset
data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

#load model
pickle_in = open("76%Accuracy.pickle", "rb")
linear = pickle.load(pickle_in)


def plotHeatMap():
	mask = np.zeros_like(data.corr())
	triangle_indices = np.triu_indices_from(mask)
	mask[triangle_indices] = True


	plt.figure(figsize=(16,10))
	sns.heatmap(data.corr(), mask=mask, annot=True, annot_kws={"size": 14})
	sns.set_style('white')
	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)
	plt.savefig('plots/heatmap.png')


def plotRegAge(age):
	age_coef = 0.005668986892699895
	sns.set(rc={'figure.figsize':(11.7,8.27)})
	sns.lmplot(x='age', y='DEATH_EVENT', data=data, height=7)
	sc_plot = plt.scatter([age], [age * age_coef])
	plt.legend((sc_plot,),
           ('Prediction based on your age only',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)
	plt.tight_layout()
	plt.savefig('plots/agereg.png')
	

def plotRegEjection(ejection_fraction):
	ejection_fraction_coef = -0.00941889062478486 
	sns.set(rc={'figure.figsize':(11.7,8.27)})
	sns.lmplot(x='ejection_fraction', y='DEATH_EVENT', data=data, height=7)
	sc_plot = plt.scatter([ejection_fraction], [ejection_fraction * ejection_fraction_coef])
	plt.legend((sc_plot,),
           ('Event based on your ejection fraction only',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)
	plt.tight_layout()
	plt.savefig('plots/ejectionreg.png')
	return ejection_fraction * ejection_fraction_coef



def plotRegSerum(serum_creatinine):
	serum_creatinine_coef = 0.08289742397591307 
	sns.set(rc={'figure.figsize':(11.7,8.27)})
	sns.lmplot(x='serum_creatinine', y='DEATH_EVENT', data=data, height=7)
	plt.ylim((-0.1, 1.2))
	sc_plot = plt.scatter([serum_creatinine], [serum_creatinine * serum_creatinine_coef])
	plt.legend((sc_plot,),
           ('Event based on your serum creatinine only',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)
	plt.tight_layout()
	plt.savefig('plots/serumreg.png')


def diagnosis(ejection_fraction, platelets, serum_creatinine, serum_sodium):
	diagnosis_list = []
	if ejection_fraction >= 50 and ejection_fraction <= 70:
		diagnosis_list.append('Your Ejection Fraction Level is In The Normal Range')
	elif ejection_fraction < 50:
		diagnosis_list.append('Your Ejection Fraction Level is Below The Normal Range')	
	else:
		diagnosis_list.append('Your Ejection Fraction Level is Above The Normal Range')		

	if platelets >= 140000 and platelets <= 450000:
		diagnosis_list.append('Your Platelets Level is In The Normal Range')
	elif platelets < 140000:
		diagnosis_list.append('Your Platelets Level is Below The Normal Range')
	else:
		diagnosis_list.append('Your Platelets Level is Above The Normal Range')

	if serum_creatinine >= 0.6 and serum_creatinine <= 1.4:
		diagnosis_list.append('Your Serum Creatinine Level is In The Normal Range')
	elif serum_creatinine < 0.6:
		diagnosis_list.append('Your Serum Creatinine Level is Below The Normal Range')
	else:
		diagnosis_list.append('Your Serum Creatinine Level is Above The Normal Range')
	
	if serum_sodium >= 135 and serum_sodium <= 145:	    
		diagnosis_list.append('Your Serum Sodium Level is In The Normal Range')
	elif serum_sodium < 135:
		diagnosis_list.append('Your Serum Sodium Level is In Below Normal Range')
	else:
		diagnosis_list.append('Your Serum Sodium Level is In Above Normal Range')

	return diagnosis_list

	





