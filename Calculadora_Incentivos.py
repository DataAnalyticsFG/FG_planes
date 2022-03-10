import streamlit as st
from EN_Calculo import Calculo_EN
from OBC_Calculo import Calculo_OBC
from CC_Calculo import Calculo_CC

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed")
st.sidebar.title("Seleccione un Segmento")
segmento = st.sidebar.selectbox("", ("Ejecutivo de Negocios", "Oficial de Banca Comunal", "Operador de CC"))

st.title("Finca Guatemala")
st.subheader("Análisis de Datos")
st.subheader("Incentivos "+str(segmento))


if(segmento == "Ejecutivo de Negocios"):

    form = st.form("EN")
    with form:
        with st.expander("Tiempo activo en Finca", expanded = True):
            meses = st.number_input("Ingrese tiempo en meses", min_value = 0, max_value =1000, format = "%i", step = 1)

        with st.expander("Monto Desembolsado Total", expanded = True):
            md_t = st.number_input("Ingrese Monto Desembolsado", min_value = 0.00, format = "%.2f")

        with st.expander("# Desembolsos Nuevos", expanded = True):
            d_n = st.number_input("Ingrese # de Desembolsos Nuevos", min_value = 0, format = "%i", step = 1)

        with st.expander("Monto Desembolsado Total (Nuevos)", expanded = True):
            md_n = st.number_input("Ingrese Monto Desembolsado (Nuevos)", min_value = 0.00, format = "%.2f")

        with st.expander("PAR1", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                p1_i = st.number_input("PAR1 Cierre Anterior", min_value=0.00, format="%.2f")
            with col2:
                p1_o = st.number_input("PAR1 Cierre Actual", min_value=0.00, format="%.2f")
            with col3:
                st.write("")
                st.write("")
                st.write("Diferencia entre PAR1 = %s" %str(round(p1_o-p1_i, 2)) +"%")
                p1_dif = p1_o-p1_i

        with st.expander("PAR30", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                p30_i = st.number_input("PAR30% Cierre Anterior", min_value=0.00, format="%.2f")
            with col2:
                p30_o = st.number_input("PAR30% Cierre Actual", min_value=0.00, format="%.2f")
            with col3:
                st.write("")
                st.write("")
                st.write("Diferencia entre PAR30 = %s" %str(round(p30_o-p30_i, 2)) +"%")
                p30_dif = p30_o-p30_i

        #enviar = st.form_submit_button("Calcular Incentivos", on_click = Calculo_EN, args = (meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))
        enviar = form.form_submit_button("Calcular Incentivos", on_click = Calculo_EN, args = (meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))

        if enviar:
            #st.write(Calculo_EN(meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))
            st.title("Total a Incentivar: Q" + str(Calculo_EN(meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif)))

elif(segmento == "Oficial de Banca Comunal"):

    form = st.form("OBC")
    with form:
        with st.expander("Clientes Iniciales", expanded=True):
            ci = st.number_input("Ingrese # de Clientes Iniciales", min_value=0, format="%i", step = 1)

        with st.expander("Clientes Finales", expanded=True):
            cf = st.number_input("Ingrese # de Clientes Finales", min_value=0, format="%i", step = 1)

        with st.expander("# de Desembolsos en el Mes", expanded=True):
            dt = st.number_input("Ingrese # Total de Desembolsos", min_value=0, format="%i", step = 1)

        with st.expander("# de Desembolsos Nuevos en el Mes", expanded=True):
            dn = st.number_input("Ingrese # Total de Desembolsos Nuevos", min_value=0, format="%i", step = 1)

        with st.expander("Monto Desembolsado (Individual)", expanded=True):
            md_i = st.number_input("Ingrese Monto Desembolsado Individual", min_value=0.00, format="%.2f")

        with st.expander("PAR1", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                p1_i = st.number_input("PAR1 Cierre Anterior", min_value=0.00, format="%.2f")
            with col2:
                p1_o = st.number_input("PAR1 Cierre Actual", min_value=0.00, format="%.2f")
            with col3:
                st.write("")
                st.write("")
                st.write("Diferencia entre PAR1 = %s" % str(round(p1_o - p1_i, 2)) + "%")
                p1_dif = p1_o - p1_i

        with st.expander("PAR30", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                p30_i = st.number_input("PAR30% Cierre Anterior", min_value=0.00, format="%.2f")
            with col2:
                p30_o = st.number_input("PAR30% Cierre Actual", min_value=0.00, format="%.2f")
            with col3:
                st.write("")
                st.write("")
                st.write("Diferencia entre PAR30 = %s" % str(round(p30_o - p30_i, 2)) + "%")
                p30_dif = p30_o - p30_i

        # enviar = st.form_submit_button("Calcular Incentivos", on_click = Calculo_EN, args = (meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))
        enviar = form.form_submit_button("Calcular Incentivos", on_click=Calculo_OBC, args=(ci, cf, dt, dn, md_i, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))

        if enviar:
            # st.write(Calculo_EN(meses, md_t, d_n, md_n, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif))
            st.title("Total a Incentivar: Q" + str(Calculo_OBC(ci, cf, dt, dn, md_i, p1_i, p1_o, p1_dif, p30_i, p30_o, p30_dif)))

elif(segmento == "Operador de CC"):

    filas = {}
    datos = {0: 'Meta', 1: 'Recuperado', 2: 'Pagos Completos', 3: 'Meta Clientes', 4: 'Clientes Recup.'}
    j = 0

    with st.expander("Numero de Agencias", expanded=True):
        ag = st.number_input("Ingrese # de Agencias Asignadas", min_value=0, format="%i", step=1)
        cols = st.columns(5)

    form = st.form("CC")

    with form:
        for ix in range(ag):
            for x, jx in enumerate(cols):
                filas["f_%i_%i" %(ix, j)] = jx.number_input("%s %i" %(datos[j], ix), min_value=0.00, format="%.2f")
                j = j + 1

                if(j == 5):
                    j = 0
                else:
                    j = j

        enviar = form.form_submit_button("Calcular Incentivos")

        print(ag)
    if enviar:
        c = Calculo_CC(ag, filas)
        try:
            c = round(c,2)
        except:
            c = c
        print(c)
        st.title("Total a Incentivar: Q "+ str(min(6000.00, round(c,2))))




