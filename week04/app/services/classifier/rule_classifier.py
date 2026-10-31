class RuleClassifier:
    """Simple classifier implementation."""

    def classify(
        self,
        text: str,
    ) -> str:

        text = text.strip().lower()

        if not text:
            raise ValueError(
                "Text cannot be empty."
            )

        if "password" in text:
            return "account"

        if ("fee" in text or "voucher" in text or "payment" in text):
            return "finance"

        if ("server" in text or "api" in text):
            return "technical"

        if "admission" in text:
            return "admission"

        if ("exam" in text or "test" in text or "assignment" in text):
            return "exam/test/assignment"

        if ("scholarship" in text or "discount" in text):
            return "scholarship"

        return "other"

if __name__ == "__main__":

    classifier = RuleClassifier()

    print(
        classifier.classify(
            "I forgot my password"
        )
    )

    print(
        classifier.classify(
            "My fee payment is missing"
        )
    )

    print(
        classifier.classify(
            "The API server is down"
        )
    )