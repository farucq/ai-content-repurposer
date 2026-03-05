class ContentPlanner:

    def plan(self, semantic_data):

        return {

            "linkedin_tone": "professional thought leadership",

            "twitter_tone": "engaging concise",

            "youtube_tone": "educational storytelling",

            "newsletter_tone": "informative digest",

            "highlights": semantic_data["key_points"]
        }