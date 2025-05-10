#Crear el archivo de la app en el interprete principal (Python)
#######
#Impprtar librerias

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


####################################
#Definir una instancia
@st.cache_resource
####################################

def load_data():
    #Lectura del archivo
    df=pd.read_csv("DataAnalytics.csv")

    ############################################################################################################
    #Calculamos el numero total de la población "n"
    df['tiempo de interacción'].info()
    n=5103

    #Obtenemos el limite superior y el límite inferior de la columna objetivo
    Max=df['tiempo de interacción'].max()
    Min=df['tiempo de interacción'].min()
    Limites= [Min, Max]
    
    #Calculamos el rango R
    R=Max-Min

    #Calculamos el número de Intervalos de Clase "ni", aplicando la regla de Sturges
    ni= 1+3.32*np.log10(n)


    #Calculamos el Ancho del Intervalo "i"
    i=R/ni

    #Categorización de variables
    #Declaramos 2 intervalos (menores de 100) y (mayores de 100)
    #Ajustamos los limites para que todos los valores sean incluidos en los intervalos
    intervalos=np.linspace(-0.1, 165.20, 14)

    #Creamos las categorías 
    categorias= ["0-12.6 seg", "12.7-25.3 seg","25.4-38.1 seg", "38.2-50.7 seg",
                "50.8-63.4 seg", "63.5-76.1 seg","76.2-88.9 seg", "89.0-101.6 seg", 
                "101.7-114.3 seg", "114.4-127.0 seg", "127.1-139.7 seg", "139.8-152.4 seg",
                "152.5-165.3 seg"]

    df['tiempo_interacción']=pd.cut(x= df['tiempo de interacción'], bins=intervalos, labels= categorias)

    ############################################################################################################
    #Obtenemos el limite superior y el límite inferior de la columna objetivo
    Max2=df['tiempo de lección'].max()
    Min2=df['tiempo de lección'].min()
    Limites2= [Min2, Max2]
    
    #Calculamos el rango R
    R2=Max2-Min2

    #Calculamos el Ancho del Intervalo "i"
    i2=R2/ni

    #Categorización de variables
    #Declaramos 2 intervalos (menores de 100) y (mayores de 100)
    #Ajustamos los limites para que todos los valores sean incluidos en los intervalos
    intervalos2=np.linspace(-0.1, 781.4, 14)
    
    categorias2 = ["0 - 60.0 seg", "60.1 - 120.1 seg", "120.2 - 180.2 seg", "180.3 - 240.4 seg", 
    "240.5 - 300.5 seg", "300.6 - 360.6 seg", "360.7 - 420.7 seg", "420.8 - 480.8 seg","480.9 - 540.9 seg",
    "541.0 - 601.1 seg", "601.2 - 661.2 seg", "661.3 - 721.3 seg", "721.4 - 781.4 seg"]

    #Finalmente creamos las categorías en la columna numérica
    df['tiempo_lección']=pd.cut(x= df['tiempo de lección'], bins=intervalos2, labels= categorias2)

    ############################################################################################################
    #Obtenemos el limite superior y el límite inferior de la columna objetivo
    Max3=df['tiempo de sesión'].max()
    Min3=df['tiempo de sesión'].min()
    Limites3= [Min3, Max3]

    #Calculamos el rango R
    R3=Max3-Min3

    #Calculamos el Ancho del Intervalo "i"
    i3=R3/ni    

    #Categorización de variables
    #Declaramos 2 intervalos (menores de 100) y (mayores de 100)
    #Ajustamos los limites para que todos los valores sean incluidos en los intervalos
    intervalos3=np.linspace(-0.1, 2144.46, 14)

    categorias3=["-0.1-164.9 seg", "165.0-329.8 seg", "329.9-494.8 seg", "494.9-659.8 seg", "659.9-824.7 seg", 
        "824.8-989.7 seg", "989.8-1,154.7 seg", "1,154.8-1,319.6 seg", "1,319.7-1,484.6 seg", "1,484.7-1,649.6 seg", 
        "1,649.7-1,814.5 seg", "1,814.6-1,979.5 seg", "1,979.6-2,144.5 seg"]
    
    #Finalmente creamos las categorías en la columna numérica
    df['tiempo_sesión']=pd.cut(x= df['tiempo de sesión'], bins=intervalos3, labels= categorias3)
    ############################################################################################################

    #Crear una lista de las variables objetivos
    lista=["Administrador", "mini juego", "color presionado", "dificultad", "Juego", "auto push", "botón correcto","tiempo_interacción",
    "tiempo_lección", "tiempo_sesión"]
    return df, lista

