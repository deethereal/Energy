import streamlit as st
import pandas as pd
from random import randint
import base64
import numpy as np
import joblib
from PIL import Image
from catboost import CatBoostRegressor
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="answers.csv">Download answers.csv</a>'

st.set_page_config(layout="wide")
st.title('Демо версия модели')
model = CatBoostRegressor().load_model('CatBoost1.pkl')
with st.form('text'):

	image = Image.open('map.jpg')	
	if image.mode != 'RGB':
		image = image.convert('RGB')
	img_array = np.array(image) # if you want to pass it to OpenCV
	st.image(image, use_column_width=True)
	c1,c2,c3,c4= st.columns([1,1,1,1])
	c5,c6,c7,c8,c9,c10,c11,c12,c13 = st.columns([1,1,1,1,1,1,1,1,1])
	c14,c15,c16,c17,c18,c19,c20,c21 = st.columns([1,1,1,1,1,1,1,1])
	c22,c23,c24,c25 = st.columns([1,1,1,1])
	PGRS_1= c1.text_input("PGRS_1", value=0)
	QGRS_1= c2.text_input("QGRS_1", value=0)
	PGRS_2= c3.text_input("PGRS_2", value=0)
	QGRS_2= c4.text_input("QGRS_2", value=0)
	P_1= c5.text_input("P_1", value=0)
	P_2= c6.text_input("P_2", value=0)
	P_3= c7.text_input("P_3", value=0)
	P_4= c8.text_input("P_4", value=0)
	P_5= c9.text_input("P_5", value=0)
	P_6= c10.text_input("P_6", value=0)
	P_7= c11.text_input("P_7", value=0)
	P_8 = c12.text_input("P_8", value=0)
	P_9= c13.text_input("P_9", value=0)
	Q_1= c14.text_input("Q_1", value=0)
	Q_2= c15.text_input("Q_2", value=0)
	Q_3= c16.text_input("Q_3", value=0)
	Q_4= c17.text_input("Q_4", value=0)
	Q_5= c18.text_input("Q_5", value=0)
	Q_6= c19.text_input("Q_6", value=0)
	Q_7= c20.text_input("Q_7", value=0)
	Q_8= c21.text_input("Q_8", value=0)
	QPlant_1= c22.text_input("QPlant_1", value=0)
	QPlant_2= c23.text_input("QPlant_2", value=0)
	QPlant_3= c24.text_input("QPlant_3", value=0)
	QPlant_4= c25.text_input("QPlant_4", value=0)

	file_button = st.form_submit_button('Посчитать значения заслонок')
	if file_button:
		df = pd.DataFrame(data=np.array([QGRS_1, QGRS_2, QPlant_1, QPlant_2, QPlant_3, QPlant_4,
       PGRS_1, PGRS_2, P_1, P_2, P_3, P_4, P_5, P_6, P_7,
       P_8, P_9, Q_1, Q_2, Q_3, Q_4, Q_5, Q_6, Q_7]).reshape(1,-1),
       columns=['QGRS_1', 'QGRS_2', 'QPlant_1', 'QPlant_2', 'QPlant_3', 'QPlant_4',
       'PGRS_1', 'PGRS_2', 'P_1', 'P_2', 'P_3', 'P_4', 'P_5', 'P_6', 'P_7',
       'P_8', 'P_9', 'Q_1', 'Q_2', 'Q_3', 'Q_4', 'Q_5', 'Q_6', 'Q_7'], index=[0])
		
		preds = pd.DataFrame(model.predict(df), columns=['Заслонка '+str(i) for i in range(1,13)])
		st.table(preds)

st.write('OR')


with st.form('file'):
	uploaded_file = st.file_uploader("Upload a csv file", ["csv"])
	file_button = st.form_submit_button('Predict labels')
	if uploaded_file:
		try:
			file = pd.read_csv(uploaded_file,sep=';')
		except:
			file = pd.read_csv(uploaded_file)

		file=file.replace(',','.',regex=True).astype('float64')
		st.write(file.describe())
			


				