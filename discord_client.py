#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Discord Client
Simple function for posting meditation messages to Discord

Usage:
  Linux:   python3 discord_client.py
  Windows: python discord_client.py
"""

import requests
from config import DISCORD_WEBHOOK_URL, MESSAGE_TEMPLATE

def post_message_to_discord(content):
    """Post meditation message to Discord via webhook"""
    if not DISCORD_WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK_URL environment variable not set")
    
    # Format message using template
    formatted_message = MESSAGE_TEMPLATE.format(content=content)
    
    # Prepare webhook payload
    payload = {
        "content": formatted_message
    }
    
    print(f"📱 Posting message to Discord...")
    
    # Send POST request to webhook
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    
    # Check if successful
    if response.status_code == 204:
        print("✅ Message posted successfully to Discord")
    else:
        print(f"❌ Failed to post message: {response.status_code}")
        raise RuntimeError(f"Discord webhook failed: {response.status_code} - {response.text}")

# =============================================================================
# TESTING
# =============================================================================

if __name__ == "__main__":
    """Test Discord client function"""
    print("🔧 Testing ATL Discord Client...")
    
    try:
        # Test message
        test_content = """**📅 24. juuli - Tänane mõte**

Tänane inspiratsioon tekst siin...
See on testimiseks mõeldud sõnum.

✨ _ATL päevamõtted_"""
        
        post_message_to_discord(test_content)
        print("🎉 Discord client test successful!")
        
    except Exception as e:
        print(f"💥 Discord client test failed: {e}")