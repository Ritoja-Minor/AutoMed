#importing all the necessary modules or libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import gspread
import time

#setting the page initial layout
st.set_page_config(layout="wide",initial_sidebar_state='collapsed')


#loading data from google sheet
@st.cache
def get_data_from_gs():

    gc = gspread.service_account(filename='creds.json')

    rank_sh = gc.open_by_key('1dkI7rXNVF9omWsXxkuN4xJzptFY-hrWBG-VpJTHgPcU')
    prec_sh = gc.open_by_key('1JrLqLOuJZqmpihsBUsgZajtYeXkpwMAScbhw3kNybg0')
    desp_sh = gc.open_by_key('1Ng5dVnoqYkHEjME5QhIVhFHf-zaIrjkdqwPEiOgP12c')

    rank_worksheet = rank_sh.sheet1
    rank_ = rank_worksheet.get_all_records()
    rank_df = pd.DataFrame(rank_)


    prec_worksheet = prec_sh.sheet1
    prec_ = prec_worksheet.get_all_records()
    prec_df = pd.DataFrame(prec_)


    desp_worksheet = desp_sh.sheet1
    desp_ = desp_worksheet.get_all_records()
    desp_df = pd.DataFrame(desp_)


    return rank_df,prec_df,desp_df

df_rank,dis_prec,dis_desp = get_data_from_gs()


#making the necessary dictionaries to map the values as required
rank_dict = dict(zip(df_rank.Symptom.to_list(),df_rank.weight.to_list()))
desp_dict = dict(zip(dis_desp.Disease.to_list(),dis_desp.Description.to_list()))


#Creating the title and the necessary header sections of the webapp
st.title('Welcome to AutoMed')
st.write('**AutoMed is a WebApp which has the ability to predict Diseases according to the Symptoms provided.**')
st.markdown('**You can provide a maximum of 17 symptoms and a minimum of 6 symptoms.**')
st.markdown('---')


#Creating the sidebar
st.sidebar.markdown('# DiseasePedia')
option = st.sidebar.selectbox(
   "",
('None',
 '(vertigo) Paroymsal  Positional Vertigo',
 'AIDS',
 'Acne',
 'Alcoholic hepatitis',
 'Allergy',
 'Arthritis',
 'Bronchial Asthma',
 'Cervical spondylosis',
 'Chicken pox',
 'Chronic cholestasis',
 'Common Cold',
 'Dengue',
 'Diabetes ',
 'Dimorphic hemmorhoids(piles)',
 'Drug Reaction',
 'Fungal infection',
 'GERD',
 'Gastroenteritis',
 'Heart attack',
 'Hepatitis B',
 'Hepatitis C',
 'Hepatitis D',
 'Hepatitis E',
 'Hypertension ',
 'Hyperthyroidism',
 'Hypoglycemia',
 'Hypothyroidism',
 'Impetigo',
 'Jaundice',
 'Malaria',
 'Migraine',
 'Osteoarthristis',
 'Paralysis (brain hemorrhage)',
 'Peptic ulcer diseae',
 'Pneumonia',
 'Psoriasis',
 'Tuberculosis',
 'Typhoid',
 'Urinary tract infection',
 'Varicose veins',
 'Hepatitis A')
)


#The code below is used to show the precautions in the sidebar after the selection of the disease
if option=='None':
 st.sidebar.write('')
else:
 st.sidebar.write(desp_dict[option])
 st.sidebar.write('# Precautions :\n')
 for i, prec in enumerate(list(dis_prec.loc[(dis_prec.Disease == option), 'Precaution_1':])):
  st.sidebar.write(f'{i+1}. {dis_prec[(dis_prec.Disease == option)][prec].values[0]}')


#Giving a gap between the two elements
st.markdown(
"""
<br><br/>
""", unsafe_allow_html=True)


