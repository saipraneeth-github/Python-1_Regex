def secconvertor(n):
    hr = n/3600
    t= n%3600
    min = t/60
    sec = t%60
    return "0%d:%02d:%02d" %(hr,min,sec)
n= int(input("Enter number of seconds :"))
print(secconvertor(n))