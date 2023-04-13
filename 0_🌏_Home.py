import pandas as pd
import streamlit as st
from PIL import Image
from utils.gpt_answer import get_answer
    
st.set_page_config(
    page_title="Road Devil",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    initial_d = Image.open('/Users/cuiyaodong/Downloads/TreeDyApp/data/Others/Initial_D_Arcade_Stage_5.webp')
    st.image(initial_d, caption='Initial D Arcade Stage 5', use_column_width=True)
    

st.title('Road Devil' )

st.header('Discription')
# annotated_text(
#     "**Road Devil** is an",
#     (" **Initial D Arcade Stage 5**",  "an arcade racing game"),
#     "team constructed by `JYL` and `Yoh`, at first there were over 30 drivers from China, Sichuan. In 2012/07/21, they won the championship of the race against SSR team from ChengDu and become the best team of the The southwest of China."
# )
st.markdown("> **Road Devil** is an **Initial D Arcade Stage 5** `(an arcade racing game)` team constructed by `JYL` and `Yoh`, at first there were over 30 drivers from China, Sichuan. RD now mainly refers to the small team of five drivers who  represented Mianyang to participate in an intercity challenge in 2012/07/21. they won the championship of the race against SSR team from ChengDu and become the best team of the The southwest of China. ")

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
    tiga = Image.open('/Users/cuiyaodong/Downloads/TreeDyApp/data/driver_photos/tiga.jpg')
    photo, discription = st.columns(2)
    with photo:
        st.image(tiga, width=250)
    with discription:
        st.info('## The best time attack driver of RD.')
        st.success('**Car**:     TRUENO 3door GT-APEX(AE86)')
        st.success('**Home Course**:     秋名 (Akina)')
        st.markdown("> **Discription**:\n `TIGA` was initially noticed by `JYL` for his awsome Akina downhill, he is one of **RD's Double ACE** and **The Time Attacker**. He was called `Takumi` due to his youngest age. He currently work in Shanghai and his spare time interest is artificial intelligence technology.")
        

with driver2:
    yoh = Image.open('/Users/cuiyaodong/Downloads/TreeDyApp/data/driver_photos/yoh.jpg')
    photo, discription = st.columns(2)
    with photo:
        st.image(yoh, width=250)
    with discription:
        st.info('## The leader and mind of RD.')
        st.success('**Car**: Suzuki Cappuccino')
        st.success('**Home Course**: いろは坂 (Irohazaka)')
        st.markdown('> **Discription**: Brain of RD. In 2009-2010, `YOH` was one of the strongest driver, famous in the D5 racing world in Mianyang. He and his red Cappuccino held the Inohazaka downhill record for a long time, `YOH` loves Go in his spare time,  he now has a cute daughter who .')

with driver3:
    jyl = Image.open('/Users/cuiyaodong/Downloads/TreeDyApp/data/driver_photos/yoh.jpg')
    photo, discription = st.columns(2)
    with photo:
        st.image(jyl, width=250)
    with discription:
        st.info('## The leader and mind of RD.')
        st.success('**Car**: Suzuki Cappuccino')
        st.success('**Home Course**: いろは坂 (Irohazaka)')
        st.markdown('> **Discription**: Brain of RD. In 2009-2010, `YOH` was one of the strongest driver, famous in the D5 racing world in Mianyang. He and his red Cappuccino held the Inohazaka downhill record for a long time, `YOH` loves Go in his spare time,  he now has a cute daughter who .')
    

st.header('Group Photo')
# st.dataframe(data)
image = Image.open('./data/4drivers.jpg')
st.image(image, caption='Tong JYL TIGA XIAO', use_column_width=True)

# GPT Part
st.header("Any advice for this page?")

comment = st.text_area('')
enter = st.button('Enter')

if enter:
    st.markdown('Hello, this is ChatGPT!')
else:
    st.write("We have gpt-3.5-turbo to be a chatbot.")