#Making the necessary number of tabs for the symptoms
col1,col2,col3,col4 =  st.beta_columns(4)
col5,col6,col7,col8 =  st.beta_columns(4)
col9,col10,col11,col12 =  st.beta_columns(4)
col13,col14,col15,col16 =  st.beta_columns(4)
col17,col18,col19,col20 =  st.beta_columns(4)
col21,col22,col23,col24 =  st.beta_columns(4)
col25,col26,col27,col28 =  st.beta_columns(4)
col29,col30,col31,col32 =  st.beta_columns(4)
col33,col34,col35,col36 =  st.beta_columns(4)
col37,col38,col39,col40 =  st.beta_columns(4)
col41,col42,col43,col44 =  st.beta_columns(4)
col45,col46,col47,col48 =  st.beta_columns(4)
col49,col50,col51,col52 =  st.beta_columns(4)
col53,col54,col55,col56 =  st.beta_columns(4)
col57,col58,col59,col60 =  st.beta_columns(4)
col61,col62,col63,col64 =  st.beta_columns(4)
col65,col66,col67,col68 =  st.beta_columns(4)
col69,col70,col71,col72 =  st.beta_columns(4)
col73,col74,col75,col76 =  st.beta_columns(4)
col77,col78,col79,col80 =  st.beta_columns(4)
col81,col82,col83,col84 =  st.beta_columns(4)
col85,col86,col87,col88 =  st.beta_columns(4)
col89,col90,col91,col92 =  st.beta_columns(4)
col93,col94,col95,col96 =  st.beta_columns(4)
col97,col98,col99,col100 =  st.beta_columns(4)
col101,col102,col103,col104 =  st.beta_columns(4)
col105,col106,col107,col108 =  st.beta_columns(4)
col109,col110,col111,col112 =  st.beta_columns(4)
col113,col114,col115,col116 =  st.beta_columns(4)
col117,col118,col119,col120 =  st.beta_columns(4)
col121,col122,col123,col124 =  st.beta_columns(4)
col125,col126,col127,col128 =  st.beta_columns(4)
col129,col130,col131,col132 =  st.beta_columns(4)
col133,col134 =  st.beta_columns(2)


#Empty list to enter the severity of the diseases
dis = []


#Checking the values of the selected checkboxes
if col1.checkbox('itching'):
 dis.append(rank_dict['itching'])
# else:
#  dis.append(0)
if col2.checkbox('skin_rash'):
 dis.append(rank_dict['skin_rash'])
# else:
#  dis.append(0)
if col3.checkbox('nodal_skin_eruptions'):
 dis.append(rank_dict['nodal_skin_eruptions'])
# else:
#  dis.append(0)
if col4.checkbox('continuous_sneezing'):
 dis.append(rank_dict['continuous_sneezing'])
# else:
#  dis.append(0)
if col5.checkbox('shivering'):
 dis.append(rank_dict['shivering'])
# else:
#  dis.append(0)
if col6.checkbox('chills'):
 dis.append(rank_dict['chills'])
# else:
#  dis.append(0)
if col7.checkbox('joint_pain'):
 dis.append(rank_dict['joint_pain'])
# else:
#  dis.append(0)
if col8.checkbox('stomach_pain'):
 dis.append(rank_dict['stomach_pain'])
# else:
#  dis.append(0)
if col9.checkbox('acidity'):
 dis.append(rank_dict['acidity'])
# else:
#  dis.append(0)
if col10.checkbox('ulcers_on_tongue'):
 dis.append(rank_dict['ulcers_on_tongue'])
# else:
#  dis.append(0)
if col11.checkbox('muscle_wasting'):
 dis.append(rank_dict['muscle_wasting'])
# else:
#  dis.append(0)
if col12.checkbox('vomiting'):
 dis.append(rank_dict['vomiting'])
# else:
#  dis.append(0)
if col13.checkbox('burning_micturition'):
 dis.append(rank_dict['burning_micturition'])
# else:
#  dis.append(0)
if col14.checkbox('spotting_urination'):
 dis.append(rank_dict['spotting_urination'])
