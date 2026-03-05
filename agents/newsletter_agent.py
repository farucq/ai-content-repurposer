from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from utils.prompt_templates import NEWSLETTER_PROMPT
from config.settings import MODEL_NAME


class NewsletterAgent:

    def generate(self, text):

        llm = ChatGroq(model=MODEL_NAME)

        prompt = PromptTemplate.from_template(NEWSLETTER_PROMPT)

        chain = prompt | llm

        return chain.invoke({"text": text}).content