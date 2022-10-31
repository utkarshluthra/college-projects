from pprint import pprint
def rid_tags(mainstr,delim1="<",delim2=">"): #separate function to detect and delete data between two specific points
    while delim1 in mainstr and delim2 in mainstr[mainstr.index(delim1):]:
        index1 = mainstr.index(delim1)
        reststr = mainstr[index1:]
        index2 = index1 + reststr.index(delim2)
        deletestr = mainstr[index1:index2+1]
        mainstr = mainstr.replace(deletestr,"")
    return mainstr

def defile(filename):
	#creates file if it doesnt exist. clears data if it exists
	defi = open(filename,"w",encoding="utf-8")
	defi.writelines("")
	defi.close()
def preprocessLine(inputLine):
	inputLine=inputLine.replace("&amp;","&")  #changes &amp; to &
	inputLine=inputLine.replace("&quot;","\"") #changes &quot; to "
	inputLine=inputLine.replace("&apos;","'")#changes &apos; to '
	inputLine=inputLine.replace("&gt;",">")#changes &gt; to >
	inputLine=inputLine.replace("&lt;","<")#changes &lt; to <
	inputLine=inputLine.replace("&#xA;"," ")#changes &#xA; to <spacebar>
	inputLine=inputLine.replace("&#xD;"," ")#changes &#xD; to <spacebar>
	inputLine=inputLine.replace("row Id","row_id")#changes row Id; to row_id to autosplit properly
	inputLine=inputLine.replace("&amp;","&")#changes &amp; to & 
	
	return inputLine

def splitFile(inputFile, outputFile_question, outputFile_answer):
	defile(outputFile_question) #creating/clearing question output file
	defile(outputFile_answer) #creating/clearing answer output file

	fh = open(inputFile,"r", encoding="utf-8") #inputFile
	filedata = fh.readlines()
	a=5
	while a<len(filedata)-1:
		fileline = filedata[a] #filedata is a list where each line is an element. this selects individual line using loop
		processedfileline = preprocessLine(fileline) #processing line 
		elementList = processedfileline.split(maxsplit=3)	#splitting line into 4 elements, row_id, PostTypeID, CreationDate and Body
		elementList = cleanlist(elementList) #recleans list
		postTypeIDequals = elementList[1] #post type id element
		
		posttypestr = (postTypeIDequals.split("=")) #splits second element
		fileelementer = (posttypestr[1]) #picks number 
				
		PostTypeID = int(fileelementer[-2]) #typecasts number
		elementbody = elementList[3] 
		elementdesc = (elementbody[6:-6])
			
		if PostTypeID == 1:
			
			questioner = open("question.txt","a",encoding="utf-8")
			questioner.writelines(elementdesc)
			questioner.writelines("\n")
		if PostTypeID == 2:
			
			answerer = open("answer.txt","a",encoding="utf-8")
			answerer.writelines(elementdesc)
			answerer.writelines("\n")
		a+=1


def cleanlist(elementList):
	for element in elementList:
		indexer = elementList.index(element)
		elementList.remove(element)
		element = preprocessLine(element)
		element=(rid_tags(element))
		elementList.insert(indexer,element)
	return elementList

if __name__ == "__main__":
	
	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)

