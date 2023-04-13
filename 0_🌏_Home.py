import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Road Devil",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    initial_d = Image.open('data/Others/Initial_D_Logo.png')
    st.image(initial_d, caption='Initial D Arcade Stage 5', use_column_width=True)
    
title, title_graph = st.columns(2)

with title_graph:
    graph = Image.open('./data/Others/Initial_D_Arcade_Stage_5.webp')
    st.image(graph, use_column_width=True)
    
with title:
    st.title('Road Devil' )

st.header('Discription')

st.markdown("### > **Road Devil** is an **Initial D Arcade Stage 5** `(an arcade racing game)` team constructed by `JYL` and `YOH`, at first there were over 30 drivers from China, Sichuan. RD now mainly refers to the small team of five drivers who  represented Mianyang to participate in an intercity challenge in 2012/07/21. they won the championship of the race against SSR team from ChengDu and become the best team of the The southwest of China. ")

# We could use a decorator like the next line to acceleate this
@st.cache_data
def load_data(data_add='./data/drivers.csv'):
    cosmetics_data = pd.read_csv(data_add)
    return cosmetics_data

data = load_data()

# Drivers Part
st.header('Drivers')

driver1, driver2, driver3, driver4, driver5 = st.tabs(['TIGA', 'YOH', 'JYL', 'TONG', 'XIAO'],)

with driver1:
    tiga, ae86 = Image.open('./data/driver_photos/tiga.jpg'), Image.open('./data/Others/ae86.png')
    akina_1, akina_2 = Image.open('data/course/akina_01.png'), Image.open('data/course/akina_02.png')
    photo, discription, course = st.columns(3)
    
    with photo:
        st.image(tiga, use_column_width=True)
        
        
    with discription:
        st.info('## The best Time Attacker of RD')
        st.success('#### **Car**:     TRUENO 3door GT-APEX(AE86)')
        st.image(ae86,use_column_width=True)
        st.markdown("####  **Discription**:\n #### `TIGA` was initially noticed by `JYL` for his awsome Akina downhill, he is one of **RD's Double ACE** and **The Time Attacker**. He was called `Takumi` due to his youngest age. Now he works in Shanghai and his spare time interest is artificial intelligence technology.")
    
    with course:
        st.success('#### **Home Course**:     秋名 (Akina)')
        st.image(akina_1, use_column_width=True)
        st.image(akina_2, use_column_width=True)
        
        

with driver2:
    yoh, cap = Image.open('./data/driver_photos/yoh.jpg'), Image.open('./data/Others/cap.png')
    irohazaka_01, irohazaka_02 = Image.open('data/course/irohazaka_01.png'), Image.open('data/course/irohazaka_02.png')
    photo, discription, course = st.columns(3)
    
    with photo:
        st.image(yoh, use_column_width=True)
        
    with discription:
        st.info('## The leader and mind of RD')
        st.success('#### **Car**: Suzuki Cappuccino')
        st.image(cap, use_column_width=True)
        st.markdown('#### **Discription**:\n #### Brain of RD. In 2009-2010, `YOH` was one of the strongest driver, famous in the D5 racing world in Mianyang. He and his red Cappuccino held the Inohazaka downhill record for a long time, `YOH` loves Go in his spare time,  he now has a cute and lovely daughter who is in primary school.')
        
    with course:
        st.success('#### **Home Course**: いろは坂 (Irohazaka)')
        st.image(irohazaka_01, use_column_width=True)
        st.image(irohazaka_02, use_column_width=True)
        

with driver3:
    jyl, fd6 = Image.open('./data/driver_photos/jyl.jpg'), Image.open('data/Others/fd6.png')
    happogahara_01, happogahara_02 = Image.open('./data/course/happogahara_01.png'), Image.open('./data/course/happogahara_02.png')
    photo, discription, course = st.columns(3)
    
    with photo:
        st.image(jyl, use_column_width=True)
        
    with discription:
        st.info('## The best battler of RD.')
        st.success('#### **Car**: RX-7 Type RS [FD3S]')
        st.image(fd6)
        st.markdown("#### **Discription**: Frontier of initial D in Mianyang, has been recognized as the strongest character for a long time. `JYL` likes compound courses involving uphill and downhill. As the first member who take the field, he won two important races at happogahara in Chengdu in the against game.")
    
    with course:
        st.success('#### **Home Course**: 八方ヶ原 (Happogahara)')
        st.image(happogahara_01, use_column_width=True)
        st.image(happogahara_02, use_column_width=True)
        
        
        
    

st.header('Group Photo')
# st.dataframe(data)
image = Image.open('./data/4drivers.jpg')
st.image(image, caption='Tong JYL TIGA XIAO', use_column_width=True)

# Advice Part
st.header("Any advice for this page?")

comment = st.text_area('')
enter = st.button('Enter')

if enter:
    st.markdown('Hello, this is ChatGPT!')
else:
    st.write("We have gpt-3.5-turbo to be a chatbot.")