# else:
#  dis.append(0)
if col15.checkbox('fatigue'):
 dis.append(rank_dict['fatigue'])
# else:
#  dis.append(0)
if col16.checkbox('weight_gain'):
 dis.append(rank_dict['weight_gain'])
# else:
#  dis.append(0)
if col17.checkbox('anxiety'):
 dis.append(rank_dict['anxiety'])
# else:
#  dis.append(0)
if col18.checkbox('cold_hands_and_feets'):
 dis.append(rank_dict['cold_hands_and_feets'])
# else:
#  dis.append(0)
if col19.checkbox('mood_swings'):
 dis.append(rank_dict['mood_swings'])
# else:
#  dis.append(0)
if col21.checkbox('weight_loss'):
 dis.append(rank_dict['weight_loss'])
# else:
#  dis.append(0)
if col22.checkbox('restlessness'):
 dis.append(rank_dict['restlessness'])
# else:
#  dis.append(0)
if col23.checkbox('lethargy'):
 dis.append(rank_dict['lethargy'])
# else:
#  dis.append(0)
if col24.checkbox('patches_in_throat'):
 dis.append(rank_dict['patches_in_throat'])
# else:
#  dis.append(0)
if col25.checkbox('irregular_sugar_level'):
 dis.append(rank_dict['irregular_sugar_level'])
# else:
#  dis.append(0)
if col26.checkbox('cough'):
 dis.append(rank_dict['cough'])
# else:
#  dis.append(0)
if col27.checkbox('high_fever'):
 dis.append(rank_dict['high_fever'])
# else:
#  dis.append(0)
if col28.checkbox('sunken_eyes'):
 dis.append(rank_dict['sunken_eyes'])
# else:
#  dis.append(0)
if col29.checkbox('breathlessness'):
 dis.append(rank_dict['breathlessness'])
# else:
#  dis.append(0)
if col30.checkbox('sweating'):
 dis.append(rank_dict['sweating'])
# else:
#  dis.append(0)
if col31.checkbox('dehydration'):
 dis.append(rank_dict['dehydration'])
# else:
#  dis.append(0)
if col32.checkbox('indigestion'):
 dis.append(rank_dict['indigestion'])
# else:
#  dis.append(0)
if col33.checkbox('headache'):
 dis.append(rank_dict['headache'])
# else:
#  dis.append(0)
if col34.checkbox('yellowish_skin'):
 dis.append(rank_dict['yellowish_skin'])
# else:
#  dis.append(0)
if col35.checkbox('dark_urine'):
 dis.append(rank_dict['dark_urine'])
# else:
#  dis.append(0)
if col36.checkbox('nausea'):
 dis.append(rank_dict['nausea'])
# else:
#  dis.append(0)
if col37.checkbox('loss_of_appetite'):
 dis.append(rank_dict['loss_of_appetite'])
# else:
#  dis.append(0)
if col38.checkbox('pain_behind_the_eyes'):
 dis.append(rank_dict['pain_behind_the_eyes'])
# else:
#  dis.append(0)
if col39.checkbox('back_pain'):
 dis.append(rank_dict['back_pain'])
# else:
#  dis.append(0)
if col40.checkbox('constipation'):
 dis.append(rank_dict['constipation'])
# else:
#  dis.append(0)
if col41.checkbox('abdominal_pain'):
 dis.append(rank_dict['abdominal_pain'])
# else:
#  dis.append(0)
if col42.checkbox('diarrhoea'):
 dis.append(rank_dict['diarrhoea'])
# else:
#  dis.append(0)
if col43.checkbox('mild_fever'):
 dis.append(rank_dict['mild_fever'])
# else:
#  dis.append(0)
if col44.checkbox('yellow_urine'):
 dis.append(rank_dict['yellow_urine'])
# else:
#  dis.append(0)
if col45.checkbox('yellowing_of_eyes'):
 dis.append(rank_dict['yellowing_of_eyes'])
