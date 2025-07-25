#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Main Coordinator
Coordinates all modules to post daily meditation to Discord

Usage:
  Linux:   python3 main.py
  Windows: python main.py
"""

from drive_client import get_current_month_meditation_text
from date_utils import get_todays_meditation_from_document
from discord_client import post_message_to_discord
from config import validate_config, get_current_date_info

def run_daily_meditation_bot():
    """Run the complete daily meditation posting process"""
    print("🤖 Starting ATL Daily Meditation Bot...")
    
    # Step 1: Validate configuration
    print("\n📋 Step 1: Validating configuration...")
    if not validate_config():
        raise RuntimeError("Configuration validation failed")
    
    # Step 2: Get current date info
    print("\n📅 Step 2: Getting current date...")
    date_info = get_current_date_info()
    print(f"   Today: day {date_info['day']}, month {date_info['month']}")
    
    # Step 3: Read current month's document
    print("\n📄 Step 3: Reading current month's document...")
    document_content = get_current_month_meditation_text()
    
    # Step 4: Extract today's meditation text
    print("\n✂️ Step 4: Extracting today's meditation...")
    meditation_text = get_todays_meditation_from_document(document_content)
    
    # Step 5: Post to Discord
    print("\n📱 Step 5: Posting to Discord...")
    post_message_to_discord(meditation_text)
    
    print("\n🎉 Daily meditation posted successfully!")
    return True

def handle_bot_errors():
    """Handle any errors that occur during bot execution"""
    try:
        return run_daily_meditation_bot()
    except Exception as e:
        print(f"\n💥 Bot execution failed: {e}")
        print("❌ Daily meditation was not posted")
        return False

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """Main entry point for the bot"""
    print("=" * 50)
    print("🧘 ATL Päevamõtete Discord Bot")
    print("=" * 50)
    
    success = handle_bot_errors()
    
    if success:
        print("\n✅ Bot completed successfully")
        exit(0)
    else:
        print("\n❌ Bot failed - check errors above")
        exit(1)