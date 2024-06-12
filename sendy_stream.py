import streamlit as st


# Logo
#st.image("e22cfe4b-d270-41f0-9f11-7523cc9fcc0b.jpg", width=300) 

st.title("Sendy Delivery Time Predictor")


def main():
    # Create a button to go to the About page
    if st.sidebar.button("About"):
        show_about()

def show_about():
    st.write("""<p style='font-size:35px;'>ABOUT</p>
            <p style='font-size:20px;'>This platform assists in predicting the time at which a package will be delivered to its destination based on several factors such as :</p>
            <p style='font-size:20px;'>1. The type of vehicle used</p>
            <p style='font-size:20px;'>2. The platform used to place the order</p>
            <p style='font-size:20px;'>3. Whether it was placed by a business or personal user</p>
            <p style='font-size:20px;'>4. The day and the weekday on which the delivery was picked</p>""", unsafe_allow_html=True)
    # Add a button to go back to the main page
    if st.button("Go back to main page"):
        main()

if __name__ == "__main__":
    main()

# # def show_about():
#     st.write("""<p style='font-size:35px;'>ABOUT</p>
#             <p style='font-size:20px;'>This platform assists in predicting the time at which a package will be delivered to its destination based on several factors such as :</p>
#             <p style='font-size:20px;'>1. The type of vehicle used</p>
#             <p style='font-size:20px;'>2. The platform used to place the order</p>
#             <p style='font-size:20px;'>3. Whether it was placed by a business or personal user</p>
#             <p style='font-size:20px;'>4. The day and the weekday on which the delivery was picked</p>""", unsafe_allow_html=True)
    


# if st.sidebar.button("About"):
#     show_about()

# #You can add more buttons or functionality here for other pages or actions

# if st.button("Exit"):
#     pass
# if st.sidebar.button('About'):
#         about_clicked = not about_clicked  # Toggle the button state






# """<p style='font-size:35px;'>ABOUT</p>
#             <p style='font-size:20px;'>This platform assists in predicting the time at which a package will be delivered to its destination based on several factors such as :</p>
#             <p style='font-size:20px;'>1. The type of vehicle used</p>
#             <p style='font-size:20px;'>2. The platform used to place the order</p>
#             <p style='font-size:20px;'>3. Whether it was placed by a business or personal user</p>
#             <p style='font-size:20px;'>4. The day and the weekday on which the delivery was picked</p>"""
#Customize background
 
#background_image = "https://miro.medium.com/v2/resize:fit:1400/1*k75ZPcME9JkK6sT1gwvj6w.jpeg"
    
# CSS to dim the background image
    
# background_css = f"""
#     <style>
#         .stApp {{
#             background: url("{background_image}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         .stContent {{
#             background-color: rgba(0, 0, 0, 5.5); 
#         }}
#     </style>
#     """
# st.markdown(background_css, unsafe_allow_html=True)



primaryColor = "#0000FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F0F0"
textColor = "#000000"

# Customize background 
background_image_url ="data:image/jpeg;base64,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"
background_css = f"""
    <style>
        .stApp {{
            background: url("{background_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stContent {{
            background-color: rgba(0, 0, 0, 5.5); 
        }}
    </style>
"""
st.markdown(background_css, unsafe_allow_html=True)