# else:
#  dis.append(0)
if col46.checkbox('acute_liver_failure'):
 dis.append(rank_dict['acute_liver_failure'])
# else:
#  dis.append(0)
if col47.checkbox('fluid_overload'):
 dis.append(rank_dict['fluid_overload'])
# else:
#  dis.append(0)
if col48.checkbox('swelling_of_stomach'):
 dis.append(rank_dict['swelling_of_stomach'])
# else:
#  dis.append(0)
if col49.checkbox('swelled_lymph_nodes'):
 dis.append(rank_dict['swelled_lymph_nodes'])
# else:
#  dis.append(0)
if col50.checkbox('malaise'):
 dis.append(rank_dict['malaise'])
# else:
#  dis.append(0)
if col51.checkbox('blurred_and_distorted_vision'):
 dis.append(rank_dict['blurred_and_distorted_vision'])
# else:
#  dis.append(0)
if col52.checkbox('phlegm'):
 dis.append(rank_dict['phlegm'])
# else:
#  dis.append(0)
if col53.checkbox('throat_irritation'):
 dis.append(rank_dict['throat_irritation'])
# else:
#  dis.append(0)
if col54.checkbox('redness_of_eyes'):
 dis.append(rank_dict['redness_of_eyes'])
# else:
#  dis.append(0)
if col56.checkbox('sinus_pressure'):
 dis.append(rank_dict['sinus_pressure'])
# else:
#  dis.append(0)
if col57.checkbox('runny_nose'):
 dis.append(rank_dict['runny_nose'])
# else:
#  dis.append(0)
if col58.checkbox('congestion'):
 dis.append(rank_dict['congestion'])
# else:
#  dis.append(0)
if col59.checkbox('chest_pain'):
 dis.append(rank_dict['chest_pain'])
# else:
#  dis.append(0)
if col60.checkbox('weakness_in_limbs'):
 dis.append(rank_dict['weakness_in_limbs'])
# else:
#  dis.append(0)
if col61.checkbox('fast_heart_rate'):
 dis.append(rank_dict['fast_heart_rate'])
# else:
#  dis.append(0)
if col62.checkbox('pain_during_bowel_movements'):
 dis.append(rank_dict['pain_during_bowel_movements'])
# else:
#  dis.append(0)
if col63.checkbox('pain_in_anal_region'):
 dis.append(rank_dict['pain_in_anal_region'])
# else:
#  dis.append(0)
if col64.checkbox('bloody_stool'):
 dis.append(rank_dict['bloody_stool'])
# else:
#  dis.append(0)
if col65.checkbox('irritation_in_anus'):
 dis.append(rank_dict['irritation_in_anus'])
# else:
#  dis.append(0)
if col66.checkbox('neck_pain'):
 dis.append(rank_dict['neck_pain'])
# else:
#  dis.append(0)
if col67.checkbox('dizziness'):
 dis.append(rank_dict['dizziness'])
# else:
#  dis.append(0)
if col68.checkbox('cramps'):
 dis.append(rank_dict['cramps'])
# else:
#  dis.append(0)
if col69.checkbox('bruising'):
 dis.append(rank_dict['bruising'])
# else:
#  dis.append(0)
if col70.checkbox('obesity'):
 dis.append(rank_dict['obesity'])
# else:
#  dis.append(0)
if col71.checkbox('wollen_legs'):
 dis.append(rank_dict['wollen_legs'])
# else:
#  dis.append(0)
if col72.checkbox('swollen_blood_vessels'):
 dis.append(rank_dict['swollen_blood_vessels'])
# else:
#  dis.append(0)
if col73.checkbox('puffy_face_and_eyes'):
 dis.append(rank_dict['puffy_face_and_eyes'])
# else:
#  dis.append(0)
if col74.checkbox('enlarged_thyroid'):
 dis.append(rank_dict['enlarged_thyroid'])
