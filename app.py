import streamlit as st
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io

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

    # Download Section
    st.markdown("---")
    st.subheader("Download Generated Content Report")
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    topic_name = semantic["topic"].replace(" ", "_")[:20] if semantic.get("topic") else "content"
    
    # Create PDF report
    def create_pdf_report():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        
        # Get styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=20, spaceAfter=30, alignment=1)
        heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=16, spaceAfter=12, textColor='#2E86AB')
        normal_style = styles['Normal']
        
        # Build story
        story = []
        
        # Title
        story.append(Paragraph("AI Content Repurposing Report", title_style))
        story.append(Spacer(1, 20))
        
        # Metadata
        story.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
        story.append(Paragraph(f"<b>Original Topic:</b> {semantic.get('topic', 'N/A')}", normal_style))
        story.append(Paragraph(f"<b>Source:</b> {'URL: ' + url if url else 'Direct Text Input'}", normal_style))
        story.append(Spacer(1, 20))
        
        # Original Content
        story.append(Paragraph("<b>Original Content</b>", heading_style))
        story.append(Paragraph(f"<b>Title:</b> {content.get('title', 'N/A')}", normal_style))
        original_text = content['text'][:500] + ('...' if len(content['text']) > 500 else '')
        story.append(Paragraph(original_text, normal_style))
        story.append(Spacer(1, 20))
        
        # LinkedIn Post
        story.append(Paragraph("<b>LinkedIn Post</b>", heading_style))
        linkedin_text = reviewer.review(linkedin).replace('\n', '<br/>')
        story.append(Paragraph(linkedin_text, normal_style))
        story.append(Spacer(1, 20))
        
        # Twitter Thread
        story.append(Paragraph("<b>Twitter Thread</b>", heading_style))
        twitter_text = reviewer.review(twitter).replace('\n', '<br/>')
        story.append(Paragraph(twitter_text, normal_style))
        story.append(Spacer(1, 20))
        
        # YouTube Script
        story.append(Paragraph("<b>YouTube Script</b>", heading_style))
        youtube_text = youtube['script'].replace('\n', '<br/>')
        story.append(Paragraph(youtube_text, normal_style))
        story.append(Paragraph(f"<b>Recommended Video:</b> {youtube.get('video_title', 'No video found')}", normal_style))
        story.append(Paragraph(f"<b>Video Link:</b> {youtube.get('video_link', 'N/A')}", normal_style))
        story.append(Spacer(1, 20))
        
        # Newsletter
        story.append(Paragraph("<b>Newsletter Summary</b>", heading_style))
        newsletter_text = reviewer.review(newsletter).replace('\n', '<br/>')
        story.append(Paragraph(newsletter_text, normal_style))
        story.append(Spacer(1, 20))
        
        # Semantic Analysis
        story.append(Paragraph("<b>Semantic Analysis</b>", heading_style))
        story.append(Paragraph(f"<b>Topic:</b> {semantic.get('topic', 'N/A')}", normal_style))
        story.append(Paragraph("<b>Key Points:</b>", normal_style))
        for point in semantic.get('key_points', []):
            story.append(Paragraph(f"• {point}", normal_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    
    # PDF Download Button
    pdf_data = create_pdf_report()
    st.download_button(
        label="Download PDF Report",
        data=pdf_data,
        file_name=f"content_report_{topic_name}_{timestamp}.pdf",
        mime="application/pdf"
    )
