
import csv
import math


def split(data, sRatio):
    k=0

    trainlength = int(len(data) * sRatio)
    trainData = []
    testarray= list(data)
    while len(trainData) < trainlength:


        trainData.append(testarray.pop(k))

    return [trainData, testarray]


def loadFiles(fname):
    lofdataset = csv.reader(open(fname, "r"))
    dataoffile = list(lofdataset)
    for i in range(len(dataoffile)):
        dataoffile[i] = [float(y) for y in dataoffile[i]]
    return dataoffile
def Mean(mean):
    return sum(mean) / float(len(mean))
def Stdev(stdev):
    avg = Mean(stdev)
    vary = sum([((x - avg)* (x-avg))for x in stdev]) / float(len(stdev) - 1)
    return math.sqrt(vary)

def Nominalvalue(dataarray):
    arrayoftf = {}
    for i in range(len(dataarray)):
        vct = dataarray[i]
        if (vct[4] not in arrayoftf):
            arrayoftf[vct[4]] = []
        arrayoftf[vct[4]].append(vct)
    return arrayoftf


def labelClass(dataset):
    arrayty = Nominalvalue(dataset)
    preparedataset= {}
    for classlabel, instances in arrayty.items():
        calculateop_dataset = [(Mean(attribute), Stdev(attribute)) for attribute in zip(*instances)]
        calculateop_dataset.pop(-1)

        preparedataset[classlabel] = calculateop_dataset
    return preparedataset

def ClassProb(data, inu):
    prob = {}
    for labelValue,classS in data.items():


        prob[labelValue] = 1
        for i in range(len(classS)):
            mean, stdev = classS[i]
            x = inu[i]
            exp = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
            prob[labelValue] *= (1 / (math.sqrt(2 * math.pi) * stdev)) * exp
    return prob

def getPredictions(data, testSet):
    prediction = []
    for i in range(len(testSet)):
        prob = ClassProb(data, testSet[i])
        bLabel, bProb = "Null", -1
        for labelValue, proba in prob.items():
            if bLabel is "Null" or proba > bProb:
                bProb = proba
                bLabel = labelValue
        result = bLabel
        prediction.append(result)
    return prediction


def Accuracy(testSet, prediction):
    true = 0
    for i in range(len(testSet)):
        if testSet[i][4] == prediction[i]:
            true += 1
    return (true/ float(len(testSet))) * 100.0


fname = 'a.csv'

pos=0
neg=0

dataarray = loadFiles(fname)
sRatio = 0.661
trainingData, testdata = split(dataarray, sRatio)
print(len(dataarray))
print(len(trainingData))
print(len(testdata))

laleledtrainingdata = labelClass(trainingData)

predictions = getPredictions(laleledtrainingdata, testdata)

print( Accuracy(testdata, predictions))



for p in range(len(testdata)):

    if testdata[p][4]==1:
      pos=pos+1
    else:
     neg=neg+1

print(pos/len(testdata))
print (neg/len(testdata))