# else:
#  dis.append(0)
if col75.checkbox('brittle_nails'):
 dis.append(rank_dict['brittle_nails'])
# else:
#  dis.append(0)
if col76.checkbox('swollen_extremeties'):
 dis.append(rank_dict['swollen_extremeties'])
# else:
#  dis.append(0)
if col77.checkbox('excessive_hunger'):
 dis.append(rank_dict['excessive_hunger'])
# else:
#  dis.append(0)
if col78.checkbox('extra_marital_contacts'):
 dis.append(rank_dict['extra_marital_contacts'])
# else:
#  dis.append(0)
if col79.checkbox('drying_and_tingling_lips'):
 dis.append(rank_dict['drying_and_tingling_lips'])
# else:
#  dis.append(0)
if col80.checkbox('slurred_speech'):
 dis.append(rank_dict['slurred_speech'])
# else:
#  dis.append(0)
if col81.checkbox('knee_pain'):
 dis.append(rank_dict['knee_pain'])
# else:
#  dis.append(0)
if col82.checkbox('hip_joint_pain'):
 dis.append(rank_dict['hip_joint_pain'])
# else:
#  dis.append(0)
if col83.checkbox('muscle_weakness'):
 dis.append(rank_dict['muscle_weakness'])
# else:
#  dis.append(0)
if col84.checkbox('stiff_neck'):
 dis.append(rank_dict['stiff_neck'])
# else:
#  dis.append(0)
if col85.checkbox('swelling_joints'):
 dis.append(rank_dict['swelling_joints'])
# else:
#  dis.append(0)
if col86.checkbox('movement_stiffness'):
 dis.append(rank_dict['movement_stiffness'])
# else:
#  dis.append(0)
if col87.checkbox('spinning_movements'):
 dis.append(rank_dict['spinning_movements'])
# else:
#  dis.append(0)
if col88.checkbox('loss_of_balance'):
 dis.append(rank_dict['loss_of_balance'])
# else:
#  dis.append(0)
if col89.checkbox('unsteadiness'):
 dis.append(rank_dict['unsteadiness'])
# else:
#  dis.append(0)
if col90.checkbox('weakness_of_one_body_side'):
 dis.append(rank_dict['weakness_of_one_body_side'])
# else:
#  dis.append(0)
if col91.checkbox('loss_of_smell'):
 dis.append(rank_dict['loss_of_smell'])
# else:
#  dis.append(0)
if col92.checkbox('bladder_discomfort'):
 dis.append(rank_dict['bladder_discomfort'])
# else:
#  dis.append(0)
if col93.checkbox('foul_smell_ofurine'):
  dis.append(rank_dict['foul_smell_ofurine'])
# else:
#  dis.append(0)
if col94.checkbox('continuous_feel_of_urine'):
 dis.append(rank_dict['continuous_feel_of_urine'])
# else:
#  dis.append(0)
if col95.checkbox('passage_of_gases'):
 dis.append(rank_dict['passage_of_gases'])
# else:
#  dis.append(0)
if col96.checkbox('internal_itching'):
 dis.append(rank_dict['internal_itching'])
# else:
#  dis.append(0)
if col97.checkbox('toxic_look_(typhos)'):
 dis.append(rank_dict['toxic_look_(typhos)'])
# else:
#  dis.append(0)
if col98.checkbox('depression'):
 dis.append(rank_dict['depression'])
# else:
#  dis.append(0)
if col99.checkbox('irritability'):
 dis.append(rank_dict['irritability'])
# else:
#  dis.append(0)
if col100.checkbox('muscle_pain'):
 dis.append(rank_dict['muscle_pain'])
# else:
#  dis.append(0)
if col101.checkbox('altered_sensorium'):
 dis.append(rank_dict['altered_sensorium'])
# else:
#  dis.append(0)
if col102.checkbox('red_spots_over_body'):
 dis.append(rank_dict['red_spots_over_body'])
