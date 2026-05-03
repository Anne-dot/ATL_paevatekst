#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Configuration
Single source of truth for all settings and constants

Usage:
  Linux:   ./config.py  (or python3 config.py)
  Windows: python config.py
  GitHub Actions: python config.py
"""

import os
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# ENVIRONMENT VARIABLES
# =============================================================================

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

# =============================================================================
# GOOGLE DRIVE SETTINGS
# =============================================================================

# Google Drive API scope (read-only access)
DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Monthly document IDs (hardcoded - not sensitive data)
MONTHLY_DOC_IDS = {
    1: "10TiqvWIbjwyn1thrHKzVsIB5hGAzmziBwGhYBB59oGw",  # jaanuar
    2: "1-jCrmmKokn8uRK4AxKJdmKxzh2O07bRElO2KzOcyQ6c",  # veebruar
    3: "1cZEfpS_ywJYUTdp21Ypid9DM_JDabJ_kqocSwpKq870",  # märts
    4: "1uY9jNtRpkXOh4cBdl6L3NSUs8dQJB8ZznG-ORLloL1E",  # aprill
    5: "1uJx0csPvtALJgRxpY-VB44MX60Q5i-93DQPtuPgJnzc",  # mai
    6: "1gpDpZJMmqFyhWrB1_aJQV3KuMwCE-RNYVLxvZGpMwFU",  # juuni
    7: "1dvOB_Q2PTHyKLCRp75ThYq2pHLyePDfsnLdLidh8aAY",  # juuli
    8: "16c4OVM9FvYV-3bZmAZbRujE8foMp6kMVSnGn6kteF1s",  # august
    9: "1yCANW0RlJaiPQk4gXq4sdCZtiv5qED3CGgIRKAPa0Ic",  # september
    10: "1cWhsG6s3w3E-fqCxnYwl7PnV1sfwP6E1wca68iuY0pg", # oktoober
    11: "1YqR1Ocx4uu8sS-EeTP9BFdBLSgHJ3yQDyU7R8jWkJ10", # november
    12: "19HPSVWEpWpjmBd8C3QVHkcq7P9wjf40mfWYDqo2qbAE", # detsember
}

# Estonian month names for date heading patterns
# Single source of truth - used by date_utils.py for both start and stop patterns
MONTH_NAMES = {
    1: "jaanuar", 2: "veebruar", 3: "märts", 4: "aprill",
    5: "mai", 6: "juuni", 7: "juuli", 8: "august",
    9: "september", 10: "oktoober", 11: "november", 12: "detsember",
}

# =============================================================================
# DATE AND TIME SETTINGS
# =============================================================================

# Estonian timezone
ESTONIA_TZ = ZoneInfo('Europe/Tallinn')

# =============================================================================
# DISCORD SETTINGS
# =============================================================================

# Discord message format template
MESSAGE_TEMPLATE = "{content}"

# =============================================================================
# LOGGING SETTINGS
# =============================================================================

# Simple console logging format
LOG_FORMAT = "[{timestamp}] {level}: {message}"

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================

def validate_config():
    """Validate that all required configuration is present"""
    errors = []
    
    if not DISCORD_WEBHOOK_URL:
        errors.append("DISCORD_WEBHOOK_URL environment variable not set")
       
    if errors:
        print("❌ Configuration errors:")
        for error in errors:
            print(f"   - {error}")
        return False
    
    print("✅ Configuration validation passed")
    return True

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_current_date_info():
    """Get current date information for Estonian timezone"""
    now = datetime.now(ESTONIA_TZ)
    return {
        'day': now.day,
        'month': now.month
    }

def get_current_month_doc_id():
    """Get the Google Drive document ID for current month"""
    current_month = datetime.now(ESTONIA_TZ).month
    return MONTHLY_DOC_IDS.get(current_month)

if __name__ == "__main__":
    # Test configuration when run directly
    print("🔧 Testing ATL Bot Configuration...")
    
    date_info = get_current_date_info()
    print(f"📅 Current day: {date_info['day']}, month: {date_info['month']}")
    print(f"🔗 Current month doc ID: {get_current_month_doc_id()}")
    
    validate_config()