#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Google Drive Client
Simple functions for reading meditation documents

Usage:
  Linux:   python3 drive_client.py
  Windows: python drive_client.py
"""

import json
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import DRIVE_SCOPES, get_current_month_doc_id

def create_google_drive_service():
    """Create Google Drive API service with authentication"""
    
    # Try environment variable first (GitHub Actions)
    google_creds_env = os.getenv('GOOGLE_CREDENTIALS')
    if google_creds_env:
        print("🔑 Using GOOGLE_CREDENTIALS environment variable")
        credentials_info = json.loads(google_creds_env)
        credentials = service_account.Credentials.from_service_account_info(
            credentials_info, scopes=DRIVE_SCOPES
        )
    else:
        # Fall back to auto-find JSON file (local development)
        print("🔍 Looking for local JSON credentials file...")
        json_file = None
        for file in os.listdir('.'):
            if file.startswith('atl-paevamotted-') and file.endswith('.json'):
                json_file = file
                break
        
        if not json_file:
            raise ValueError("No authentication found: set GOOGLE_CREDENTIALS env var or place atl-paevamotted-*.json file in directory")
        
        print(f"🔑 Using local JSON file: {json_file}")
        credentials = service_account.Credentials.from_service_account_file(
            json_file, scopes=DRIVE_SCOPES
        )
    
    service = build('drive', 'v3', credentials=credentials)
    print("✅ Google Drive API service created")
    return service

def download_document_as_text(service, document_id):
    """Download Google Drive document content as plain text"""
    print(f"📄 Downloading document: {document_id}")
    
    content = service.files().export(
        fileId=document_id, 
        mimeType='text/plain'
    ).execute()
    
    text = content.decode('utf-8')
    print(f"✅ Document downloaded ({len(text)} characters)")
    return text

def get_current_month_meditation_text():
    """Get meditation text for current month"""
    current_doc_id = get_current_month_doc_id()
    
    if not current_doc_id:
        raise ValueError("No document ID found for current month")
    
    print(f"📅 Getting current month meditation text...")
    
    service = create_google_drive_service()
    content = download_document_as_text(service, current_doc_id)
    
    return content

# =============================================================================
# TESTING
# =============================================================================

if __name__ == "__main__":
    """Test drive client functions"""
    print("🔧 Testing ATL Drive Client...")
    
    try:
        content = get_current_month_meditation_text()
        
        # Show first 40 lines
        lines = content.split('\n')[:40]
        print(f"📖 First 40 lines:")
        for i, line in enumerate(lines, 1):
            display_line = line.strip() if line.strip() else "(empty line)"
            print(f"   {i:2d}: {display_line}")
        
        print(f"\n🎉 Drive client test successful!")
        
    except Exception as e:
        print(f"💥 Drive client test failed: {e}")