# else:
#  dis.append(0)
if col103.checkbox('belly_pain'):
 dis.append(rank_dict['belly_pain'])
# else:
#  dis.append(0)
if col104.checkbox('abnormal_menstruation'):
 dis.append(rank_dict['abnormal_menstruation'])
# else:
#  dis.append(0)
if col105.checkbox('dischromic_patches'):
 dis.append(rank_dict['dischromic_patches'])
# else:
#  dis.append(0)
if col106.checkbox('watering_from_eyes'):
 dis.append(rank_dict['watering_from_eyes'])
# else:
#  dis.append(0)
if col107.checkbox('increased_appetite'):
 dis.append(rank_dict['increased_appetite'])
# else:
#  dis.append(0)
if col108.checkbox('polyuria'):
 dis.append(rank_dict['polyuria'])
# else:
#  dis.append(0)
if col109.checkbox('family_history'):
 dis.append(rank_dict['family_history'])
# else:
#  dis.append(0)
if col110.checkbox('mucoid_sputum'):
 dis.append(rank_dict['mucoid_sputum'])
# else:
#  dis.append(0)
if col111.checkbox('rusty_sputum'):
 dis.append(rank_dict['rusty_sputum'])
# else:
#  dis.append(0)
if col112.checkbox('lack_of_concentration'):
 dis.append(rank_dict['lack_of_concentration'])
# else:
#  dis.append(0)
if col113.checkbox('visual_disturbances'):
 dis.append(rank_dict['visual_disturbances'])
# else:
#  dis.append(0)
if col114.checkbox('receiving_blood_transfusion'):
 dis.append(rank_dict['receiving_blood_transfusion'])
# else:
#  dis.append(0)
if col115.checkbox('receiving_unsterile_injections'):
  dis.append(rank_dict['receiving_unsterile_injections'])
# else:
#  dis.append(0)
if col116.checkbox('coma'):
 dis.append(rank_dict['coma'])
# else:
#  dis.append(0)
if col117.checkbox('stomach_bleeding'):
 dis.append(rank_dict['stomach_bleeding'])
# else:
#  dis.append(0)
if col118.checkbox('distention_of_abdomen'):
 dis.append(rank_dict['distention_of_abdomen'])
# else:
#  dis.append(0)
if col119.checkbox('history_of_alcohol_consumption'):
 dis.append(rank_dict['history_of_alcohol_consumption'])
# else:
#  dis.append(0)
if col120.checkbox('blood_in_sputum'):
 dis.append(rank_dict['blood_in_sputum'])
# else:
#  dis.append(0)
if col121.checkbox('prominent_veins_on_calf'):
 dis.append(rank_dict['prominent_veins_on_calf'])
# else:
#  dis.append(0)
if col122.checkbox('palpitations'):
 dis.append(rank_dict['palpitations'])
# else:
#  dis.append(0)
if col123.checkbox('painful_walking'):
 dis.append(rank_dict['painful_walking'])
# else:
#  dis.append(0)
if col124.checkbox('pus_filled_pimples'):
 dis.append(rank_dict['pus_filled_pimples'])
# else:
#  dis.append(0)
if col125.checkbox('blackheads'):
 dis.append(rank_dict['blackheads'])
# else:
#  dis.append(0)
if col126.checkbox('scurring'):
 dis.append(rank_dict['scurring'])
# else:
#  dis.append(0)
if col127.checkbox('skin_peeling'):
 dis.append(rank_dict['skin_peeling'])
# else:
#  dis.append(0)
if col128.checkbox('silver_like_dusting'):
 dis.append(rank_dict['silver_like_dusting'])
# else:
#  dis.append(0)
if col129.checkbox('small_dents_in_nails'):
 dis.append(rank_dict['small_dents_in_nails'])
# else:
#  dis.append(0)
if col130.checkbox('inflammatory_nails'):
 dis.append(rank_dict['inflammatory_nails'])
