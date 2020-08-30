"""
Joanne Kwon
PIC 16
Professor Cai
February 1, 2019
"""

'''
PROBLEM 1
The function myype(v) recognizes integers, floats, strings, and lists.
Lists can only contain integers, while strings include anything that is
not an integer, float or list.
'''
import re #regex library

def mytype(v):
    v=str(v)#returns contents inputted in v
    if re.search(r'\[*[0-9]\]',v): #search for lists with only integers
        output="list"
    elif re.search(r'[0-9]\.[0-9]',v): #search for floats
        output="float"
    elif re.search(r'[0-9]',v): #search for integers
        output="integer"
    else:
        output="string" #search for strings (anything but integer, float, and list)
    return output

#test cases and respective outputs
print mytype(789) #integer
print mytype(309896.1419) #float
print mytype('abcde') #string
print mytype([109,29,3,409]) #list
print mytype(['wow','hi','cool']) #string
print mytype('^&') #string


'''
PROBLEM 2
The function findpdfs(L) takes a list of filenames and returns a list of
names for each pdf file without the extension. The filenames are only
composed of letters and numbers.
'''
import re #regex library

def findpdfs(L):
    pdf_list=[] #empty list
    for doc in L: #for each document listed in L
        if re.findall(r'\.([a-zA-Z0-9]*)',doc)[0]=="pdf": #determine whether the document is a .pdf 
            name=re.findall(r'([a-zA-Z0-9]*)\.',doc) #takes the name of the pdf document
            pdf_list.append(name[0]) #appends pdf names to new list
    return pdf_list

L=["IMG2309.jpg","lecture1.pdf","homework.py"] #test input
print findpdfs(L) #test case


'''
PROBLEM 3
The function findemail(url) takes in a url and returns any email address from
the page, including hidden email addresses. The email addresses can have any 
number of dots after the at-sign.
'''
import re #regex library
import urllib2 #url library

def findemail(url):
    d=dict() #dictionary for each email key and value
    email_addresses=[]

    page=urllib2.urlopen(url).read() #reads contents of the url to page
    emails=re.findall(r'([\w]*(@|\sAT\s|\sat\s|\[AT\]|\[at\]).*(\.|\sDOT\s|\sdot\s|\[DOT\]|\[dot\]).?([\w]*))',page) #find content with email format (normal and trick email)
    
    for email in emails: #for every email that was found within the url
        d[email[0]]=0 #sets values to 0 (emailaddress:0)
    for obj in d: #for every object in the dictionary
        email_addresses.append(obj) #appends all keys (email addresses) in email_addresses list to be returned
    return email_addresses

url="file:///Users/joannekwon/Desktop/test.html" #case input
print findemail(url) #test case

"""
##HTML CODE FOR test.html file used in url case input
<h1>Test Emails</h1>
<p>hqcai@math.ucla.org<br>
hqcai AT math DOT ucla DOT com<br>
hqcai at math dot ucla DOT edu<br>
hqcai[AT]ucla[DOT]com<br>
hqcai[at]ucla[dot]edu</p>
"""


'''
PROBLEM 4
The function happiness(text) rates the happiness level of a piece of inputted
text. The happiness score is then determined by averaging the score for all
the words and dividing it by the number of words in the text that are from 
the happiness dictionary.
'''
import re #regex library

def happiness(text):
    count=0 #keep track of how many words are from the happiness dictionary
    happy_word=0 #keep track of value of happy words
    
    dictionary=open("happiness_dictionary.py","r").read() #opens and reads contents of the happiness dictionary
    exec(dictionary,globals()) #dynamically executes dictionary in terms of global variables
    
    text=re.findall(r'[A-Za-z]*',text) #extracts words from inputted text

    for word in text: #for every word in the inputted text
        if word.lower() in happiness_dictionary: #if the word (in lowercase) is in the happiness dictionary
            happy_word+=happiness_dictionary[word.lower()] #adds happiness values to happy_word
            count+=1 #increment by 1 each time there's a happy word
            total_happiness=happy_word/count #divide the total happiness value with the amount of happy words to get the average happiness score
    return total_happiness
        
text="Smiling is correlated with $%23$ Happiness. It can 'uplift' someones mood within just a second!" #case input
print happiness(text) #test case

    