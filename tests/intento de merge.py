import json
def merge(**dic):
    me,mm,mh=0,0,0
    #load dic
    m=[dic['eas'][0],dic['mid'][0],dic['har'][0]]
    for i in range(8):
        maximo=max(m)
        if(maximo==dic['eas'][me]):
            me+=1
            m.append(dic['eas'][me])

        elif(maximo==dic['mid'][mm]):
            mm+=1
            m.append(dic['mid'][mm])
        
        elif(maximo==dic['har'][mh]):
            mh+=1
            m.append(dic['har'][mh])
            #excepcion out of range => append 0
        elif(maximo==0):
            print(i+1,': ---')
            continue
        print(i+1,': ',maximo)

        m.remove(maximo)


merge(eas=[[10],[9],[3],[0]],mid=[[5],[4],[1]],har=[[8],[7],[6],[2]])