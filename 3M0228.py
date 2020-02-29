#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    return sum(data)/len(data)
    #Insert your code here
print(mean(data1))

#Complete the median function to make it return the median of a list of numbers
data2=[1., 2, 5, 10, 20]
def median(data):
    sdata = sorted(data)
    index = (len(data)-1)/2
    return sdata[index]
    #Insert your code here
print(median(data2))


## mode:
def mode(data):
    modecnt = 0
    for i in range(len(data)):
        icount=data.count(data[i])
        if icount>modecnt:
            mode=data[i]
            modecnt=icount
        return mode
data3 = [1, 2, 5, 10, -20, 5, 5]
print(mode(data3))


## variance:
#Complete the variance function to make it return the variance of a list of numbers
data4=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu = mean(data)
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i] - mu)**2)
    sigma2 = mean(ndata)
    return sigma2
    ## retrun mean([(x-mu)**2 for x in data])
print(variance(data4))

#Complete the stddev function to make it return the standard deviation 
#of a list of numbers
from math import sqrt
data6=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)
def variance(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])
def stddev(data):
    #Insert your code here
    return sqrt(varianve(data))
print(stddev(data6))