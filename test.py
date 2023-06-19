txt = txt = open('./Question.txt','r')



for i in txt.readlines():
    i = i.rstrip()
    ques = '"'+i+'",'
    with open('Ques.txt','a') as f:
        f.write(ques)
    f.close()
    
