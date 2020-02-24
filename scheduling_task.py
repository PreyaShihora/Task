import copy
import json
import operator
from datetime import datetime,timedelta
def insert(data_file):
    with open('test.json', 'w') as outfile:
        json.dump(data_file, outfile, indent=4)
        print("Data modified succesfully")




def schedule_task(user,profile,startdate,enddate):
    data={}
    # data_file={}
    temp={}
    for i in range(0,1):
        u1_dict={}
        u1_list=[]
        # user=input("Enter user")
        # profile=input("Enter profile")
        # start_date=input("Enter start date")
        # end_date=input("Enter end date")
        u1_dict["profile"]=profile
        u1_dict["startDate"]=startdate
        u1_dict["endDate"]=enddate
        u1_list.append(u1_dict)
        data.update({user:u1_list})
        sd = (datetime.strptime(u1_dict["startDate"],'%d-%m-%Y').date())
        ed = (datetime.strptime(u1_dict["endDate"], '%d-%m-%Y').date())


    with open('test.json', 'r') as f:
      data_file = json.load(f)

    if sd <= ed:
        if user not in data_file.keys():
            data_file.update(data.items())
            with open('test.json', 'w') as outfile:
                json.dump(data_file, outfile, indent=4)

        else:
            c = -1
            temp_list = copy.deepcopy(data_file[user])
            for i in data_file[user]:
                c += 1

                sd_f = (datetime.strptime(i["startDate"],'%d-%m-%Y').date())
                ed_f = (datetime.strptime(i["endDate"],'%d-%m-%Y').date())
                profile_f=i["profile"]

                if profile_f != profile: #different profile
                    #Case1-3
                    if sd_f < sd and sd_f < ed and ed_f >= sd and ed_f < ed:
                        print("Overlapping Case 1")
                        latest_start = max(sd_f, sd)
                        earliest_end = min(ed_f, ed)
                        delta = (earliest_end - latest_start).days + 1
                        days = timedelta(days=delta)
                        new_date = earliest_end - days
                        ed_f = datetime.strftime(new_date, '%d-%m-%Y')
                        temp_list[c]["endDate"]=ed_f

                    #Case 2
                    elif sd_f == sd and sd_f < ed and ed_f > sd and ed_f > ed:
                        print("Overlapping Case 2")
                        delta = (ed - sd_f).days + 1
                        diff_days = timedelta(days=delta)
                        new_date = sd_f + diff_days
                        sd_f = datetime.strftime(new_date, '%d-%m-%Y')
                        temp_list[c]["startDate"] = sd_f

                    #Case 4
                    elif sd_f < sd and sd_f < ed and ed_f > ed and ed_f > sd:
                      print("Overlapping Case 4")
                      end = ed_f
                      new_date_end = sd - timedelta(days=1)
                      ed_f = datetime.strftime(new_date_end, '%d-%m-%Y')
                      temp_list[c]["endDate"] = ed_f
                      ed_f_new=datetime.strftime(end, '%d-%m-%Y')
                      #new start of second P1
                      new_date_start = ed + timedelta(days=1)
                      sd_f_new=datetime.strftime(new_date_start, '%d-%m-%Y')
                      temp["profile"]=profile_f
                      temp["startDate"]=sd_f_new
                      temp["endDate"]=ed_f_new
                      temp_list.append(temp)

                    #Case6
                    elif sd_f == sd and sd_f < ed and ed_f > sd and ed_f < ed:
                        print("Overlapping Case 6")
                        temp_list.remove(i)
                        c -= 1

                    #Case7
                    elif sd_f > sd and sd_f < ed and ed_f > sd and ed_f < ed:
                        print("Overlapping Case 7")
                        temp_list.remove(i)
                        c -= 1

                    #Case8-13
                    elif sd_f > sd and sd_f <= ed and ed_f >sd and ed_f > ed:
                        print("overlapping Case 8")
                        new_date = ed + timedelta(days=1)
                        sd_f = datetime.strftime(new_date,'%d-%m-%Y')
                        temp_list[c]["startDate"] = sd_f

                    #Case10
                    elif sd_f < sd and sd_f < ed and ed_f > sd and ed_f == ed:
                        print("Overlapping Case 10")
                        new_date = sd - timedelta(days=1)
                        ed_f = datetime.strftime(new_date, '%d-%m-%Y')
                        temp_list[c]["endDate"]=ed_f

                    #Casse11
                    elif sd_f > sd and sd_f < ed and ed_f > sd and ed_f == ed:
                        print("Overlapping Case 11")
                        temp_list.remove(i)
                        c -= 1

                    #Case12
                    elif sd_f == sd and sd_f < ed and ed_f == ed and ed_f > sd:
                        print("Overlapping Case 12")
                        temp_list.remove(i)
                        c -= 1

                    #Case 16
                    elif sd_f == sd and sd_f < ed and ed_f == sd and ed_f < ed:
                        print("Overlapping Case 16")
                        temp_list.remove(i)
                        c -= 1

                    #Case17
                    elif sd_f == sd and sd_f == ed and ed_f > sd and ed_f > ed:
                        print("Overlapping Case 17")
                        new_date = ed + timedelta(days=1)
                        sd_f = datetime.strftime(new_date, '%d-%m-%Y')
                        temp_list[c]["startDate"] = sd_f

                    #Case 18
                    elif sd_f < sd and sd_f < sd and ed_f == ed and ed_f == sd:
                        print("Overlapping Case 18")
                        new_date = ed_f - timedelta(days=1)
                        ed_f = datetime.strftime(new_date, '%d-%m-%Y')
                        temp_list[c]["endDate"] = ed_f

                    # Case 19
                    elif sd_f == sd and sd_f == sd and ed_f == ed and ed_f == sd:
                        print("Overlapping Case 19")
                        temp_list.remove(i)
                        c -= 1

                    elif ed < sd_f:
                        break

                    else:
                        print("No Overlapping")


                else:#same profile
                    #Case 1-3
                    if sd_f < sd and sd_f < ed and ed_f >= sd and ed_f < ed:
                        print("Overlapping Case 1")
                        sd=sd_f
                        u1_dict["startDate"] = datetime.strftime(sd, '%d-%m-%Y')
                        temp_list.remove(i)
                        c-=1

                    # Case 2
                    elif sd_f == sd and sd_f < ed and ed_f > sd and ed_f > ed:
                        print("Overlapping Case 2")
                        ed=ed_f
                        u1_dict["endDate"] = datetime.strftime(ed, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    # Case 4
                    elif sd_f < sd and sd_f < ed and ed_f > ed and ed_f > sd:
                        print("Overlapping Case 4")
                        sd=sd_f
                        ed=ed_f
                        u1_dict["startDate"] = datetime.strftime(sd, '%d-%m-%Y')
                        u1_dict["endDate"] = datetime.strftime(ed, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    #Case6
                    elif sd_f == sd and sd_f < ed and ed_f > sd and ed_f < ed:
                        print("Overlapping Case 6")
                        temp_list.remove(i)
                        c -= 1

                    # Case7
                    elif sd_f > sd and sd_f < ed and ed_f > sd and ed_f < ed:
                        print("Overlapping Case 7")
                        temp_list.remove(i)
                        c -= 1


                    # Case8-13
                    elif sd_f > sd and sd_f <= ed and ed_f > sd and ed_f > ed:
                        print("overlapping Case 8")
                        ed=ed_f
                        u1_dict["endDate"] = datetime.strftime(ed, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    #Case10
                    elif sd_f < sd and sd_f < ed and ed_f > sd and ed_f == ed:
                        print("Overlapping Case 10")
                        sd=sd_f
                        u1_dict["startDate"] = datetime.strftime(sd, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    # Case11
                    elif sd_f > sd and sd_f < ed and ed_f > sd and ed_f == ed:
                        print("Overlapping Case 11")
                        temp_list.remove(i)
                        c -= 1

                    # Case12
                    elif sd_f == sd and sd_f < ed and ed_f == ed and ed_f > sd:
                        print("Overlapping Case 12")
                        temp_list.remove(i)
                        c -= 1

                    # Case 14
                    elif sd_f < sd and sd_f < ed and (sd-ed_f).days==1 and ed_f < sd and ed_f < ed:
                        print("Overlapping case 14")
                        sd=sd_f
                        u1_dict["startDate"] = datetime.strftime(sd, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    # Case 16
                    elif sd_f == sd and sd_f < ed and ed_f == sd and ed_f < ed:
                        print("Overlapping Case 16")
                        temp_list.remove(i)
                        c -= 1

                    # Case17
                    elif sd_f == sd and sd_f == ed and ed_f > sd and ed_f > ed:
                        print("Overlapping Case 17")
                        ed = ed_f
                        u1_dict["endDate"] = datetime.strftime(ed, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    # Case 18
                    elif sd_f < sd and sd_f < sd and ed_f == ed and ed_f == sd:
                        print("Overlapping Case 18")
                        sd = sd_f
                        u1_dict["startDate"] = datetime.strftime(sd, '%d-%m-%Y')
                        temp_list.remove(i)
                        c -= 1

                    elif ed < sd_f:
                        break

                    else:
                        print("No Overlapping")


            data_file[user] = temp_list[:]
            data_file[user].append(u1_dict)
            data_file[user].sort(key=lambda x: datetime.strptime(x['startDate'], '%d-%m-%Y'))
            # data_file[user] = sorted(data_file[user], key=operator.itemgetter("startDate"))
            # print(data_file)
            insert(data_file)
    else:
        print("invalid")

    return(data_file[user])

def result():
    with open('test.json', 'r') as f:
        data_file = json.load(f)
    return (data_file)