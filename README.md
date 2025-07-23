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
- **✅ Hardcoded URLs**: 12 monthly document URLs for reliability

See [discordi_päevatekstide_automaatse_postitamise_plaan.md](discordi_päevatekstide_automaatse_postitamise_plaan.md) for detailed planning decisions.

## Getting Started

See [SETUP.md](SETUP.md) for detailed setup instructions.

## Current Status

**✅ Completed:**
- Discord webhook setup and testing
- Google Drive API connection established
- GitHub secrets configured
- Service account has access to ATL meditation documents

**🔄 In Progress:**
- Python script development
- Text parsing logic
- GitHub Actions automation

**Progress:** 2/9 issues completed (22%)

## Contributing

Contributions are welcome to improve the automation system and enhance the experience for the Estonian ACA community.

## License

(To be determined)

## Support

For questions or issues related to this automation system, please open an issue in this repository.