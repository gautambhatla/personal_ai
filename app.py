import chatbot
import hydralit_components as hc
import streamlit as st 
# Set configuration 
st.set_page_config( 
    page_title="Personal AI",
    # page_icon = "", 
    layout="wide",
    initial_sidebar_state='collapsed', 
) 

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

menu_data = [
    {'id': 'id1', 'label': 'Chatbot', 'icon': ''},
    # {'id': 'id2', 'label': 'Coming soon', 'icon': ''},
    # {'id': 'id3', 'label': 'Coming soon', 'icon': ''},
]

over_theme = {'txc_inactive': '#000000', 'menu_background': '#00000', 'txc_active': '#FFFFFF', 'option_active': '#367ea8'}

menu_params = {
    'menu_definition': menu_data,
    'override_theme': over_theme,
    'sticky_nav': True,
    'sticky_mode': "pinned",
    'use_animation': False,
    'hide_streamlit_markers': True,
}

# menu_id = hc.nav_bar(**menu_params)

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='not-jumpy', #jumpy or not-jumpy, but sticky or pinned
    use_animation=False,
)

if menu_id.strip() == 'id1':
    chatbot.main_page()
if menu_id.strip() == 'id2':
    pass