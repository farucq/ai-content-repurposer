import streamlit as st

from modules.parser import ContentParser
from modules.semantic_analyzer import SemanticAnalyzer
from modules.planner import ContentPlanner
from modules.reviewer import QualityReviewer

from agents.linkedin_agent import LinkedInAgent
from agents.twitter_agent import TwitterAgent
from agents.youtube_agent import YoutubeAgent
from agents.newsletter_agent import NewsletterAgent


st.title("AI Content Repurposing Engine")


url = st.text_input("Blog URL")

text = st.text_area("Or paste blog content")


generate = st.button("Generate Content")


if generate:

    parser = ContentParser()

    if url:
        content = parser.parse_url(url)
    else:
        content = parser.parse_text(text)

    analyzer = SemanticAnalyzer()

    semantic = analyzer.analyze(content)

    planner = ContentPlanner()

    planner.plan(semantic)

    linkedin = LinkedInAgent().generate(content["text"])

    twitter = TwitterAgent().generate(content["text"])

    youtube = YoutubeAgent().generate(
    content["text"],
    semantic["topic"]
)

    newsletter = NewsletterAgent().generate(content["text"])

    reviewer = QualityReviewer()

    st.subheader("LinkedIn Post")
    st.write(reviewer.review(linkedin))

    st.subheader("Twitter Thread")
    st.write(reviewer.review(twitter))

    st.subheader("YouTube Script")
    st.write(youtube["script"])
    st.subheader("Recommended YouTube Video")
    st.write(youtube.get("video_title", "No video found"))
    video_link = youtube.get("video_link", "")
    if video_link:
        st.video(video_link)
    else:
        st.markdown(f"[Search YouTube for related videos]({video_link})")

    st.subheader("Newsletter Summary")
    st.write(reviewer.review(newsletter))