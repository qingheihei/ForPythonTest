import os

FB_num= []
FB_str = []
m_base =0
try:
    with open("input.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip().split(":"))==2:
                number, string = line.strip().split(":")
                FB_num.append(int(number))
                FB_str.append(str(string))
            else:
                m_base = int(line)
except ValueError:
    print("value error, stop!")
    os._exit(0)
except IOError:
    print("file IOerror, stop!")
    os._exit(0)
            
result = ""
no_baisu=False
for i in range(len(FB_num)):
    idx = FB_num.index(min(FB_num))
    if m_base % FB_num[idx] ==0:
        no_baisu=True
        result += FB_str[idx]
    FB_num[idx]=max(FB_num)+1
if no_baisu == False:
    result = str(m_base)
print(result)