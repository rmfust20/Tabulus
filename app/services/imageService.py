import os
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContentSettings
from datetime import datetime, timedelta
from azure.storage.blob import (
    BlobServiceClient,
    generate_blob_sas,
    BlobSasPermissions,
)


ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_BYTES = 8 * 1024 * 1024  # 8 MB
MAX_FILES = 5

def blob_service_client() -> BlobServiceClient:
    account_name = "tabulususerimages"
    account_url = f"https://{account_name}.blob.core.windows.net"
    credential = DefaultAzureCredential()
    return BlobServiceClient(account_url=account_url, credential=credential)


async def upload_images(
    files: list[UploadFile] = File(..., description="Up to 5 image files"),
    game_night_id: int = 1
):
    if not files:
        raise HTTPException(400, "No files provided.")

    if len(files) > MAX_FILES:
        raise HTTPException(413, f"Too many files (max {MAX_FILES}).")

    container_name = "images"
    bsc = blob_service_client()

    uploaded: list[dict] = []

    for f in files:
        if f.content_type not in ALLOWED_CONTENT_TYPES:
            raise HTTPException(415, f"Unsupported content type: {f.content_type}")

        data = await f.read()
        if len(data) > MAX_BYTES:
            raise HTTPException(413, f"File too large (max {MAX_BYTES // (1024 * 1024)}MB).")

        ext = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp"}[f.content_type]
        blob_name = f"game_nights/{game_night_id}/{uuid.uuid4().hex}.{ext}"

        blob_client = bsc.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(
            data,
            overwrite=False,
            content_settings=ContentSettings(content_type=f.content_type),
        )

        uploaded.append({
            "filename": f.filename,
            "content_type": f.content_type,
            "blob_name": blob_name,
            "bytes": len(data),
        })

    return {"count": len(uploaded), "uploads": uploaded}

async def generate_sas_url(blob_name: str) -> str:
    ACCOUNT_NAME = "tabulususerimages"
    CONTAINER = "images"
    now = datetime.utcnow()
    delegation_key = bsc.get_user_delegation_key(
        key_start_time=now - timedelta(minutes=5),
        key_expiry_time=now + timedelta(hours=1),
    )

    sas = generate_blob_sas(
        account_name=ACCOUNT_NAME,
        container_name=CONTAINER,
        blob_name=blob_name,
        user_delegation_key=delegation_key,
        permission=BlobSasPermissions(read=True),
        expiry=now + timedelta(hours=1),
    )

    return {
        "url": f"https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER}/{blob_name}?{sas}"
    }




