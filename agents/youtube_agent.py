from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from config.settings import MODEL_NAME
from utils.prompt_templates import YOUTUBE_PROMPT
from utils.youtube_search import search_youtube_video


class YoutubeAgent:

    def generate(self, text, topic):

        llm = ChatGroq(model=MODEL_NAME)

        prompt = PromptTemplate.from_template(YOUTUBE_PROMPT)

        chain = prompt | llm

        script = chain.invoke({"text": text}).content

        video = search_youtube_video(topic)

        return {
            "script": script,
            "video_title": video.get("title", "No video found"),
            "video_link": video.get("link", "")
        }