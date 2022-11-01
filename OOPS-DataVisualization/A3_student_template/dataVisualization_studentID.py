import numpy as np
import matplotlib.pyplot as plt
from parser_studentID import Parser

def visualizeWordDistribution(inputFile, outputImage):
	read = open(inputFile,"r",encoding="utf-8")
	data = read.readlines()
	voclist, vclist0to10 ,vclist10to20 ,vclist20to30 ,vclist30to40 ,vclist40to50,vclist50to60 ,vclist60to70 ,vclist70to80 ,vclist80to90 ,vclist90to100 ,vclist100andgreater = [],[],[],[],[],[],[],[],[],[],[],[]
	pointer = 2

	while pointer<len(data)-1:
		readerline = data[pointer]	
		dataclassed = Parser(readerline)
		vocsize = dataclassed.Vocabularysize
		voclist.append(vocsize)
		if vocsize in range(0,10):
			vclist0to10.append(vocsize)
		if vocsize in range(10,20):
			vclist10to20.append(vocsize)
		if vocsize in range(20,30):
			vclist20to30.append(vocsize)
		if vocsize in range(30,40):
			vclist30to40.append(vocsize)
		if vocsize in range(40,50):
			vclist40to50.append(vocsize)
		if vocsize in range(50,60):
			vclist50to60.append(vocsize)
		if vocsize in range(60,70):
			vclist60to70.append(vocsize)
		if vocsize in range(70,80):
			vclist70to80.append(vocsize)
		if vocsize in range(80,90):
			vclist80to90.append(vocsize)
		if vocsize in range(90,100):
			vclist90to100.append(vocsize)
		else:
			vclist100andgreater.append(vocsize)
		pointer+=1
	n010,n1020,n2030,n3040,n4050,n5060,n6070,n7080,n8090,n90100,n100p = len(vclist0to10),len(vclist10to20),len(vclist20to30),len(vclist30to40),len(vclist40to50),len(vclist50to60),len(vclist60to70),len(vclist70to80),len(vclist80to90),len(vclist90to100),len(vclist100andgreater)
	yax = [n010,n1020,n2030,n3040,n4050,n5060,n6070,n7080,n8090,n90100,n100p]
	
	namelist = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100","100+"]
	ypos = np.arange(len(namelist))
	plt.xticks(ypos,namelist)
	
	plt.tick_params(axis = 'both',labelsize=8)
	graph = plt.bar(ypos,yax,facecolor='#f1f1f1',edgecolor='#1f1f1f',)
	plt.bar_label(graph,yax)
	plt.savefig(outputImage, dpi=48)
	plt.cla()
	
	return outputImage 


def visualizePostNumberTrend(inputFile, outputImage):
	def repeat_counter(listvar):
		newlister=[]
		varlister = []
		for i in listvar:
			if i not in newlister:
				newlister.append(i)
		for b in newlister:
			vari = listvar.count(b)
			varlister.append(vari)
		return(newlister,varlister)
	read = open(inputFile,"r",encoding="utf-8")
	data = read.readlines()

	pointer = 2
	qlistm,alistm=[],[]

	while pointer<len(data)-1:
		readerline = data[pointer]	
		dataclassed = Parser(readerline)
		datatype = dataclassed.type

		datatime = dataclassed.dateQuarter
		if datatype == "Question" :
			qlistm.append(datatime)
		if datatype == "Answer":
			alistm.append(datatime)
		pointer+=1
	cleanlist,countlist = [],[]
	cleanlist,countlist = repeat_counter(qlistm)
	yp = np.arange(len(cleanlist))
	plt.xticks(yp,cleanlist)
	plt.plot(yp,countlist,color="red",label="Questions")
	cleanlist,countlist = repeat_counter(alistm)
	yp = np.arange(len(cleanlist))
	plt.xticks(yp,cleanlist)
	plt.plot(yp,countlist,color="green",label="Answers")
	plt.tick_params(axis = 'both',labelsize=8)
	plt.legend(loc="upper right",frameon=True)
	plt.savefig(outputImage,dpi=48)
	return outputImage


if __name__ == "__main__":

	f_data = r"A3_student_template\data.xml"
	f_wordDistribution = "vocabularySizeDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
