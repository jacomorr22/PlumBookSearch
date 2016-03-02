import os
import  pickle


class Person:
    def __init__(self,json):
        self.idx = json['id']
        self.name = json['name_of_incumbent']
        self.location = json['location']
        self.apptType = json['type_of_appt']
        self.organization = json['org_name']
        self.title = json['title']
        self.payPlan = json['pay_plan']
        self.pay = json['pay']

    def __str__(self):
        return 'ID:\t{}\nName:\t{}\nLoc:\t{}\nAType:\t{}\nOrg:\t{}\nTitle:\t{}\nPPlan:\t{}\nPay:\t{}\n\n'.format(self.idx,self.name,self.location,self.apptType,self.organization,self.title,self.payPlan,self.pay)


##INPUT: name of attribute to create index on i.e 'type_of_appt'
##OUTPUT: Dictionary with key = Unique Value of Indexed attribute and value = [list of IDs that have unique value as their attribute]
def createIndex(indName):
    index = {}

    for i in range(1,8139):

        file = open(os.path.join('PlumBookData',str(i)+'.pb'),'rb')
        data = pickle.load(file)

        ids,col = data['id'],data[indName]

        index.setdefault(col, [])
        
        index[col].append(ids)
        
    new = open(os.path.join('PlumBookData',indName+'.pb'),'wb')
    pickle.dump(index,new)
    new.close()
    
    return index

##INPUT: ID of person to find
##OUTPUT: Dictionary object with all info assciated with ID

def getPersonByID(idx):
    
    file = open(os.path.join('PlumBookData',str(idx)+'.pb'),'rb')
    data = pickle.load(file)
    file.close()
    
    return data

##INPUT: name of attribute to create index on i.e 'type_of_appt'
##OUTPUT: Either return attribute index if its created or creates then returns it

def getIndex(indName):
    try:
        file = open(os.path.join('PlumBookData',indName+'.pb'),'rb')
        data = pickle.load(file)
    except:
        data = createIndex(indName)
        
    return data

##INPUT: name of attribute to create index on i.e 'type_of_appt',name of unique value to search with
##OUTPUT: list of people whos attribute matches the searched term
def searchIndex(indName,search):
    
    index = getIndex(indName)
    
    return [Person(getPersonByID(idx)) for idx in index[search]]

##INPUT: list of choices
##OUTPUT: word representing users choice
def getChoice(choices):
    
    string = ''
    choices = sorted(choices)
    for i in range(len(choices)):
        string += str(i) + ': ' + choices[i] +'\n'

    print(string)
    
    
    while True:
        try:
            choice = int(input('Enter the number corresponding to your choice: '))
            choice1 = choices[choice]
        except:
            print('Please use a number between 1 and {}'.format(str(len(choices)-1)))
        else:
            return choice1
            
##INPUT: none
##OUTPUT: List of people matching search term on selected index       
def chooseIndex():    
    print('Please choose which index you would like to search on')
    index = getChoice(list(getPersonByID(1).keys()))
 

    options = list(getIndex(index).keys())
    print()
    print(index + ' Choices:')
    print('-' *20)
    searchTerm = getChoice(options)
    print (index,searchTerm)
    return searchIndex(index,searchTerm)


people = chooseIndex()
print (len(people))
string = []
searchYN = input('Would You like to search? (Y/N) ')

if searchYN.upper() in ('Y','YES'):

    choices = ['idx','name','location','apptType','organization','title','payPlan','pay']
    choice = getChoice(choices)
    search = input('What term would you like to search for? ')

for per in people:
    #if per.name != 'Vacant' and per.location != 'Washington, DC':
    
    
    if searchYN.upper() in ('Y','YES'):        
        if search.lower() in eval('per.'+choice).lower():
            string.append( str(per))
    else:
        string.append(str(per))
        
print(len(string))
print(''.join(string)) 