# else:
#  dis.append(0)
if col131.checkbox('blister'):
 dis.append(rank_dict['blister'])
# else:
#  dis.append(0)
if col132.checkbox('red_sore_around_nose'):
 dis.append(rank_dict['red_sore_around_nose'])
# else:
#  dis.append(0)
if col133.checkbox('yellow_crust_ooze'):
 dis.append(rank_dict['yellow_crust_ooze'])
# else:
#  dis.append(0)
if col134.checkbox('prognosis'):
 dis.append(rank_dict['prognosis'])
# else:
#  dis.append(0)


#Providing a gap in between the two elements
st.markdown(
"""
<br><br/>
"""
, unsafe_allow_html=True
)


#the below code is used to check the number of symptoms selected and the number of symptoms required for prediction
if (len(dis)>=6) and (len(dis)<17):
 diff = 17-len(dis)
 for i in range(diff):
  dis.append(0)



#The below dict is used to map the prediction to the name of the diseases
final_pred_dict = \
 {0: '(vertigo) Paroymsal  Positional Vertigo',
 1: 'AIDS',
 2: 'Acne',
 3: 'Alcoholic hepatitis',
 4: 'Allergy',
 5: 'Arthritis',
 6: 'Bronchial Asthma',
 7: 'Cervical spondylosis',
 8: 'Chicken pox',
 9: 'Chronic cholestasis',
 10: 'Common Cold',
 11: 'Dengue',
 12: 'Diabetes ',
 13: 'Dimorphic hemmorhoids(piles)',
 14: 'Drug Reaction',
 15: 'Fungal infection',
 16: 'GERD',
 17: 'Gastroenteritis',
 18: 'Heart attack',
 19: 'Hepatitis B',
 20: 'Hepatitis C',
 21: 'Hepatitis D',
 22: 'Hepatitis E',
 23: 'Hypertension ',
 24: 'Hyperthyroidism',
 25: 'Hypoglycemia',
 26: 'Hypothyroidism',
 27: 'Impetigo',
 28: 'Jaundice',
 29: 'Malaria',
 30: 'Migraine',
 31: 'Osteoarthristis',
 32: 'Paralysis (brain hemorrhage)',
 33: 'Peptic ulcer diseae',
 34: 'Pneumonia',
 35: 'Psoriasis',
 36: 'Tuberculosis',
 37: 'Typhoid',
 38: 'Urinary tract infection',
 39: 'Varicose veins',
 40: 'Hepatitis A'}


#the below code is used to make the predictions and display the disease that is predicted
result=299                                                   #random seed value can be any value greater than 140
p1,p2,p3 = st.beta_columns([2,1,1.5])
with p2:
 if st.button('Predict'):
    if len(dis)<6:
        st.text('\nPlease increase the number of symptoms.\n')
    elif len(dis)>17:
        st.text('\nThe number of symptoms should be less than 17, please reduce the count.\n')
    else:
        with st.spinner('Loading Model...'):                 #to display the loading model sign
          filename = 'Symptoms_model.sav'
          loaded_model = pickle.load(open(filename, 'rb'))
          time.sleep(1.5)
        with st.spinner('Making Predictions...'):
          result = loaded_model.predict(np.array(dis).reshape(1, -1))[0]
          time.sleep(1.5)


#This code is used to demonstrate the action after pressing the predict button.
if result==299:
 st.markdown('')
elif (len(set(dis))==1) and (list(set(dis))[0]==0):
 ph = st.empty()
 ph.text('Warning : Please select the Symptoms First.')
else:
 st.markdown(f'## You may have : {final_pred_dict[result]}')
 st.markdown('Following are the precautions that you should take.')
 for i,prec in enumerate(list(dis_prec.loc[(dis_prec.Disease == final_pred_dict[result]), 'Precaution_1':])):
  st.write(f'{i+1}. {dis_prec[(dis_prec.Disease == final_pred_dict[result])][prec].values[0]}')



