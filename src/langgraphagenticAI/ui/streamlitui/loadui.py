import streamlit as st
import os

from src.langgraphagenticAI.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="  "+ self.config.get_page_title(), layout="centered")
        st.header(" "+ self.config.get_page_title())

        with st.sidebar:
            #Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                #Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY", type="password")

                #Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(" Please enter your GROQ API key to proceed. Don't have ? Refer: https://console.groq.com/keys")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]= st.text_input("TAVILY_API_KEY", type="password")

                #validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY_API_KEY to proceed.")


            #if self.user_controls["selected_llm"]=="Openai":
              #  model_options = self.config.get_openai_model_options()
             #   self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)
               # self.user_controls["OPENAI_API_KEY"] = st.session_state["OPEANAI_API_KEY"] = st.text_input("API KEY", type = "password")

              #  if not self.user_controls["OPENAI_API_KEY"]:
              #     st.warning("Please enter your API key")
           # self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)
        return self.user_controls
