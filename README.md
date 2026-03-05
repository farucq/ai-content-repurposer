# AI Content Repurposing Engine

A powerful Streamlit application that transforms your blog content into multiple formats using AI. Convert your articles into LinkedIn posts, Twitter threads, YouTube scripts, and newsletter summaries with intelligent content analysis and video recommendations.

## Features

- **Multi-format Content Generation**: Transform blog posts into LinkedIn posts, Twitter threads, YouTube scripts, and newsletters
- **Intelligent Content Analysis**: Uses semantic analysis to extract key topics and themes
- **YouTube Video Recommendations**: Finds relevant educational videos based on content topics
- **URL & Text Input**: Parse content from URLs or paste directly
- **Quality Review**: Built-in content quality assessment
- **Modern UI**: Clean, responsive Streamlit interface

## Architecture diagram

```bash
                        ┌───────────────────────┐
                        │      User Input       │
                        │  (Blog URL / Text)    │
                        └─────────────┬─────────┘
                                      │
                                      ▼
                        ┌───────────────────────┐
                        │   Content Parser      │
                        │ (Newspaper3k / BS4)   │
                        └─────────────┬─────────┘
                                      │
                                      ▼
                        ┌───────────────────────┐
                        │  Semantic Analyzer    │
                        │ Topic + Key Insights  │
                        │ Sentence Embeddings   │
                        └─────────────┬─────────┘
                                      │
                                      ▼
                        ┌───────────────────────┐
                        │  Content Planner      │
                        │ Tone + Strategy       │
                        │ Platform Selection    │
                        └─────────────┬─────────┘
                                      │
                                      ▼
                ┌───────────────────────────────────────────┐
                │        Platform Generation Agents         │
                │                                           │
                │  ┌──────────────┐   ┌──────────────┐      │
                │  │ LinkedIn     │   │ Twitter      │      │
                │  │ Generator    │   │ Thread Gen   │      │
                │  └──────────────┘   └──────────────┘      │
                │                                           │
                │  ┌──────────────┐   ┌──────────────┐      │
                │  │ YouTube      │   │ Newsletter   │      │
                │  │ Script Gen   │   │ Summary Gen  │      │
                │  └──────────────┘   └──────────────┘      │
                └───────────────────────┬───────────────────┘
                                        │
                                        ▼
                        ┌─────────────────────────┐
                        │   Quality Reviewer      │
                        │ Tone & Readability      │
                        │ Redundancy Removal      │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │  YouTube Video Search   │
                        │ Topic-based Video Match │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │      Streamlit UI       │
                        │ Display + Download      │
                        └─────────────────────────┘
```

## Tech Stack

- **Backend**: Python
- **AI/ML**: LangChain, Groq API, Sentence Transformers
- **Web Scraping**: Newspaper3k, BeautifulSoup4
- **Vector Storage**: ChromaDB
- **Frontend**: Streamlit
- **Video Search**: Custom YouTube search implementation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/farucq/ai-content-repurposer.git
cd ai-content-repurposer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file with your Groq API key
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Input Content**: 
   - Enter a blog URL to automatically parse the content
   - Or paste blog text directly into the text area

2. **Generate Content**: Click "Generate Content" to transform your blog into multiple formats

3. **Review Results**: 
   - LinkedIn post with professional tone
   - Twitter thread with engaging format
   - YouTube script with recommended videos
   - Newsletter summary with key insights

## Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for AI content generation
- `MODEL_NAME`: AI model to use (default: "llama-3.3-70b-versatile")

### Settings
Configure AI models and parameters in `config/settings.py`:
```python
MODEL_NAME = "llama-3.3-70b-versatile"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

## Project Structure

```
ai-content-repurposer/
├── app.py                 # Main Streamlit application
├── agents/                # Content generation agents
│   ├── linkedin_agent.py
│   ├── twitter_agent.py
│   ├── youtube_agent.py
│   └── newsletter_agent.py
├── modules/               # Core processing modules
│   ├── parser.py          # Content parsing
│   ├── semantic_analyzer.py # Content analysis
│   ├── planner.py         # Content planning
│   └── reviewer.py        # Quality review
├── utils/                 # Utility functions
│   ├── embeddings.py      # Text embeddings
│   ├── helpers.py         # Helper functions
│   ├── prompt_templates.py # AI prompts
│   └── youtube_search.py  # Video search
├── vectorstore/           # Vector storage
│   └── chroma_store.py
├── config/                # Configuration
│   └── settings.py
└── requirements.txt       # Dependencies
```

## API Keys Setup

1. Get a Groq API key from [Groq Console](https://console.groq.com/)
2. Create a `.env` file in the project root
3. Add your API key:
```
GROQ_API_KEY=gsk_your_api_key_here
```

## Features in Detail

### Content Parsing
- **URL Parsing**: Automatically extracts content from blog URLs using Newspaper3k
- **Fallback Scraping**: Uses BeautifulSoup4 as backup for difficult URLs
- **Text Cleaning**: Removes HTML tags and formats content properly

### Semantic Analysis
- **Topic Extraction**: Identifies main topics and keywords
- **Embedding Generation**: Creates vector representations for similarity matching
- **Key Point Extraction**: Identifies important sentences and insights

### Content Generation
- **LinkedIn**: Professional thought leadership posts (150-300 words)
- **Twitter**: Engaging threads (5-10 tweets, under 280 characters each)
- **YouTube**: Structured scripts with hook, explanation, insights, and CTA
- **Newsletter**: Informative summaries with bullet points and conclusions

### Video Recommendations
- **Smart Search**: Uses multiple search strategies with keyword extraction
- **Relevance Scoring**: Filters and ranks videos by educational value
- **Fallback Options**: Provides search links when direct video extraction fails
- **Add your API key**:
```
API_KEY=youtube_your_api_key_here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation
- Review the code comments

