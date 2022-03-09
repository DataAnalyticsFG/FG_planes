import streamlit as st

def Calculo_OBC(ci, cf, dt, dn, md_i, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif):
    global mult1, mult2, pen_p1, pen_p30
    incentivos = 0
    mult1 = 0
    mult2 = 0

    try:

        #Incentivos Para clientes iniciales < 300

        if(ci < 300):
            ret_min = 1
            ret_real = cf/ci

        #Multiplicadores Incentivos

            if(ret_real >= ret_min):
                if((dn > 5) & (dt > 15)):
                    mult1 = 12
                elif(dt == 15):
                    mult1 = 6
                elif((dt >= 16) & (dt < 50)):
                    mult1 = 8
                elif (dt > 50):
                    mult1 = 12
            else:
                mult1 = 0

            if((ret_real >= ret_min) & (dt > 15)):
                if(md_i < 200000):
                    mult2 = 8
                elif((md_i >= 200000) & (md_i < 250000)):
                    mult2 = 12
                elif((md_i >= 250000)):
                    mult2 = 15

            else:
                mult2 = 0


        #Incentivos para clientes iniciales >= 300

        elif(ci >= 300):
            ret_min = 0.95
            ret_real = cf/ci

            if((ret_real >= ret_min) & (cf >= 300)):
                if (dn > 5 & dt > 15):
                    mult1 = 12
                elif (dt == 15):
                    mult1 = 6
                elif ((dt >= 16) & (dt < 50)):
                    mult1 = 8
                elif (dt > 50):
                    mult1 = 12
                else:
                    mult1 = 0

                if ((ret_real >= ret_min) & (dt > 15)):
                    if (md_i < 200000):
                        mult2 = 8
                    elif ((md_i >= 200000) & (md_i < 250000)):
                        mult2 = 12
                    elif ((md_i >= 250000)):
                        mult2 = 15

                else:
                    mult2 = 0

        #Penalizaciones Incentivos

        if ((p1_o <= 3) & (p30_o <= 2)):
            pen_p1 = 1
            pen_p30 = 1

        if ((p1_o > 3) & (p1_dif > 0)):
            pen_p1 = 0
        else:
            pen_p1 = 1

        if ((p30_o > 2) & (p30_dif > 0)):
            pen_p30 = 0
        else:
            pen_p30 = 1

        incentivos = ((mult1*cf + mult2*(md_i/1000))/2)*pen_p1 + ((mult1*cf + mult2*(md_i/1000))/2)*pen_p30


    except:
        pass

    return incentivos