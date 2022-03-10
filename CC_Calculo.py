import streamlit as st

def Calculo_CC(ag, lista):
    try:
        ag = ag
        lista = lista
        cump_ag = 0
        incentivos = 0

        print(ag)
        resultados = []
        penalizaciones = []

        for i in range(ag):
            print(i)
            meta = lista["f_%i_0" %i]
            recuperacion = lista["f_%i_1" %i]
            p_comp = lista["f_%i_2" %i]
            p_parc = recuperacion - p_comp
            meta_c = lista["f_%i_3" %i]
            rec_c = lista["f_%i_4" % i]

            print(meta, recuperacion, p_comp, p_parc, meta_c, rec_c)

            cump_mon = recuperacion/meta
            cump_cli = rec_c/meta_c

            if(cump_mon >= 1):
                i1 = p_comp*0.02 + p_parc*0.01
            elif(cump_mon < 1):
                i1 = 0

            if((cump_cli > 0) & (cump_cli <= 0.3)):
                pen_1 = 0.4
            elif((cump_cli > 0.3) & (cump_cli <= 0.4)):
                pen_1 = 0.6
            elif((cump_cli > 0.4) & (cump_cli <= 0.7)):
                pen_1 = 0.8
            elif(cump_cli > 0.7):
                pen_1 = 1
            else:
                pen_1 = 0

            resultados.append(i1)
            penalizaciones.append(pen_1)


        for i in range(ag):
            print(resultados[i], penalizaciones[i])

        for i in range(ag):
            if(resultados[i] > 0):
                cump_ag = cump_ag +1

        ag_perc = cump_ag/ag

        if((ag_perc > 0) & (ag_perc <= 0.4)):
            pen_2 = 0.2
        elif((ag_perc > 0.4) & (ag_perc <= 0.7)):
            pen_2 = 0.5
        elif((ag_perc > 0.7) & (ag_perc <= 0.9)):
            pen_2 = 0.75
        elif(ag_perc > 0.9):
            pen_2 = 1
        elif(ag_perc == 0):
            pen_2 = 0


        for i in range(ag):
            incentivos = incentivos + ((resultados[i]*0.5*penalizaciones[i])+(resultados[i]*0.5*pen_2))

        #print("Total: " + str(incentivos))

    except:
        st.warning("Revise Condiciones")

    return float(incentivos)




