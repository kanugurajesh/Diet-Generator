import streamlit as st
from generate_diet import generate_diet

st.title('Diet Generator')
gender = st.selectbox('What is your Gender?', ['Male', 'Female'])
age = st.number_input('What is your Age?', min_value=1, max_value=120)
body_comp = st.selectbox("What is your Body Composition?", ["Lean", "Average", "Overweight", "Obese"])
activity = st.selectbox("What is your Activity Level?", ["Sedentary", "Light", "Moderate", "Active", "Athlete"])
generate_button = st.button('Generate')

if generate_button:
	print('Generating Diet...')
	with st.spinner("Generating your diet plan..."):
		try:
			diet = generate_diet(age=age, body_comp=body_comp, activity_level=activity, gender=gender)
			st.download_button("Download Plan", data=diet.content, file_name="diet_plan.txt")
			st.markdown(diet.content)
		except Exception as e:
			st.error("Something Went wrong. Please try again.")
			st.text(str(e))