from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

def generate_diet(age, gender, body_comp, activity_level):
	# docstring
	"""
	Generate a personalized diet recommendation based on user input.

    	Parameters:
	    - age (int): The user's age in years
	    - gender (str): The user's gender (e.g., 'Male', 'Female')
	    - body_comp (str): Body composition category (e.g., 'Lean', 'Overweight')
	    - activity_level (str): Physical activity level (e.g., 'Sedentary', 'Athlete')
	
	    Returns:
	    - A string with the final diet recommendation (to be implemented later)
	"""
	# template to feed into PromptTemplate
	template = """
	You are a nutrition expert tasked with recommending the most relevant aspects of a person's diet based on their core 
	attributes. Given the following details about a person:
	
	Age: {age}
	Sex/Gender: {gender}
	Body Composition: {body_comp}
	Activity Level: {activity_level}
	
	Output a list of key diet aspects this person should focus on. Cover:
	
	Macronutrient balance
	Caloric needs
	Timing/frequency of meals
	Food types to prioritize or avoid
	Supplement needs (if applicable)
	Any special recommendations based on their conditions/preferences
	
	Keep the recommendations concise, practical, and personalized to the attributes given. Avoid generic advice.
	    """
	# initializing PromptTemplate
	prompt = PromptTemplate(
		template=template,
		input_variables=["age", "gender", "body_comp", "activity_level"],
	)
	
	# initializing the llm (could be replaced with openai or other llms)
	llm = ChatOllama(model="llama3.2")

	# chaining prompt into the llm
	diet_chain = prompt | llm

	# invoking chain with relevant inputs
	res = diet_chain.invoke(
		input={
			"age": age,
			"gender": gender,
			"body_comp": body_comp,
			"activity_level": activity_level,
		}
	)
	return res

if __name__ == "__main__":
    print("Generating Diet...")
    result = generate_diet(19, 'Male', '25% Fat', '5 times a weak')
    print(result.content)