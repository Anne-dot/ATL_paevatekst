#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Date Utilities
Simple functions for date handling and finding daily meditation text

Usage:
  Linux:   python3 date_utils.py
  Windows: python date_utils.py
"""

import re
from config import get_current_date_info

def create_heading_pattern_for_today():
    """Create regex pattern to find today's heading in document"""
    date_info = get_current_date_info()
    current_day = date_info['day']
    
    # Pattern matches: "## 24." or "## 24 " (with optional space/period)
    pattern = rf"^{current_day}[\.\s]"
    print(f"🔍 Looking for heading pattern: {current_day}.")
    
    return pattern

def find_todays_meditation_text(document_content):
    """Extract today's meditation text from document content"""
    lines = document_content.split('\n')
    heading_pattern = create_heading_pattern_for_today()
    
    # Find the line with today's heading
    start_line = None
    for i, line in enumerate(lines):
        if re.match(heading_pattern, line.strip()):
            start_line = i
            print(f"✅ Found today's heading at line {i + 1}: {line.strip()}")
            break
    
    if start_line is None:
        date_info = get_current_date_info()
        raise ValueError(f"Could not find heading for day {date_info['day']} in document")
    
    # Collect text until next heading (## XX) or end of document
    meditation_lines = []
    for i in range(start_line + 1, len(lines)):
        line = lines[i].strip()
        
        # Stop if we hit another heading
        if re.match(r"^\d+[\.\s]", line):
            print(f"📄 Found next heading at line {i + 1}, stopping collection")
            break
        
        # Add non-empty lines to meditation text
        if line:
            meditation_lines.append(line)
    
    if not meditation_lines:
        raise ValueError("No meditation text found after today's heading")
    
    # Join lines with newlines
    meditation_text = '\n'.join(meditation_lines)
    print(f"✅ Extracted meditation text ({len(meditation_text)} characters)")
    
    return meditation_text

def get_todays_meditation_from_document(document_content):
    """Get today's complete meditation text from document"""
    print(f"📅 Extracting today's meditation text...")
    
    meditation_text = find_todays_meditation_text(document_content)
    
    return meditation_text

# =============================================================================
# TESTING
# =============================================================================

if __name__ == "__main__":
    """Test date utilities functions"""
    print("🔧 Testing ATL Date Utilities...")
    
    try:
        # Test current date info
        date_info = get_current_date_info()
        print(f"📅 Current date info: day {date_info['day']}, month {date_info['month']}")
        
        # Test heading pattern creation
        pattern = create_heading_pattern_for_today()
        print(f"🔍 Today's heading pattern: {pattern}")
        
        # Test with sample document content
        sample_content = """Some header text

24. 
Yesterday's meditation text here...
This continues on multiple lines.

25.
Today's meditation text here...
This is the text we want to extract.
It can span multiple lines too.

26.
Tomorrow's text starts here...
"""
        
        if date_info['day'] == 25:  # Only test if today is actually 25th
            meditation_text = get_todays_meditation_from_document(sample_content)
            print(f"📖 Extracted meditation text:")
            print(f"   {meditation_text}")
        else:
            print(f"ℹ️  Skipping text extraction test (today is {date_info['day']}, not 24)")
        
        print("🎉 Date utilities test successful!")
        
    except Exception as e:
        print(f"💥 Date utilities test failed: {e}")