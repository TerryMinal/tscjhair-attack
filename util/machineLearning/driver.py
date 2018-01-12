import csv, machinelearning

def get_data(d):
    data = []
    with open(d) as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            temp = []
            for item in row:
                temp.append(float(item))
            data.append(temp)
            i += 1
    return data

d1 = get_data('ex2data1.csv')
d2 = get_data('ex2data2.csv')

# print "d1\n", d1
# print "d2\n", d2

machinelearning.set_train_set(d1)
machinelearning.populate_parameters()
machinelearning.optimize()
l = machinelearning.predict([45, 85])
print l
