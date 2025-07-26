# Estonian ACA Daily Meditation Bot

Automated system for posting daily meditations to the Estonian Adult Children of Alcoholics (ACA) Discord group.

## Overview

This project automates the daily posting of meditation content to help support the Estonian ACA community. Each morning, the system automatically posts:
- Daily meditation text
- Meditation audio file (when available)

## Features

- **Automated Scheduling**: Posts meditation content every morning without manual intervention
- **Discord Integration**: Seamlessly posts to the designated Discord channel
- **Multi-format Support**: Handles both text and audio meditation content
- **Reliability**: Designed to run consistently without human oversight

## Project Goals

1. Provide consistent daily meditation content to the Estonian ACA community
2. Eliminate the need for manual posting
3. Ensure reliable delivery of both text and audio content
4. Support the recovery journey of ACA members through regular spiritual practice

## Chosen Architecture

**Final Implementation:**
- **✅ Discord Webhook**: Simple posting mechanism (KISS principle)
- **✅ GitHub Actions**: Cloud-based scheduling and execution
- **✅ Google Drive API**: Direct access to ATL meditation documents
- **✅ Document IDs**: 12 monthly document IDs hardcoded for reliability

See [discordi_päevatekstide_automaatse_postitamise_plaan.md](discordi_päevatekstide_automaatse_postitamise_plaan.md) for detailed planning decisions.

## Getting Started

See [SETUP.md](SETUP.md) for detailed setup instructions.

## GitHub Secrets Configuration

### Required Secrets
The following secrets must be configured in GitHub repository settings → Secrets and variables → Actions:

1. **`DISCORD_WEBHOOK_URL`** *(secret)*
   - Discord webhook URL for posting messages
   - Format: `https://discord.com/api/webhooks/...`
   - How to get: Discord server settings → Integrations → Webhooks

2. **`GOOGLE_CREDENTIALS`** *(secret)*  
   - Google Service Account JSON credentials (entire file content)
   - Format: Complete JSON object as string
   - How to get: Google Cloud Console → Service Accounts → Create Key

### Document Configuration
Monthly meditation document IDs are configured in `config.py` - no secrets required since document IDs are not sensitive data.

### Environment Variables
- **Local development**: Uses `atl-paevamotted-*.json` file for Google auth
- **GitHub Actions**: Uses `GOOGLE_CREDENTIALS` environment variable from secret

## Current Status

**✅ Completed:**
- Discord webhook setup and testing
- Google Drive API connection established  
- Complete modular Python system (5 files)
- GitHub Actions workflow with dual authentication
- Text parsing and daily extraction logic
- GitHub secrets and environment variables configured
- Service account has access to ATL meditation documents
- Technical documentation (SETUP.md, TROUBLESHOOTING.md, HANDOVER.md)

**🔄 In Progress:**
- Extended testing with production data
- Text formatting improvements

**Progress:** 8/10 issues completed (80%)

## Contributing

Contributions are welcome to improve the automation system and enhance the experience for the Estonian ACA community.

## License

(To be determined)

## Documentation

- **[SETUP.md](SETUP.md)** - Complete setup guide
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Problem solving guide  
- **[HANDOVER.md](HANDOVER.md)** - Project handover instructions

## Support

For questions or issues related to this automation system:
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) first
- Contact: ruusmann@gmail.com
- Open an issue in this repository