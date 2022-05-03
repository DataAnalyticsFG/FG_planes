import streamlit as st


def Calculo_EN(meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif):
    global mult
    incentivos = 0
    mult = 0

    try:

        if((meses == 0) or (md_t < md_n) or ((d_n > 0) and (md_n == 0))):
            st.warning("Verifique los valores ingresados")

        if(meses >= 4 or ((meses == 1) & (md_t >= 200000) & (d_n >= 6) & (md_n >= 125000)) or ((meses == 2) & (md_t >= 200000) & (d_n >= 6) & (md_n >= 125000)) or ((meses == 3) & (md_t >= 200000) & (d_n >= 6) & (md_n > 125000))):

            if(md_t < 200000 or d_n < 6):
                mult = 0
            elif((md_t >= 200000) & ((d_n >= 6) & (d_n <= 9)) & (md_n < 125000)):
                mult = 8
            elif((md_t >= 200000) & ((d_n >= 6) & (d_n <= 9)) & (md_n >= 125000)):
                mult = 12
            elif((md_t >= 200000) & ((d_n >= 10) & (d_n <= 14)) & (md_n < 250000)):
                mult = 12
            elif((md_t >= 200000) & ((d_n >= 10) & (d_n <= 14)) & (md_n >= 250000)):
                mult = 15
            elif((md_t >= 200000) & (d_n >= 15) & (md_n < 375000)):
                mult = 15
            elif((md_t >= 200000) & (d_n >= 15) & (md_n >= 375000)):
                mult = 20

        elif((meses <= 3) or (((md_t < 200000) & (d_n < 6)) or ((md_t >= 200000) & (d_n < 6)))):

            if(meses == 1):
                if(md_n < 125000):
                    mult = 0
                elif(md_n >= 125000):
                    mult = 8

            elif(meses == 2):
                if(md_n < 150000):
                    mult = 0
                elif(md_n >= 150000):
                    mult = 8

            elif(meses == 3):
                if(md_n < 175000):
                    mult = 0
                elif(md_n >= 175000):
                    mult = 8

        print(p1_dif)
        print(p30_dif)

        if((p1_o <= 2) & (p30_o <= 1.5) or ((p1_o == 0) & (p30_o == 0))):
            mult = mult

        elif(((p1_o > 2) & (p1_dif <= 0)) & (p30_o <= 1.5)):
            mult = mult

        elif((p30_o > 1.5) & (p1_o >= 0)):
            mult = mult*0.5

        elif(((p1_o > 2) & (p1_dif > 0)) & (p30_o >= 0)):
            mult = mult*0.5

        elif(mult == 0):
            mult = 0

        incentivos = (md_t/1000)*mult

    except:
        #st.warning("Verifique los datos ingresados")
        pass
    return incentivos




