from langchain.llms import OpenAI
from langchain import PromptTemplate
import streamlit as st

# Set the title of the Streamlit application
st.title("Email4Me")

# Request user to input OpenAPI API Key
api_key = st.sidebar.text_input("Enter OpenAPI API Key", type="password")


st.sidebar.markdown("## Follow me at:")
st.sidebar.markdown("www.linkedin.com/company/siri-analytics/")
st.sidebar.markdown("Book my consulting services")
st.sidebar.markdown("https://calendly.com/d/y7f-4hz-sj6/consulting-call")


if api_key:
    try:
        your_name = st.text_input("Enter your name", "Email4Me")

        dummy = """Dear Email4Me,
I hope this message finds you well. 
We are excited about the prospect of collaborating with you to build our AI business,
and are considering engaging your services for this purpose.

We are looking to kick-start this project as early as tomorrow. 
I would greatly appreciate it if you could get back to us at your earliest convenience,
to discuss the specifics and confirm your availability.

Looking forward to your prompt response.

Best regards,
Best Client
"""

        content = st.text_area("Enter email content ", value=dummy, height=400)

        # Note, the default model is already 'text-davinci-003',
        # but I call it out here explicitly so you know where to change it later if you want
        llm = OpenAI(
            temperature=0, model_name="text-davinci-003", openai_api_key=api_key
        )

        # Create our template
        template1 = """
        %INSTRUCTIONS:
        My name is {name}. Please answer email for me using the following piece of text.
        Respond in a manner that I can get hire quickly.

        %TEXT:
        {email_content}
        """

        # Create a LangChain prompt template that we can insert values to later
        prompt = PromptTemplate(
            input_variables=["name", "email_content"],
            template=template1,
        )

        final_prompt = prompt.format(name=your_name, email_content=content)

        if st.button("Reply Email"):
            if your_name and content:
                # While the answer is being generated, show a loading spinner
                with st.spinner("Generating Terraform..."):
                    output = llm(final_prompt)
                    st.write(output)
                    # print ("output")

            else:
                # Display a warning if the user hasn't entered a question
                st.warning("Please enter information")

    except Exception as e:
        st.error(f"Please enter a valid OpenAPI API Key! Your Input: {api_key}")

else:
    # Display a warning if the user hasn't entered an API key
    st.warning("Please enter OpenAPI API Key!")
