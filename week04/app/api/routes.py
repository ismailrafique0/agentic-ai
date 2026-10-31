from fastapi import (
    APIRouter,
    HTTPException,
)

from app.services import (
    AIService,
)

from app.services.classifier import (
    RuleClassifier,
)


router = APIRouter()


classifier = RuleClassifier()

ai_service = AIService(
    classifier
)


@router.get("/")
def root():

    return {
        "message": "AI Service is running",
        "version": "1.0.0",
    }


@router.post("/classify")
def classify(
    text: str,
):

    try:

        return ai_service.classify(
            text
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )