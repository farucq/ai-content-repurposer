class QualityReviewer:

    def review(self, text):

        text = text.replace("  ", " ")

        return text.strip()