####################################
#Cargar los archivos
df, lista =load_data()

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/007/765/451/non_2x/blue-background-illustration-lighting-effect-graphic-for-text-and-message-board-design-infographic-vector.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
####################################
#Creación de dashboard
#Generar las páginas que usaremos en el diseño
#Generar los encabezados para la barra lateral
st.sidebar.title("Dadhboard Wuupi")
st.sidebar.image("logo.png", width=280)
st.sidebar.markdown("---")

#Widget 1:Selectbox
View =st.sidebar.selectbox(label="Pestaña:", options=["Descripción de datos", "Usuarios"])

if View == "Descripción de datos":
    st.subheader("Dataframe de Wuupi")
    st.dataframe(df)
    st.subheader("HeatMap:")
    # Seleccionar solo columnas numéricas para el heatmap
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Crear el heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

if View == "Usuarios":
    df_filtrado1 = df[df['Usuario'] == 'JOSE IAN']
    df_filtrado2 = df[df['Usuario'] == 'JOSE IGNACIO TADEO']
    df_filtrado3 = df[df['Usuario'] == 'JOSHUA']
    df_filtrado4 = df[df['Usuario'] == 'KYTZIA']

    #Extracción de caracterisitcas
    #Selectbox
    variable_cat=st.sidebar.selectbox(label="Variables", options=lista)
    #Obtener las frecuencias de las categorias de la variable seleccionada
    tabla_frecuencias1 =df_filtrado1[variable_cat].value_counts().reset_index()
    tabla_frecuencias1.columns=["categorias", "frecuencia"]

    tabla_frecuencias2 =df_filtrado2[variable_cat].value_counts().reset_index()
    tabla_frecuencias2.columns=["categorias", "frecuencia"]

    tabla_frecuencias3 =df_filtrado3[variable_cat].value_counts().reset_index()
    tabla_frecuencias3.columns=["categorias", "frecuencia"]

    tabla_frecuencias4 =df_filtrado4[variable_cat].value_counts().reset_index()
    tabla_frecuencias4.columns=["categorias", "frecuencia"]

    #Generar los encabezados para el dashboard
    st.title("Extracción de Características")

