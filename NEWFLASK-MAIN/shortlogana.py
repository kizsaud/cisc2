from numpy import short
from tabulate import tabulate
from finderror import geterror
import re
class bb2:
    def hater():
        prevline=""
        shortreason=[]
        lastme=[]
        lastmeiter=0
        counter=0
        errorcheck=open('shortenedlog.txt','r')
        errorcheker=errorcheck.read()
        aa=open('resultlog.txt','w+')
        with open('shortenedlog.txt','r+') as f:
            for line in f:
                if "Caught an exception"in line:
                    print("hi"+prevline)
                    
                    shortreason.insert(counter,prevline)
                    nextline=next(f)
                    aa.write(line)
                    counter+=1
                    while("AETEST-3-ERROR") in nextline:
                        nextline=next(f)
                        aa.write(nextline)
                        if "AETEST-6" in nextline:
                            nextline=next(f)
                            aa.write(nextline)
                            
                        
                       
                            
                        if "result of testcase" in nextline:
                            
                    
                            nextline=next(f)
                    aa.write("\n")
                    aa.write("++++++++++++++++++++++++++++++++++++++\n")
                prevline=line
            
                        
                            
                        
            aa.close()
        with open('resultlog.txt','r') as log:
            f=log.read()
        ShortenTextAeTestInfo='.%AETEST-6-INFO.+|.%AETEST-3-ERROR.+|%GENIE-6-INFO:.+pyATS.+'
        ShortenListOfText=re.findall(ShortenTextAeTestInfo,f)
        shortenlogpart2=']:.+'
        prevline2=''
        xeneth=0
        errorfilefind=open('results.txt')
        errorfileread=errorfilefind.read()
        ERRORED_FROM='ERRORED FROM:.:.The result of section(.*).is.+.ERRORED'
        ERRORED_FROM_FINDER=re.findall(ERRORED_FROM,errorfileread)
        
        shortlog=open('resultlog.txt','w+')
        for x in range(len(ShortenListOfText)):
            shortlog.write(ShortenListOfText[x])
            shortlog.write("\n")
        shortlog.close()
        with open('resultlog.txt','r') as log2:
            z=log2.read()
        shortenlistoftextpart2=re.findall(shortenlogpart2,z)
        print(shortenlistoftextpart2)
        results=open('newresultlog.txt','w')
        for x in range(len(shortenlistoftextpart2)):
            results.write(shortenlistoftextpart2[x])
            results.write("\n")
        results.close()
        start = ".Caught.an.exception.+"
        end =".The result of.section.+"
        wordx='.The.result.*section (.*) is'
        logfile=open('newresultlog.txt','r')
        line=logfile.read()
        count=0
        blockedcounter=0
        testcasecounter=0
        testcasecounter=0
        erroredcount=0
        caughtcalc=0
       
        with open('shortenedlog.txt') as ERRORLOOKFILE:
            for lines in ERRORLOOKFILE:
                if 'Starting testcase' in lines:
                    testcasecounter+=1
                if 'Caught an exception while executing section' in lines:
                    caughtcalc+=1
                    
                if 'result of testcase 'in lines:
                    if 'ERRORED' in lines:
                        erroredcount+=1
                    if 'BLOCKED' in lines:
                        blockedcounter+=1
                
        
        if testcasecounter>=1 and erroredcount>=1 and caughtcalc>0:
            m = re.compile(r'%s.*?%s' % (start,end), re.S)

            read=m.search(line).group(0)
            file=open('newnew.txt','w')
            file.write(read)
            list3=re.findall(wordx,read)
            kk=0
            zz=0
            file.close()
            with open('newnew.txt','r+') as data_log:
                with open('newnew2.txt','w+')as outfile:
                    for line in data_log:
                        if "Caught an exception" in line:
                            print("HI")
                            outfile.write("Monster start"+str(kk))
                            outfile.write("\n")
                            kk+=1
                        
                        if "The result of testcase" in line or "The result of section"   in line:
                            zz+=1
                        else:
                            outfile.write(line)
            list=[]
            iter=0
            lineiter=0
            with open('newnew2.txt','r') as finallog:
                if"Monster"+str(iter) in line:
                    list.insert(lineiter,line)
                    iter+=1
            filefile=open('newnew2.txt','r')
            ff=filefile.read()
            nana=ff.split('Monster start')
            print("IFFAFDFDSFSADFDSFASDFDS+++++++++++++++++++++++++++DSFSDFSAF++++++++++++")
            #print(read)
            print("here")
            print(nana[0])
            yer=0
            newerrored=[]
            newiter=0
            x=0
            harami=open('harami2.txt','w+')
            while("") in nana:
                nana.remove("")
            for x in range(len(nana)):
                for y in range(len(ERRORED_FROM_FINDER)):
                    if "Caught an exception while executing section"+ ERRORED_FROM_FINDER[y]  in nana[x]:
                        print(ERRORED_FROM_FINDER[y])
                        print(x)
                        
                        #ERRORED_FROM_FINDER.pop()
                        
                        break
            for y in range(len(ERRORED_FROM_FINDER)):
                harami.write(nana[y])
                harami.write("\n")
            harami.close()
            for x in range(len(nana)):
                if 'Error:' in nana[x]:
                    print("hiss")
            print("now+++++++++++")
            with open('harami2.txt','r')as haramilog:
                namaste=haramilog.read()
            shortthisboy='Exception:.+'
            heythismightbeit1=re.findall(shortthisboy,namaste)
            shortthisboy2=':.[Error].+:.+.'
            heythismightbeit2=re.findall(shortthisboy2,namaste)
            if (len(heythismightbeit2))==0:
                heythismightbeit2=re.findall('Error:.+',namaste)
            heytheman=heythismightbeit1+heythismightbeit2
            #print(heythismightbeit)
            print(len(nana))
            actualfile=open('actually.txt','w')
            for x in range (len(shortreason)):
                actualfile.write(shortreason[x])
                actualfile.write("\n")
            actualfile.close()
            with open('actually.txt','r') as log:
                f=log.read()
            ShortenTextAeTestInfo='.%AETEST-6-INFO.+|'
            ShortenTextAetError='.%SCRIPT-3-ERROR.+|.%AETEST-3-ERROR..+|.NONE'
            ShortenListOfText=re.findall(ShortenTextAetError,f)
            shortenlogpart2=']:.+'
        #print(ShortenListOfText)
            shortenlistoftextpart2=re.findall(shortenlogpart2,f)
            #print(shortenlistoftextpart2)
            

            #with open('erroredtexts.txt','r') as log22:
             #   f=log22.read()
            #if (len(ERRORED_FROM_FINDER))<len(heythismightbeit2):
             #   heythismightbeit2.pop()
            manfuers=open('boyss.txt','w')
            for x in range(len(nana)):
                manfuers.write(nana[x])
                manfuers.write("++++++++++++++++++++++++++++++++++++++++++++++++++")
                
                with open('boyss.txt','r') as logfile:
                    word=logfile.read()
                    shorttextthis=re.findall(shortthisboy2,word)
                    outfile=open('tiredofthis.txt','w')
                    for x in range(len(shorttextthis)):
                        outfile.write(shorttextthis[x])
                        outfile.write('\n')
                        outfile.write("++++++++++++++++++++")
                        outfile.write("\n")
                    print(shorttextthis)
                    
                                  
                
            return heythismightbeit2,nana
        else:
            return None
            
                
