# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## MANDATORY: Read Global Instructions First

**Before starting ANY work, you MUST:**

1. Read ALL files in `/home/d0021/Automation/05-ai-instructions/` directory
2. Read them WITHOUT optimization (read full files, not summaries)
3. Follow those instructions ALWAYS and CONTINUOUSLY throughout the session
4. Those instructions are NON-NEGOTIABLE and apply to ALL work in this repository

Global instruction files include:
- `instructions.md` - Core working principles, coding standards, documentation rules, response format requirements
- `eesti_keele_juhend.txt` - Estonian language usage rules

## Project Overview

Automated Discord bot for posting daily ACA (Adult Children of Alcoholics) meditations to Estonian ACA Discord group.

**Status:** ✅ Production - Running daily at 6:00 AM Estonian time

## Core Functionality

Posts daily meditation content automatically:
- Daily meditation text (Estonian)
- Audio file (when available)
- Runs via GitHub Actions (scheduled)
- Posts to Discord via webhooks

## Architecture

**Final Implementation:**
- Discord Webhook - Simple posting mechanism (KISS principle)
- GitHub Actions - Cloud-based scheduling and execution
- Google Drive API - Direct access to ATL meditation documents (12 monthly document IDs)
- Document IDs hardcoded for reliability

## Commands

### Development
```bash
# No local development commands - runs in GitHub Actions
```

### Testing
- **Manual test:** GitHub Actions → "Run workflow" button → Posts to test channel
- **Production:** Automatic daily run at 6:00 AM → Posts to production channel

## GitHub Secrets Configuration

Required secrets in repository settings → Actions:

1. **`DISCORD_WEBHOOK_URL`** - Production webhook (daily cron at 6:00 AM)
2. **`DISCORD_WEBHOOK_TEST_URL`** - Test webhook (manual "Run workflow")
3. **`GOOGLE_CREDENTIALS`** - Google Service Account JSON (entire file as string)

**Automatic webhook selection:**
- Scheduled run (cron) → uses production webhook
- Manual run → uses test webhook
- No manual secret switching required

## Project Structure

```
ATL_paevatekst/
├── .github/workflows/          # GitHub Actions workflow
├── config.py                   # Monthly document IDs
├── [5 modular Python files]    # Bot logic
├── README.md                   # Main documentation
├── SETUP.md                    # Setup instructions
├── TROUBLESHOOTING.md          # Problem solving
└── HANDOVER.md                 # Project handover docs
```

## Key Files

- **README.md** - Complete project overview and status
- **config.py** - Monthly Google Docs document IDs (not sensitive)
- **SETUP.md** - Setup guide
- **TROUBLESHOOTING.md** - Common issues and solutions

## Important Notes

- Service account has access to ATL meditation documents
- Audio player init uses Angular SPA (dynamic loading)
- Discord markdown formatting applied to meditation text
- Progress: 10/10 core issues completed (100%)

## Recent Fixes (Oct 2025)

- Fixed `ModuleNotFoundError: No module named 'packaging'`
- Automatic webhook selection (test vs production)
- No more manual secret switching for testing
