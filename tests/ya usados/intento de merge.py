import json


def merge(**dic):
    me, mm, mh = 0, 0, 0
    l = []
    # load dic                                       <------------
    m = [dic['eas'][0], dic['mid'][0], dic['har'][0]]
    for i in range(10):
        maximo = max(m)
        try:
            if(maximo[0] == 0):
                #print(i+1,': ---')
                l.append(str(str(i+1)+': '+'-'))
                continue
            elif(maximo == dic['eas'][me]):
                me += 1
                m.append(dic['eas'][me])

            elif(maximo == dic['mid'][mm]):
                mm += 1
                m.append(dic['mid'][mm])

            elif(maximo == dic['har'][mh]):
                mh += 1
                m.append(dic['har'][mh])

        except IndexError:  # excepcion out of range => append 0
            m.append([0])
        #print(i,': ',maximo)
        l.append(str(str(i)+': '+str(maximo[0])))
        m.remove(maximo)
    return l


l = merge(eas=[[10], [9], [3], [0]], mid=[[5], [4]], har=[[8], [7], [2]])

for dato in l:
    print(dato)
print('lista:', l)
