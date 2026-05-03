#!/usr/bin/env python3
"""
ATL Päevamõtete Bot - Date Utilities
Simple functions for date handling and finding daily meditation text

Usage:
  Linux:   python3 date_utils.py
  Windows: python date_utils.py
"""

import re
from config import get_current_date_info, MONTH_NAMES

def create_heading_pattern_for_today():
    """Create regex pattern to find today's heading: 'N. kuunimi'"""
    date_info = get_current_date_info()
    current_day = date_info['day']
    current_month_name = MONTH_NAMES[date_info['month']]

    # Strict match: day (with optional leading zero) + period + optional space + current month name
    pattern = rf"^0?{current_day}\.\s*{current_month_name}\b"
    print(f"🔍 Looking for heading pattern: {current_day}. {current_month_name}")

    return pattern

def find_todays_meditation_text(document_content):
    """Extract today's meditation text from document content with formatting"""
    lines = document_content.split('\n')
    heading_pattern = create_heading_pattern_for_today()
    
    # Find the line with today's heading
    start_line = None
    heading_line = None
    for i, line in enumerate(lines):
        if re.match(heading_pattern, line.strip()):
            start_line = i
            heading_line = line.strip()
            print(f"✅ Found today's heading at line {i + 1}: {heading_line}")
            break
    
    if start_line is None:
        date_info = get_current_date_info()
        raise ValueError(f"Could not find heading for day {date_info['day']} in document")
    
    # Collect text until next heading (## XX) or end of document
    meditation_lines = []
    
    for i in range(start_line + 1, len(lines)):
        line = lines[i].strip()
        
        # Stop if we hit another date heading (day + any month name)
        all_months = "|".join(MONTH_NAMES.values())
        date_heading_pattern = rf"^\d{{1,2}}\.\s*(?:{all_months})\b"
        if re.match(date_heading_pattern, line, re.IGNORECASE):
            print(f"📄 Found next date heading at line {i + 1}, stopping collection")
            break
        
        # Add line to meditation text (keep empty lines for paragraph breaks)
        meditation_lines.append(line)
    
    if not meditation_lines:
        raise ValueError("No meditation text found after today's heading")
    
    # Remove leading/trailing empty lines
    while meditation_lines and not meditation_lines[0]:
        meditation_lines.pop(0)
    while meditation_lines and not meditation_lines[-1]:
        meditation_lines.pop()
    
    # Format first line (title) as bold, rest as normal
    if meditation_lines:
        # First non-empty line becomes the title
        title = f"**{meditation_lines[0]}**"
        content_lines = meditation_lines[1:]

        # Remove any leading empty lines from content (Drive may have multiple)
        while content_lines and not content_lines[0]:
            content_lines.pop(0)

        # Join content with preserved line breaks
        raw_content = '\n'.join(content_lines)
        # Normalize all paragraph breaks to exactly 1 blank line for Discord readability
        # Replace any sequence of 1+ newlines with exactly 2 newlines (1 blank line)
        formatted_content = re.sub(r'\n+', '\n\n', raw_content)

        # Format with Discord markdown
        # Structure: date, title, 1 blank line, content
        formatted_date = f"📅 **{heading_line}**"
        formatted_text = f"{formatted_date}\n{title}\n\n{formatted_content}"
    else:
        # Fallback if no content
        formatted_date = f"📅 **{heading_line}**"
        formatted_text = formatted_date
    
    print(f"✅ Extracted and formatted meditation text ({len(formatted_text)} characters)")
    
    return formatted_text

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