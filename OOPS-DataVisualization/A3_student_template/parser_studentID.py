from preprocessData_studentID import cleanlist, preprocessLine, rid_tags

class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()
		self.Vocabularysize = self.getVocabularySize()
		
	def __str__(self):
		print("{};;;{};;;{};;;{};;;".format(self.ID, self.type, self.dateQuarter, self.cleanBody, self.Vocabularysize))		
		
	def getID(self):
		proclist = (self.inputString.split(maxsplit=4))
		ROWID = int(((proclist[1].split("="))[-1])[1:-1])
		return ROWID

	def getPostType(self):
		proclist = self.inputString.split(maxsplit=4)
		POSTID = int(((proclist[2].split("="))[-1])[1])
		if POSTID == 1:
			posttype = "Question"
		if POSTID == 2:
			posttype = "Answer"
		else:
			posttype = "Others"	
		return posttype


	def getDateQuarter(self):
		proclist = self.inputString.split(maxsplit=4)
		DATETIME = ((proclist[3].split("=")[1]))
		calendarList = (DATETIME.split("T")[0]).split("-")
		MONTH =int(calendarList[1])
		if MONTH <= 3 :
			QUARTER = "Q1"
		if MONTH in [3,6] :
			QUARTER = "Q2"
		if MONTH in [6,9]:
			QUARTER = "Q3"
		else:
			QUARTER ="Q4"
		YEAR = (calendarList[0])[1:]
		yearq = YEAR + QUARTER
		return yearq

	def getCleanedBody(self):
		line = rid_tags(preprocessLine(self.inputString))
		line = line[2:-6]
		return line		

	def getVocabularySize(self):
		from string import punctuation
		forbidden =list(punctuation)
		forbidden.append('')
		forbidden.append('\n')
		
		vocabline = self.getCleanedBody()
		vocablist = vocabline.split(" ")
		for elements in vocablist:
			insertindex =vocablist.index(elements)
			vocablist.remove(elements)
			
			for symbols in forbidden:
				if symbols in elements:
					elements = elements.replace(symbols,"")
			vocablist.insert(insertindex,elements)
		#lowercasing and adding to new list
		newlist = []
		for newelements in vocablist:
			newelements = newelements.lower()

			if newelements not in newlist and len(newelements)!=0:
				newlist.append(newelements)
		return(len(newlist))
if __name__ == '__main__':
	reader = open("data.xml","r",encoding="utf-8")
	a=2
	readerdata = reader.readlines()
	while a<len(readerdata):
		readerline = readerdata[a]	
		data = Parser(readerline)
		data.__str__()
		a+=1
		