#Calorie Coach
import streamlit as st
import plotly.graph_objects as go

st.title("Calorie Coach")

def disp(b, sex, age, available_cals, goal, protein, carbohydrates, fat, activity_dict):

################################################ DISPLAY ########################################################

	col1, col11 = st.beta_columns([1, 3])
	with col1:
		st.write("Your BMR is: ")
		bmr = st.write(round(b + sex + goal))
	with col11:
		st.write("narrowly surviving...")

	col2, col22 = st.beta_columns([1, 3])
	with col2:
		st.write("Sedentary: ")
		st.write(activity_dict["Sedentary"])
	with col22:
		st.write("LAZY. Memento Mori people... get up and live.")

	col3, col33 = st.beta_columns([1, 3])
	with col3:
		st.write("Light: ")
		st.write(activity_dict["Light"])
	with col33:
		st.write("1 - 3 days light exercise")

	col4, col44 = st.beta_columns([1, 3])
	with col4:
		st.write("Moderate: ")
		st.write(activity_dict["Moderate"])
	with col44:
		st.write("3 - 5 days of moderate exercise")

	col5, col55 = st.beta_columns([1, 3])
	with col5:
		st.write("Very: ")
		st.write(activity_dict["Very"])
	with col55:
		st.write("daily vigorous exercise")

	col6, col66 = st.beta_columns([1, 3])
	with col6:
		st.write("Extremely: ")
		st.write(activity_dict["Extremely"])
	with col66:
		st.write("6 - 7 days vigorous exercise + highly physical work life")
	
	st.title("Your Caloric Intake: " + str(activity_dict[available_cals]))
	col7, col77 = st.beta_columns([1, 3])
	with col7:
		st.write("Available Calories: ")
	with col77:
		st.write(activity_dict[available_cals] - ((activity_dict[available_cals]*(protein/100)) + (activity_dict[available_cals]*(carbohydrates/100)) + (activity_dict[available_cals]*(fat/100))))
	col8, col88 = st.beta_columns([1, 3])
	with col8:
		st.write("Protein: ")
	with col88:
		st.write(str(((protein/100)*activity_dict[available_cals])//4) + "g")
	col9, col99 = st.beta_columns([1, 3])
	with col9:
		st.write("Carbohydrates: ")
	with col99:
		st.write(str(((carbohydrates/100)*activity_dict[available_cals])//4) + "g")
	col10, col1010 = st.beta_columns([1, 3])
	with col10:
		st.write("Fat: ")
	with col1010:
		st.write(str(((fat/100)*activity_dict[available_cals])//9) + "g")
	
	labels = ["Protein", "Carbohydrates", "Fat"]
	values = [protein, carbohydrates, fat]
	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	st.plotly_chart(fig, use_container_width=True)

############################################## SIDEBAR ###############################################
def bmr():
	################################################ SET BMR ########################################################

	sex = st.sidebar.radio("Sex:", ("Male", "Female"))
	if sex == "Male":
		sex = 5
	elif sex == "Female":
		sex = -161
	
	age = st.sidebar.slider("Age:", 1, 100)
	
	measurement = st.sidebar.radio("Measurement:", ("Metric", "Imperial"))
	if measurement == "Metric":
		weight = st.sidebar.slider("Weight (kg):", 1, 200)
		height = st.sidebar.slider("Height (cm):", 1, 300)
	if measurement == "Imperial":
		weight = (st.sidebar.slider("Weight (lbs):", 1, 300)) / 2.2
		height = (st.sidebar.slider("Height (in):", 1, 100)) * 2.54
	
	available_cals = st.sidebar.radio("Activity Level:", ("Sedentary", "Light", "Moderate", "Very", "Extremely"))
	
	goal = st.sidebar.radio("Goal:", ("Build", "Maintain", "Cut"))
	b = (10 * weight) + (6.25 * height) - (5 * age)
	bulk = 0
	cut = 0
	if goal == "Build":
		goal = st.sidebar.slider("Build:", (b * 0.03), (b * 0.15))             #added on to bmr
	elif goal == "Cut":
		goal = st.sidebar.slider("Cut:", -1 * (b * 0.15), -1 * (b * 0.1))      #subtracted from bmr
	else:
		goal = 0

	#Activity Modifiers
	activity_mod = [1.2, 1.375, 1.55, 1.725, 1.9] #sedentary, light, moderate, very, extreme
	activity_dict = {"Sedentary": round(((b + sex + goal) * activity_mod[0])), "Light": round(((b + sex + goal)
	 * activity_mod[1])), "Moderate": round(((b + sex + goal) * activity_mod[2])), "Very": round(((b + sex + goal)
	  * activity_mod[3])), "Extremely": round(((b + sex + goal) * activity_mod[4]))}
	
		
	protein = st.sidebar.slider("Protein", 0, 100, 25)
	carbohydrates = st.sidebar.slider("Carbohydrates", 0, 100, 55)
	fat = st.sidebar.slider("Fat", 0, 100, 25)

	disp(b, sex, age, available_cals, goal, protein, carbohydrates, fat, activity_dict)


bmr()

#Macros

#MENU examples
