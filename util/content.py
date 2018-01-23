import json
import apicalling as api
import ml, ml_db
# from time import sleep

parameters = [1,1,1,1,1,1,1]
api.getKey("credentials.txt")

def get_content(parameters, thing):
    result = []
    count = 0
    # if (thing == "music"):
    #     genre = [ml_db.random_val("genre") for i in range(7)]
    #     artist [ml_db.random_val("artist") for i in range(7)]
    #     count = 0
    #     for music in genre:
    #         for singer in artist:
    #             if (predict(parameters, [music, singer]) >= .5):
    #                 count++
    #                 result.append()
    if (thing == "img"):
        numbers = []
        tags = []
        for i in range(10):
            t1 = []
            t2 = []
            for s in range(len(parameters) - 1):
                temp = ml_db.random_val("img")
                t1.append(temp[0])
                t2.append(temp[1])
            numbers.append(t1)
            tags.append(t2)
        for i in range(10):
            if (ml.predict(parameters, numbers[i]) >= .5):
                result.append(tags[i])
                count += 1
            if (count >= 2):
                break
    data = []
    for i in range(5 - len(result)): #assures that we get 5 images
        temp = ml_db.random_val("img")
        print temp
        t = api.getty(temp[1])
        # ap = " ".join(str(x) for x in ap)
        # print "ap: ", ap
        data.append(t)
        # sleep(1)
    for i in range(len(result)):
        t = api.getty(" ".join(str(x) for x in result[i]))
        # ap = " ".join(str(x) for x in ap)
        # print "ap:", ap
        data.append(t)
    print data
    #with open('j.json', 'w') as jf:
    #    json.dump(data, jf)
    #print j
    # dwrap = {'data':data}
    j = json.dumps(data)
    print j
    l = json.loads(j)
    print l
    return j
    # x = [ml_db.random_val() for i in range(5)] # do this for each db
    # predict(parameters, x) # i think i need to create a db for images, genre, and artists, might as well do
    # features while im at it

get_content("img", parameters)
