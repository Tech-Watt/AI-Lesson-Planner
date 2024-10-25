import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st 


load_dotenv()

def LLM_Setup(prompt):
    model = ChatGroq(
        model = "llama-3.2-90b-text-preview",
        groq_api_key = os.getenv('key')
    )

    parser = StrOutputParser()
    output = model | parser 
    output = output.invoke(prompt)
    return output



subject = 'Science'

topic = 'The Solar System'

grade = 5

duration = 'one hour'

learning_objectives = 'student need to understand the solar system in a practical manner'
 
customization = 'make this lesson fun and intereactive'


# prompt = (
#                 f"Generate a detailed lesson plan for the subject of {subject} on the topic of {topic}. "
#                 f"This lesson is intended for {grade} students and will last for {duration}. "
#                 f"The following are the learning objectives: {learning_objectives}. Return the results as Markdown and don't return class size"
#                 f"This is how the user wants the plan to be customized {customization}."
#             )



# llm_output = LLM_Setup(prompt)
# print(llm_output)

st.title('AI Lesson Planner')

subject = st.text_input(label='Subject')
topic = st.text_input(label='Topic')
grade = st.text_input(label='Grade')
duration = st.text_input(label='Duration')
learning_objectives = st.text_area(label='Learning Objective')
customization = st.text_area(label='Customization')

if st.button('Generate Lesson Plan'):
    if not subject or not topic or not grade or not duration or not learning_objectives:
        st.warning('Please fill out all required fields before generating the lesson plan.')
    else:
        prompt = (
            f"Generate a detailed lesson plan for the subject of {subject} on the topic of {topic}. "
            f"This lesson is intended for {grade} students and will last for {duration}. "
            f"The following are the learning objectives: {learning_objectives}. "
            f"Return the results as Markdown and don't return class size. "
            f"This is how the user wants the plan to be customized: {customization}. return the result as Markdown"
        )
        llm_output = LLM_Setup(prompt)
        st.markdown(llm_output)