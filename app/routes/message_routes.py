from app.dependencies.message_dependencies import get_message_service, get_db
from app.models.message_model import CreateMessage, ResponseMessage
from app.services.message_service import MessageService

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

MESSAGE_NOT_FOUND = "Mensaje no encontrado"

router = APIRouter(tags=["Messages"], prefix="/messages")


@router.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "Bienvenido a la API Profesional con MySQL",
        "swagger": "http://127.0.0.1:8000/docs",
        "redoc": "http://127.0.0.1:8000/redoc",
    }


@router.get("/", response_model=List[ResponseMessage])
def get_all_messages(
    db: Session = Depends(get_db),
    service: MessageService = Depends(get_message_service),
):
    return service.get_all_messages(db)


@router.get("/{message_id}", response_model=ResponseMessage)
def get_message_by_id(
    message_id: int,
    db: Session = Depends(get_db),
    service: MessageService = Depends(get_message_service),
):
    message = service.get_message_by_id(db, message_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return message


@router.post("/", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_message(
    message: CreateMessage,
    db: Session = Depends(get_db),
    service: MessageService = Depends(get_message_service),
):
    return service.create_message(db, message)


@router.put("/{message_id}", response_model=ResponseMessage)
def update_message(
    message_id: int,
    message: CreateMessage,
    db: Session = Depends(get_db),
    service: MessageService = Depends(get_message_service),
):
    updated_message = service.update_message(db, message_id, message)
    if not updated_message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return updated_message


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(
    message_id: int,
    db: Session = Depends(get_db),
    service: MessageService = Depends(get_message_service),
):
    success = service.delete_message(db, message_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return None