############################################################################################################
    if variable_cat =="Administrador":
        #Generar el diseño del layout deseado
        #Fila 1
        contenedor_A, contenedor_B =st.columns(2)
        with contenedor_A:
            st.write("JOSE IAN")
            #Graph1: Barplot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure1=px.pie(data_frame=tabla_frecuencias1, names="categorias",
            values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
            figure1.update_layout(height=300)
            st.plotly_chart(figure1, use_container_width=True)

        with contenedor_B:
            st.write("JOSE IGNACIO TADEO")
            #Graph2: pastel
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure2=px.pie(data_frame=tabla_frecuencias2, names="categorias",
            values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
            figure2.update_layout(height=300)
            st.plotly_chart(figure2, use_container_width=True)


        contenedor_C, contenedor_D =st.columns(2)
        with contenedor_C:
            st.write("JOSHUA")
            #Graph3: Donut graph
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure3=px.pie(data_frame=tabla_frecuencias3, names="categorias",
            values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
            figure3.update_layout(height=300)
            st.plotly_chart(figure3, use_container_width=True)

        with contenedor_D:
            st.write("KYTZIA")
            #Graph3: area plot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure4=px.pie(data_frame=tabla_frecuencias4, names="categorias",
            values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
            figure4.update_layout(height=300)
            st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="mini juego":
        #Generar el diseño del layout deseado
        #Fila 1
        contenedor_A, contenedor_B =st.columns(2)
        with contenedor_A:
            st.write("JOSE IAN")
            #Graph1: Barplot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure1=px.bar(data_frame=tabla_frecuencias1, x="categorias",
            y="frecuencia", title=str("Frecuencia por categoría"))
            figure1.update_xaxes(automargin=True)
            figure1.update_yaxes(automargin=True)
            figure1.update_layout(height=300)
            st.plotly_chart(figure1, use_container_width=True)

        with contenedor_B:
            st.write("JOSE IGNACIO TADEO")
           #Graph1: Barplot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure2=px.bar(data_frame=tabla_frecuencias2, x="categorias",
            y="frecuencia", title=str("Frecuencia por categoría"))
            figure2.update_xaxes(automargin=True)
            figure2.update_yaxes(automargin=True)
            figure2.update_layout(height=300)
            st.plotly_chart(figure2, use_container_width=True)


        contenedor_C, contenedor_D =st.columns(2)
        with contenedor_C:
            st.write("JOSHUA")
            #Graph1: Barplot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure3=px.bar(data_frame=tabla_frecuencias3, x="categorias",
            y="frecuencia", title=str("Frecuencia por categoría"))
            figure3.update_xaxes(automargin=True)
            figure3.update_yaxes(automargin=True)
            figure3.update_layout(height=300)
            st.plotly_chart(figure3, use_container_width=True)

        with contenedor_D:
            st.write("KYTZIA")
            #Graph1: Barplot
            #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
            figure4=px.bar(data_frame=tabla_frecuencias4, x="categorias",
            y="frecuencia", title=str("Frecuencia por categoría"))
            figure4.update_xaxes(automargin=True)
            figure4.update_yaxes(automargin=True)
            figure4.update_layout(height=300)
            st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="color presionado":
            #Generar el diseño del layout deseado
            #Fila 1
            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.pie(data_frame=tabla_frecuencias1, names="categorias",
                values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
                #Graph2: pastel
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.pie(data_frame=tabla_frecuencias2, names="categorias",
                values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph3: Donut graph
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.pie(data_frame=tabla_frecuencias3, names="categorias",
                values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.pie(data_frame=tabla_frecuencias4, names="categorias",
                values="frecuencia", hole=0.4, title=str("Frecuencia por categoría"))
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="dificultad":
            #Generar el diseño del layout deseado
            #Fila 1
            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.bar(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_xaxes(automargin=True)
                figure1.update_yaxes(automargin=True)
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
            #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.bar(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_xaxes(automargin=True)
                figure2.update_yaxes(automargin=True)
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.bar(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_xaxes(automargin=True)
                figure3.update_yaxes(automargin=True)
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.bar(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_xaxes(automargin=True)
                figure4.update_yaxes(automargin=True)
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="Juego":
            #Generar el diseño del layout deseado
            #Fila 1
            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.pie(data_frame=tabla_frecuencias1, names="categorias",
                values="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
                #Graph2: pastel
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.pie(data_frame=tabla_frecuencias2, names="categorias",
                values="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph3: Donut graph
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.pie(data_frame=tabla_frecuencias3, names="categorias",
                values="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.pie(data_frame=tabla_frecuencias4, names="categorias",
                values="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="auto push":

            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.bar(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_xaxes(automargin=True)
                figure1.update_yaxes(automargin=True)
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
            #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.bar(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_xaxes(automargin=True)
                figure2.update_yaxes(automargin=True)
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.bar(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_xaxes(automargin=True)
                figure3.update_yaxes(automargin=True)
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.bar(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_xaxes(automargin=True)
                figure4.update_yaxes(automargin=True)
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="botón correcto":

            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.bar(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_xaxes(automargin=True)
                figure1.update_yaxes(automargin=True)
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
            #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.bar(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_xaxes(automargin=True)
                figure2.update_yaxes(automargin=True)
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.bar(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_xaxes(automargin=True)
                figure3.update_yaxes(automargin=True)
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph1: Barplot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.bar(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_xaxes(automargin=True)
                figure4.update_yaxes(automargin=True)
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="tiempo_interacción":

            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.area(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.area(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.area(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.area(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="tiempo_lección":

            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.area(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.area(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.area(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.area(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################
    if variable_cat =="tiempo_sesión":

            contenedor_A, contenedor_B =st.columns(2)
            with contenedor_A:
                st.write("JOSE IAN")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure1=px.area(data_frame=tabla_frecuencias1, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure1.update_layout(height=300)
                st.plotly_chart(figure1, use_container_width=True)

            with contenedor_B:
                st.write("JOSE IGNACIO TADEO")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure2=px.area(data_frame=tabla_frecuencias2, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure2.update_layout(height=300)
                st.plotly_chart(figure2, use_container_width=True)


            contenedor_C, contenedor_D =st.columns(2)
            with contenedor_C:
                st.write("JOSHUA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure3=px.area(data_frame=tabla_frecuencias3, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure3.update_layout(height=300)
                st.plotly_chart(figure3, use_container_width=True)

            with contenedor_D:
                st.write("KYTZIA")
                #Graph3: area plot
                #Despliegue de un barplot definiendo las variables "X categorias" y "Y num"
                figure4=px.area(data_frame=tabla_frecuencias4, x="categorias",
                y="frecuencia", title=str("Frecuencia por categoría"))
                figure4.update_layout(height=300)
                st.plotly_chart(figure4, use_container_width=True)
############################################################################################################