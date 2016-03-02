import re,os
import urllib.request
import json
import pickle
file = open('GPO-PLUMBOOK-2012.txt','r').readlines()


for i in range(1,8139):
    url = 'https://m.gpo.gov/wsgpo/plumBook/getPositionDetails?id='+str(i)
    r = urllib.request.urlopen(url).read()
    
    data = json.loads(r.decode('utf-8'))
    if data:
        new = open(os.path.join('PlumBookData',str(i)+'.pb'),'wb')
        pickle.dump(data,new)
        new.close()

    if i%10 == 0:
        print('Done with', i)
