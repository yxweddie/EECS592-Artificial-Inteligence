def scan(f_name):
    # table 1
    D_TRUE  = 0
    D_FALSE = 0


    SB_AND_D_TRUE = 0
    SB_AND_D_FALSE = 0

    PS_TRUE = 0
    PS_FALSE= 0

    PSB_AND_PS_TRUE = 0
    PSB_AND_PS_FALSE = 0

    FC_AND_MB_TRUE = 0
    FC_AND_MB_FALSE = 0

    MB_TRUE = 0
    MB_FALSE =0

    MB_D_TRUE_PS_TRUE = 0
    MB_D_TRUE_PS_FALSE = 0
    MB_D_FALSE_PS_TRUE = 0
    MB_D_FALSE_PS_FALSE =0

    D_TRUE_PS_TRUE = 0
    D_TRUE_PS_FALSE = 0
    D_FALSE_PS_TRUE = 0
    D_FALSE_PS_FALSE = 0

    WC_SB_TRUE_MB_TRUE = 0
    WC_SB_TRUE_MB_FALSE = 0
    WC_SB_FALSE_MB_TRUE = 0
    WC_SB_FALSE_MB_FALSE = 0

    SB_TRUE_MB_TRUE = 0
    SB_TRUE_MB_FALSE = 0
    SB_FALSE_MB_TRUE = 0
    SB_FALSE_MB_FALSE = 0

    WTO_SB_TRUE_PSB_TRUE_MB_TRUE = 0
    WTO_SB_TRUE_PSB_TRUE_MB_FALSE = 0
    WTO_SB_TRUE_PSB_FALSE_MB_TRUE = 0
    WTO_SB_TRUE_PSB_FASLE_MB_FALSE = 0
    WTO_SB_FALSE_PSB_TRUE_MB_TRUE = 0
    WTO_SB_FALSE_PSB_TRUE_MB_FALSE = 0
    WTO_SB_FALSE_PSB_FALSE_MB_TRUE = 0
    WTO_SB_FALSE_PSB_FALSE_MB_FALSE = 0

    SB_TRUE_PSB_TRUE_MB_TRUE = 0
    SB_TRUE_PSB_TRUE_MB_FALSE = 0
    SB_TRUE_PSB_FALSE_MB_TRUE = 0
    SB_TRUE_PSB_FASLE_MB_FALSE = 0
    SB_FALSE_PSB_TRUE_MB_TRUE = 0
    SB_FALSE_PSB_TRUE_MB_FALSE = 0
    SB_FALSE_PSB_FALSE_MB_TRUE = 0
    SB_FALSE_PSB_FALSE_MB_FALSE = 0

    variable = ["D","PS","SB","MB","PSB","WC","WTO","FC"]

    with open(f_name,'rU') as f:
        lines = f.readlines()
        row_num = 0;
        for line in lines:
            row_dic = dict()
            if row_num !=0 :
                count = 0
                for literal in line:
                    if literal != ",":
                        if literal == "T":
                            row_dic[variable[count]] = True
                        elif literal == "F":
                            row_dic[variable[count]] = False
                        count = count + 1

                len(row_dic)
                if row_dic["D"] :
                    D_TRUE = D_TRUE + 1
                else:
                    D_FALSE = D_FALSE + 1

                if row_dic["PS"]:
                    PS_TRUE = PS_TRUE + 1
                else:
                    PS_FALSE = PS_FALSE + 1

                if row_dic["MB"] :
                    MB_TRUE = MB_TRUE + 1
                else :
                    MB_FALSE = MB_FALSE +1

                if row_dic["SB"] and row_dic["D"]:
                    SB_AND_D_TRUE = SB_AND_D_TRUE +1
                if row_dic["SB"] == True and row_dic["D"] == False:
                    SB_AND_D_FALSE = SB_AND_D_FALSE +1

                if row_dic["PSB"] and row_dic["PS"]:
                    PSB_AND_PS_TRUE = PSB_AND_PS_TRUE + 1
                if row_dic["PSB"] and (not row_dic["PS"]):
                    PSB_AND_PS_FALSE = PSB_AND_PS_FALSE +1

                if row_dic["FC"] and row_dic["MB"]:
                    FC_AND_MB_TRUE = FC_AND_MB_TRUE +1
                if row_dic["FC"] and (not row_dic["MB"]):
                    FC_AND_MB_FALSE = FC_AND_MB_FALSE +1

                if row_dic["MB"] and row_dic["D"] and row_dic["PS"]:
                    MB_D_TRUE_PS_TRUE = MB_D_TRUE_PS_TRUE+1
                if row_dic["MB"] and row_dic["D"] and (not row_dic["PS"]):
                    MB_D_TRUE_PS_FALSE = MB_D_TRUE_PS_FALSE+1
                if row_dic["MB"] and (not row_dic["D"]) and row_dic["PS"]:
                    MB_D_FALSE_PS_TRUE = MB_D_FALSE_PS_TRUE+1
                if row_dic["MB"] and (not row_dic["D"]) and (not row_dic["PS"]):
                    MB_D_FALSE_PS_FALSE = MB_D_FALSE_PS_FALSE+1

                if row_dic["D"] and row_dic["PS"]:
                    D_TRUE_PS_TRUE = D_TRUE_PS_TRUE+1
                if row_dic["D"] and (not row_dic["PS"]):
                    D_TRUE_PS_FALSE = D_TRUE_PS_FALSE+1
                if (not row_dic["D"]) and row_dic["PS"]:
                    D_FALSE_PS_TRUE = D_FALSE_PS_TRUE+1
                if (not row_dic["D"]) and (not row_dic["PS"]):
                    D_FALSE_PS_FALSE = D_FALSE_PS_FALSE+1

                if row_dic["WC"] and row_dic["SB"] and row_dic["MB"]:
                    WC_SB_TRUE_MB_TRUE = WC_SB_TRUE_MB_TRUE + 1
                if row_dic["WC"] and row_dic["SB"] and (not row_dic["MB"]):
                    WC_SB_TRUE_MB_FALSE = WC_SB_TRUE_MB_FALSE + 1
                if row_dic["WC"] and (not row_dic["SB"]) and row_dic["MB"]:
                    WC_SB_FALSE_MB_TRUE = WC_SB_FALSE_MB_TRUE + 1
                if row_dic["WC"] and (not row_dic["SB"]) and (not row_dic["MB"]):
                    WC_SB_FALSE_MB_FALSE = WC_SB_FALSE_MB_FALSE + 1

                if row_dic["SB"] and row_dic["MB"]:
                    SB_TRUE_MB_TRUE = SB_TRUE_MB_TRUE + 1
                if row_dic["SB"] and (not row_dic["MB"]):
                    SB_TRUE_MB_FALSE = SB_TRUE_MB_FALSE + 1
                if (not row_dic["SB"]) and row_dic["MB"]:
                    SB_FALSE_MB_TRUE = SB_FALSE_MB_TRUE + 1
                if (not row_dic["SB"]) and (not row_dic["MB"]):
                    SB_FALSE_MB_FALSE = SB_FALSE_MB_FALSE + 1

                if row_dic["WTO"] and row_dic["SB"] and row_dic["PSB"] and row_dic["MB"]:
                    WTO_SB_TRUE_PSB_TRUE_MB_TRUE = WTO_SB_TRUE_PSB_TRUE_MB_TRUE + 1
                if row_dic["WTO"] and row_dic["SB"] and row_dic["PSB"] and not row_dic["MB"]:
                    WTO_SB_TRUE_PSB_TRUE_MB_FALSE = WTO_SB_TRUE_PSB_TRUE_MB_FALSE + 1
                if row_dic["WTO"] and row_dic["SB"] and not row_dic["PSB"] and row_dic["MB"]:
                    WTO_SB_TRUE_PSB_FALSE_MB_TRUE = WTO_SB_TRUE_PSB_FALSE_MB_TRUE + 1
                if row_dic["WTO"] and row_dic["SB"] and not row_dic["PSB"] and not row_dic["MB"]:
                    WTO_SB_TRUE_PSB_FASLE_MB_FALSE = WTO_SB_TRUE_PSB_FASLE_MB_FALSE + 1
                if row_dic["WTO"] and not row_dic["SB"] and row_dic["PSB"] and row_dic["MB"]:
                    WTO_SB_FALSE_PSB_TRUE_MB_TRUE = WTO_SB_FALSE_PSB_TRUE_MB_TRUE + 1
                if row_dic["WTO"] and not row_dic["SB"] and row_dic["PSB"] and not row_dic["MB"]:
                    WTO_SB_FALSE_PSB_TRUE_MB_FALSE = WTO_SB_FALSE_PSB_TRUE_MB_FALSE + 1
                if row_dic["WTO"] and not row_dic["SB"] and not row_dic["PSB"] and row_dic["MB"]:
                    WTO_SB_FALSE_PSB_FALSE_MB_TRUE = WTO_SB_FALSE_PSB_FALSE_MB_TRUE + 1
                if row_dic["WTO"] and not row_dic["SB"] and not row_dic["PSB"] and not row_dic["MB"]:
                    WTO_SB_FALSE_PSB_FALSE_MB_FALSE = WTO_SB_FALSE_PSB_FALSE_MB_FALSE + 1

                if row_dic["SB"] and row_dic["PSB"] and row_dic["MB"]:
                    SB_TRUE_PSB_TRUE_MB_TRUE = SB_TRUE_PSB_TRUE_MB_TRUE + 1
                if row_dic["SB"] and row_dic["PSB"] and not row_dic["MB"]:
                    SB_TRUE_PSB_TRUE_MB_FALSE = SB_TRUE_PSB_TRUE_MB_FALSE + 1
                if row_dic["SB"] and not row_dic["PSB"] and row_dic["MB"]:
                    SB_TRUE_PSB_FALSE_MB_TRUE = SB_TRUE_PSB_FALSE_MB_TRUE + 1
                if row_dic["SB"] and not row_dic["PSB"] and not row_dic["MB"]:
                    SB_TRUE_PSB_FASLE_MB_FALSE = SB_TRUE_PSB_FASLE_MB_FALSE + 1
                if not row_dic["SB"] and row_dic["PSB"] and row_dic["MB"]:
                    SB_FALSE_PSB_TRUE_MB_TRUE = SB_FALSE_PSB_TRUE_MB_TRUE + 1
                if not row_dic["SB"] and row_dic["PSB"] and not row_dic["MB"]:
                    SB_FALSE_PSB_TRUE_MB_FALSE = SB_FALSE_PSB_TRUE_MB_FALSE + 1
                if not row_dic["SB"] and not row_dic["PSB"] and row_dic["MB"]:
                    SB_FALSE_PSB_FALSE_MB_TRUE = SB_FALSE_PSB_FALSE_MB_TRUE + 1
                if not row_dic["SB"] and not row_dic["PSB"] and not row_dic["MB"]:
                    SB_FALSE_PSB_FALSE_MB_FALSE = SB_FALSE_PSB_FALSE_MB_FALSE + 1
            row_num = row_num +1

    print "Dropped is true: " + str(D_TRUE) + " Dropped is false: " + str(D_FALSE) + "\n"
    print "Power surge is true: " + str(PS_TRUE) + " Power surge is false: " + str(PS_FALSE) + "\n"
    print "SB^D: " + str(SB_AND_D_TRUE) + " SB^(-D): " + str(SB_AND_D_FALSE) + "\n"
    print "MB: " + str(MB_TRUE) + " (-MB): " + str(MB_FALSE) + "\n"
    print "FC^MB: " + str(FC_AND_MB_TRUE) + " FC^(-MB): " + str(FC_AND_MB_FALSE) + "\n"
    print "PSB^PS: " + str(PSB_AND_PS_TRUE) + " PSB^(-PS): " + str(PSB_AND_PS_FALSE) + "\n"
    print "D^PS: " + str(D_TRUE_PS_TRUE) + " D^(-PS): " + str(D_TRUE_PS_FALSE) + " (-D)^PS: " + str(D_FALSE_PS_TRUE) + " (-D)^(-PS): " + str(D_FALSE_PS_FALSE) + "\n"
    print "MB^D^PS: " + str(MB_D_TRUE_PS_TRUE) + " MB^D^(-PS): " + str(MB_D_TRUE_PS_FALSE) + " MB^(-D)^PS: " + str(MB_D_FALSE_PS_TRUE) + " MB^(-D)^(-PS): " + str(MB_D_FALSE_PS_FALSE) +"\n"
    print "SB^MB: " + str(SB_TRUE_MB_TRUE) + " SB^(-MB): " + str(SB_TRUE_MB_FALSE) + " (-SB)^MB: " + str(SB_FALSE_MB_TRUE) + " (-SB)^(-MB): " + str(D_FALSE_PS_FALSE) + "\n"
    print "WC^SB^MB: " + str(WC_SB_TRUE_MB_TRUE) + " WC^SB^(-MB): " + str(WC_SB_TRUE_MB_FALSE) + " WC^(-SB)^MB: " + str(WC_SB_FALSE_MB_TRUE) + " WC^(-SB)^(-MB): " + str(MB_D_FALSE_PS_FALSE) +"\n"
    print "WTO^SB^PSB^MB: " + str(WTO_SB_TRUE_PSB_TRUE_MB_TRUE) + " WTO^SB^PSB^(-MB): " +str(WTO_SB_TRUE_PSB_TRUE_MB_FALSE) + " WTO^SB^(-PSB)^MB: " + str(WTO_SB_TRUE_PSB_FALSE_MB_TRUE) + " WTO^SB^(-PSB)^(-MB): " +str(WTO_SB_TRUE_PSB_FASLE_MB_FALSE) + " WTO^(-SB)^(PSB)^MB: " + str(WTO_SB_FALSE_PSB_TRUE_MB_TRUE) + " WTO^(-SB)^(PSB)^(-MB): " +str(WTO_SB_FALSE_PSB_TRUE_MB_FALSE) + " WTO^(-SB)^(-PSB)^MB: " + str(WTO_SB_FALSE_PSB_FALSE_MB_TRUE) + " WTO^(-SB)^(-PSB)^(-MB): " + str(WTO_SB_FALSE_PSB_FALSE_MB_FALSE) + "\n"
    print "SB^PSB^MB: " + str(SB_TRUE_PSB_TRUE_MB_TRUE) + " SB^PSB^(-MB): " + str(SB_TRUE_PSB_TRUE_MB_FALSE) + " SB^(-PSB)^MB: " + str(SB_TRUE_PSB_FALSE_MB_TRUE) + " SB^(-PSB)^(-MB): " + str(SB_TRUE_PSB_FASLE_MB_FALSE) + " (-SB)^(PSB)^MB: " + str(SB_FALSE_PSB_TRUE_MB_TRUE) + " (-SB)^(PSB)^(-MB): " + str(SB_FALSE_PSB_TRUE_MB_FALSE) + " (-SB)^(-PSB)^MB: " + str(SB_FALSE_PSB_FALSE_MB_TRUE) + " (-SB)^(-PSB)^(-MB): " + str(SB_FALSE_PSB_FALSE_MB_FALSE) + "\n"


def main():
    scan("report.txt")

if __name__ == '__main__':
    main()