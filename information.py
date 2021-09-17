def chosing_ports():
    ls1_top10 = [21,22,23,25,80,110,443,445,3389]
    ls2_top20 = [21,22,23,25,80,110,443,445,3389,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    ls3_top50 = [21,22,23,25,80,110,443,445,3389,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,
3389,5060,5666,5900,6001,8000,8008,8080,8443,8888,10000,32768,49152,49154]
    ls4_f200 = range(1,200)
    ls5_f1000 = range(1,1000)

    print ("Select a list of PORTS bellow for your scan: ")
    print ("1 - TOP 10")
    print ("2 - TOP 20")
    print ("3 - TOP 50")
    print ("4 - FIRST 200")
    print ("5 - FIRST 1000")
    choice = input("\n---> ")

    list_of_ports = []

    if (choice == '1'):
        list_of_ports = ls1_top10
        return list_of_ports
    elif (choice == '2'):
        list_of_ports = ls2_top20
        return list_of_ports
    elif (choice == '4'):
        list_of_ports = ls4_f200
        return list_of_ports
    elif (choice == '5'):
        list_of_ports = ls4_f1000
        return list_of_ports
    else:
        list_of_ports = ls3_top50
        return list_of_ports

