string = '''  <row Id="106" PostTypeId="1" CreationDate="2015-09-10T11:47:03.630" Body="&lt;p&gt;I'm considering building a hobby &lt;a href=&quot;https://en.wikipedia.org/wiki/Acoustic_holography&quot;&gt;acoustic holography&lt;/a&gt; setup. I would need several (at least 12, I think) microphones to do this, but I have a limited budget. Does anyone have recommendations for microphones that are relatively cheap but still good enough to get decent resolution?&lt;/p&gt;&#xA;" />
'''
from preprocessData_studentID import preprocessLine
def rid_tags(mainstr,delim1="<",delim2=">"):
    while delim1 in mainstr and delim2 in mainstr[mainstr.index(delim1):]:
        index1 = mainstr.index(delim1)
        reststr = mainstr[index1:]
        index2 = index1 + reststr.index(delim2)
        deletestr = mainstr[index1:index2+1]
        mainstr = mainstr.replace(deletestr,"")
    return mainstr
if __name__=='__main__':
    print(rid_tags(preprocessLine(string)))