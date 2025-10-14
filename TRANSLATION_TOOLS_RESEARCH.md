# Translation Tools and Collaboration Platforms Research

**Date:** 2025-10-14
**Context:** ACA/ATL Translation Project - Research for terminology-aware translation assistance

## Executive Summary

This research evaluates tools across four categories for an ACA (Adult Children of Alcoholics) translation project from English to Estonian. The project has 4 planned milestones: (1) Terminology Database, (2) Personal CLI assistant, (3) Estonian community web tool, (4) Universal multi-language platform.

**Key Findings:**
- **Best for Estonian Translation Quality:** DeepL (strong European language support)
- **Most Cost-Effective AI:** Claude API via prompt caching ($0.30-$3.00 per million tokens)
- **Best Free Platform for Small Teams:** Weblate (Libre plan for public open source projects)
- **Best Self-Hosted Option:** Weblate or Tolgee (both fully open source)
- **Most Affordable Paid Platform:** POEditor ($14.99/month for 3,000 strings)

---

## 1. AI Translation APIs

### 1.1 Claude API (Anthropic)

**URL:** https://docs.anthropic.com/docs/about-claude/pricing

**Key Features:**
- Large context window (100k+ tokens)
- Excellent for long documents
- Custom terminology support via prompt engineering
- Fast processing speed
- Prompt caching capability (up to 90% cost savings)

**Pricing (2025):**
- **Claude Haiku 3.5** (Most Economical): $0.25/$1.25 per million tokens (input/output)
- **Claude Sonnet 4.5** (Recommended): $3.00/$15.00 per million tokens
- **Claude Opus 4.1** (Most Intelligent): $15.00/$75.00 per million tokens
- **Batch Processing:** 50% discount
- **Prompt Caching:** Up to 90% savings on repeated context

**Free Tier:** None (pay-as-you-go)

**Estonian Language Support:** Good quality. Claude supports Estonian and performs well with European languages when given proper context.

**Custom Terminology:** Excellent. Can include terminology glossaries in prompts, supports detailed instructions for consistency.

**Pros for Small Community:**
- Pay only for what you use
- Excellent for specialized terminology with prompt engineering
- Very long documents in single pass
- Fast processing
- No subscription required

**Cons:**
- No free tier
- Requires API integration (technical setup)
- Quality depends on prompt engineering skill
- No built-in translation memory

**Estimated Cost Example:**
- 10,000 words (~15,000 tokens) translation: $0.045 input + $0.225 output = $0.27 using Sonnet 4.5
- With prompt caching for terminology: ~$0.03-0.10 per translation

---

### 1.2 OpenAI ChatGPT API

**URL:** https://platform.openai.com/docs/pricing

**Key Features:**
- GPT-4o model suitable for translation
- Good general translation quality
- Custom instructions support
- Wide language support

**Pricing (2025):**
- **GPT-4o** (Recommended): $3.00/$10.00 per million tokens (input/output)
- **GPT-3.5 Turbo** (Budget): $0.50/$1.50 per million tokens
- **GPT-4 Turbo:** $10.00/$30.00 per million tokens

**Free Tier:** None (pay-as-you-go)

**Estonian Language Support:** Good. Supports Estonian translation with generally good quality.

**Custom Terminology:** Good. Can include terminology in prompts, supports system messages for consistency.

**Pros for Small Community:**
- Pay-as-you-go pricing
- Well-documented API
- Good ecosystem and tools
- Competitive pricing with GPT-4o

**Cons:**
- Requires 3x more edits than DeepL according to blind tests
- Less consistent than DeepL for repeated translations
- No built-in translation memory
- Can introduce semantic shifts

**Estimated Cost Example:**
- 10,000 words translation with GPT-4o: $0.045 input + $0.15 output = $0.195

---

### 1.3 DeepL API

**URL:** https://www.deepl.com/en/pro-api

**Key Features:**
- Best-in-class translation quality for European languages
- Strong consistency (same input = same output)
- Excellent for specialized terminology
- Translation glossary support
- Custom terminology database integration

**Pricing (2025):**
- **Free Tier:** 500,000 characters/month (testing/non-commercial only)
- **Starter:** €5.49/month + €4.99 per million characters
- **Advanced:** €24.49/month + €14.99 per million characters
- **Ultimate:** €44.49/month + €24.99 per million characters

**Estonian Language Support:** Excellent. DeepL officially supports Estonian and shows particular strength for European languages.

**Custom Terminology:** Excellent. Built-in glossary feature allows uploading custom terminology that's enforced during translation.

**Pros for Small Community:**
- Best translation quality for Estonian
- 500,000 free characters/month for testing
- Most consistent translations
- Requires 2x fewer edits than Google Translate, 3x fewer than ChatGPT
- Built-in glossary support

**Cons:**
- Free tier limited to non-commercial testing
- More expensive per character than AI models
- Lower character limit than token-based pricing
- Monthly subscription required for commercial use

**Estimated Cost Example:**
- 10,000 words (~50,000 characters)
- Free tier: First 500k characters free, then €4.99 per million = ~€0.25
- Monthly cost for regular use: €5.49 + usage fees

---

### 1.4 LibreTranslate (Open Source)

**URL:** https://libretranslate.com / https://github.com/LibreTranslate/LibreTranslate

**Key Features:**
- Free and open source
- Self-hosted or cloud-hosted
- Offline capable
- Privacy-focused (data stays on your server)
- Argos Translate engine
- API compatible with other translation services

**Pricing:**
- **Self-hosted:** Free (open source)
- **Cloud hosted (libretranslate.com):** Free tier + paid plans available
- **No hidden costs or proprietary restrictions**

**Estonian Language Support:** Yes, Estonian is supported. However, translation quality is generally lower than DeepL or LLM-based tools.

**Custom Terminology:** Limited. Not as sophisticated as commercial solutions.

**Pros for Small Community:**
- Completely free if self-hosted
- Full control over data
- Open source - can be modified
- No usage limits when self-hosted
- Privacy-focused

**Cons:**
- Translation quality "sometimes falters" according to user reviews
- Requires technical setup for self-hosting
- Limited terminology management
- Slower than commercial APIs

**Note:** There's a newer project called **LTEngine** that uses larger language models for improved quality, reportedly comparable to or better than DeepL for some languages.

---

## 2. Translation Platform Solutions

### 2.1 Weblate ⭐ TOP RECOMMENDATION FOR OPEN SOURCE

**URL:** https://weblate.org

**Type:** Open Source (GPL License)

**Key Features:**
- Web-based translation platform
- Git integration (direct integration with version control)
- Translation memory
- Terminology management (glossaries)
- Automatic suggestions
- Machine translation integration (Google, DeepL, Microsoft, etc.)
- Review workflow with comments
- User roles and permissions
- Translation quality checks
- Supports 40+ file formats

**Pricing (2025):**

**Cloud Hosted:**
- 10k strings: €45/month or €450/year (€37.50/month)
- 40k strings: €66/month or €660/year (€55/month)
- 160k strings: €106/month or €1,060/year (€88.33/month)
- 640k strings: €178/month or €1,780/year
- 2.5M strings: €313/month or €3,130/year
- 10M strings: €562/month or €5,620/year

**Libre Plan (FREE):**
- Free for public open source projects
- Same features as 160k plan
- Must be public projects

**Self-Hosted:**
- Gratis: Free (open source software)
- Basic Support: €50/month (optional)
- Extended Support: €100/month (optional)

**All cloud plans include:**
- All Weblate features
- Unlimited projects
- Unlimited components
- Unlimited translators
- Premium support from core developers
- 14-day free trial

**Estonian Language Support:** Excellent. Weblate supports Estonian interface and translation workflows.

**Custom Terminology:** Excellent. Full glossary support with terminology management.

**Review Workflow:** Excellent. Comments, suggestions, review states, quality checks built-in.

**Pros for Small Community:**
- **Best option for public open source ACA project**
- Libre plan is completely free (160k strings limit)
- Can self-host for complete control
- Full-featured - nothing held back
- Strong Git integration
- Active development community
- Can use multiple machine translation services
- Data ownership (especially self-hosted)

**Cons:**
- Must be public project for free tier
- Interface may have learning curve
- Self-hosting requires technical expertise

**Recommendation:** **BEST CHOICE** for ACA translation project if willing to make project public.

---

### 2.2 POEditor

**URL:** https://poeditor.com

**Type:** Commercial SaaS

**Key Features:**
- Web-based translation platform
- Translation memory
- Machine translation integrations
- Multiple file format support
- API access
- Unlimited projects and collaborators (all plans)
- Version control integration

**Pricing (2025):**
- **Free:** 1,000 strings, unlimited projects, up to 5 contributors
- **Start:** $14.99/month, 3,000 strings
- **Plus:** $44.99/month, 10,000 strings (Most Popular)
- **Premium:** $119.99/month, 30,000 strings
- **Enterprise:** $199.99/month, 100,000 strings

**Discount options:**
- 6-month prepay: ~10% discount
- 12-month prepay: ~15% discount

**Open Source:** Free for projects with OSI-approved license

**Estonian Language Support:** Yes, supports Estonian.

**Custom Terminology:** Good. Supports glossaries and translation memory.

**Review Workflow:** Yes. Comments, suggestion mode, proofreading features.

**Pros for Small Community:**
- **Most affordable paid option** ($14.99/month)
- Unlimited projects and collaborators
- All features included (no tiered features)
- Free for open source projects
- Simple, straightforward interface
- No extra costs for team members

**Cons:**
- String limits can be restrictive
- Less feature-rich than competitors
- Cloud-only (no self-hosting)

**Recommendation:** Best budget option for small paid project or free for open source.

---

### 2.3 Crowdin

**URL:** https://crowdin.com

**Type:** Commercial SaaS with Open Source Program

**Key Features:**
- Comprehensive localization platform
- Translation memory with configurable matching (40-100%)
- Terminology management with source text review
- Quality assurance checks
- Workflow automation (parallel/sequential steps)
- Pre-translation with TM
- Multiple file format support (40+)
- Integration with development tools
- Machine translation support (DeepL, Google, etc.)
- Review and approval workflows
- Version control integration

**Pricing (2025):**
- **Free:** 60,000 words limit, basic features
- **Individual:** $59/month
- **Team:** $179/month
- **Enterprise:** $450+/month

**Open Source Program:**
- **Free for qualifying open source projects**
- Must be: Non-commercial, publicly accessible, OSI-approved license
- Includes: Unlimited projects, strings, and members
- Academic discount: 50% off

**Estonian Language Support:** Excellent. Full support for Estonian language.

**Custom Terminology:** Excellent. Dedicated terminology management with glossaries, source text review step.

**Review Workflow:** Excellent. Multi-step workflows (translation → proofreading → approval), parallel/sequential options, quality checks.

**Pros for Small Community:**
- Free for qualifying open source projects
- Most comprehensive features
- Excellent workflow management
- Strong community support for open source
- Professional-grade platform
- Good documentation

**Cons:**
- Expensive if not open source
- May be overly complex for simple needs
- Cloud-only
- Free plan very limited (60k words)

**Recommendation:** Excellent choice if project qualifies for open source program.

---

### 2.4 Transifex

**URL:** https://www.transifex.com

**Type:** Commercial SaaS with Open Source Program

**Key Features:**
- Professional localization platform
- Translation memory
- Git integration (GitHub, Bitbucket)
- Support for 46+ file formats
- Branching for iterative development
- Online editor
- Team collaboration

**Pricing (2025):**
- **Basic:** $70/month
- **Premium:** $105/month
- **Starter:** $120/month
- **Growth:** $570/month
- **Enterprise:** Custom

**Open Source Program:**
- Free for qualifying projects
- Requirements: No funding, revenue, or commercialization model
- Focus on small independent open source projects

**Estonian Language Support:** Yes, supports Estonian.

**Custom Terminology:** Limited. Users report "very limited functionality for searching terms, no filtering options, no real TM management."

**Review Workflow:** Basic. Online editor with review capabilities but less sophisticated than competitors.

**Pros for Small Community:**
- Free for qualifying open source
- Good Git integration
- Supports many file formats
- Professional platform

**Cons:**
- **Weak terminology management** (major limitation)
- Limited TM features compared to competitors
- Expensive paid plans
- Acquired by XTM International in 2025 (uncertain future)
- More restrictive open source criteria

**Recommendation:** Not recommended due to weak terminology management, which is critical for ACA translation.

---

### 2.5 Lokalise

**URL:** https://lokalise.com

**Type:** Commercial SaaS

**Key Features:**
- Professional localization platform
- Translation memory
- Collaborative web editor
- Import/export translation files
- Task management
- API access

**Pricing (2025):**
- **Free:** 500 translation keys, unlimited projects, basic features
- **Paid plans:** Start at $120/month for 5,000 translation keys

**Open Source/Non-Profit:** No specific program found.

**Estonian Language Support:** Yes, supports Estonian.

**Custom Terminology:** Yes. Supports terminology management.

**Review Workflow:** Yes. Task management and collaboration features.

**Pros for Small Community:**
- Free tier available
- Professional platform
- Good collaboration features

**Cons:**
- Limited free tier (500 keys)
- Expensive paid plans
- No open source program
- No non-profit discount found

**Recommendation:** Not ideal for small volunteer community due to cost and limited free tier.

---

### 2.6 Tolgee ⭐ GREAT SELF-HOSTED OPTION

**URL:** https://tolgee.io

**Type:** Open Source

**Key Features:**
- **In-context translation** (ALT+click in app to translate)
- One-click screenshot generation
- Translation memory
- Machine translation (DeepL, Google Translate, AWS)
- Auto-translation suggestions
- Activity log
- Figma plugin
- Web-based editor
- Developer-friendly

**Pricing:**
- **Self-hosted:** FREE forever (open source)
- **Self-hosted Free Plan includes:** 10 seats, in-context translating, auto translation, translation memory, activity log, machine translations
- **Cloud:** Paid plans for larger teams

**Estonian Language Support:** Yes, as it integrates with major MT providers.

**Custom Terminology:** Yes, through translation memory and manual glossaries.

**Review Workflow:** Yes, with activity log and collaboration features.

**Pros for Small Community:**
- **Completely free when self-hosted**
- Modern, developer-friendly interface
- In-context translation is excellent feature
- No seat/project limits when self-hosted
- Open source
- Integrates with DeepL, Google Translate

**Cons:**
- Self-hosting requires technical setup
- Smaller community than Weblate
- Newer platform (less mature)

**Recommendation:** Excellent option for technically capable teams wanting modern UI and in-context translation.

---

### 2.7 translate5

**URL:** https://www.translate5.net

**Type:** Open Source (with commercial support)

**Key Features:**
- "What you see is what you get" support for all file types
- Translation memory
- Machine translation integration
- Terminology management
- Quality assurance
- Used by language service providers
- Based on Okapi Framework and LanguageTool

**Pricing:**
- **Open Source:** Free (self-hosted)
- **30-day free trial**
- **Cloud-hosted:** €250/month (2 main users + 20 linguists)
- **Self-hosted with support:** €600/month (2 main users + 20 linguists)

**Estonian Language Support:** Yes, supports Estonian.

**Custom Terminology:** Yes. Four core functions include terminology management.

**Review Workflow:** Yes. Professional proofreading and post-editing features.

**Pros for Small Community:**
- Free if self-hosted
- Professional-grade features
- WYSIWYG editing
- Flexible architecture

**Cons:**
- Expensive commercial support
- Requires technical expertise for self-hosting
- Smaller community
- Pricing not transparent for smaller teams

**Recommendation:** Consider only if WYSIWYG editing is critical and you can self-host.

---

## 3. Desktop CAT (Computer-Assisted Translation) Tools

### 3.1 OmegaT ⭐ BEST FREE DESKTOP TOOL

**URL:** https://omegat.org

**Type:** Open Source (Free)

**Key Features:**
- Professional translation memory application
- Glossary support (TSV format, UTF-8)
- Multiple translation memories simultaneously
- Fuzzy matching and match propagation
- Dictionary matching
- Concordance searching
- Spell-checking (Hunspell dictionaries)
- TMX, XLIFF, SDLXLIFF format support
- Multiple files/folders simultaneously
- Cross-platform (Java-based: Windows, macOS, Linux)

**Pricing:** Completely FREE (open source)

**Estonian Language Support:** Yes. Uses Hunspell dictionaries (same as LibreOffice, Firefox).

**Custom Terminology:** Excellent. Simple TSV-format glossaries, multiple glossaries supported simultaneously.

**Review Workflow:** Basic. Multi-user collaboration supported but less sophisticated than web platforms.

**Pros for Small Community:**
- Completely free
- No limits on projects, files, or TMs
- Better matching algorithm than Wordfast or Trados (per reviews)
- Fast segmenting and compilation
- Great support community
- Works offline
- Full control over data

**Cons:**
- Desktop application (not web-based)
- Learning curve for first-time users
- Less feature-rich than commercial CAT tools
- Collaboration requires manual TM sharing
- Java-based (requires Java runtime)

**Recommendation:** Excellent for personal CLI assistant (Milestone 2). Not ideal for web-based community tool (Milestone 3).

---

## 4. Collaboration Platforms for Translation Workflows

### 4.1 Google Docs

**URL:** https://docs.google.com

**Key Features:**
- Real-time collaboration
- Commenting and suggesting mode
- Version history with timestamps
- User permissions
- Revision tracking
- Automatic saving
- Google Translate integration
- Free for personal use

**Pricing:**
- **Free:** 15GB storage (personal)
- **Google Workspace:** $6-18/user/month

**Estonian Language Support:** Yes. Google Translate supports Estonian.

**Custom Terminology:** Poor. No built-in terminology management. Manual only.

**Review Workflow:** Excellent. Suggestion mode, comments, resolve threads, version history.

**Pros for Small Community:**
- Free for small teams
- Familiar interface
- Excellent real-time collaboration
- Great for review and approval
- No technical setup
- Accessible anywhere

**Cons:**
- Not designed for translation
- No translation memory
- No terminology enforcement
- Manual workflow management
- Limited for large-scale projects

**Recommendation:** Good for document review phase but not primary translation tool.

---

### 4.2 Notion

**URL:** https://notion.so

**Key Features:**
- Flexible workspace (wiki, roadmap, documentation)
- Version history
- Collaboration and comments
- Database features
- Template support
- Integration possibilities

**Pricing:**
- **Free:** Personal use
- **Plus:** $10/user/month
- **Business:** $18/user/month

**Estonian Language Support:** Interface supports Estonian.

**Custom Terminology:** Poor. Manual only, though databases could track terminology.

**Review Workflow:** Good. Comments and collaboration features.

**Pros for Small Community:**
- Free for small teams
- Very flexible
- Good for project management
- Can build custom workflows
- Database features useful for terminology tracking

**Cons:**
- Not designed for translation
- No built-in translation features
- Requires manual setup
- Learning curve for complex setups
- No translation memory

**Recommendation:** Good for project management and documentation, not primary translation tool. Could potentially track terminology in databases.

---

### 4.3 Integration Options

**Google Docs + Notion Integration:**
- Tools like Latenode and Make.com can sync Google Docs with Notion
- Enables automated workflows between platforms
- Useful for combining document collaboration (Google Docs) with project management (Notion)

**Translation Platform + Collaboration Tool:**
- Most translation platforms have commenting and review features built-in
- Better to use dedicated translation platform than general collaboration tools
- Use Google Docs/Notion for supplementary documentation and planning

---

## 5. 12-Step Program and ACA-Specific Resources

### 5.1 ACA Translation Program

**URL:** https://adultchildren.org / https://acawso.org/translations/

**Key Information:**
- ACA has official Translation Subcommittee
- Guidelines document available: "Guidelines for Translation of ACA Literature and Materials"
- ACA literature available in multiple languages
- Free literature section includes translated materials
- ACA seeks volunteers for translation teams worldwide
- Support and guidance provided for translation teams
- Translation license process managed by WSO (World Service Organization)

**Translation Process:**
- Work with Translations Sub-Committee
- Collaboration with Publishing staff
- Publications prepared for both print and digital
- Licensing requirements must be met

**Available Resources:**
- Steps available in different languages
- Trifolds in various languages
- Multiple topic documents

**Important:** ACA is not affiliated with AA but follows 12-step structure. Has separate translation program and guidelines.

---

### 5.2 Alcoholics Anonymous Translation Resources

**URL:** https://www.aa.org / https://anonpress.org/translate/

**Key Information:**
- Big Book translated into 70+ languages
- AA publishes in English, Spanish, French
- Licenses translations in international languages
- International General Service Offices guide local translation
- Extensive catalog of translated materials
- "Plain Language Big Book" available as accessibility tool

**Distribution:**
- Online bookstore with translated materials
- Country-specific service offices
- Meeting lists in multiple languages

**Note:** AA has more resources and longer history but is separate from ACA.

---

### 5.3 Non-Profit Translation Services

**Translators without Borders (TWB)**

**URL:** https://translatorswithoutborders.org

**Key Information:**
- 501(c)(3) nonprofit
- Kató platform: 26,000+ volunteer translators
- 250+ language pairs
- Serves non-profit organizations worldwide

**Important Limitation for ACA:**
- Religious organizations must be registered as charity with secular community designation
- Must serve people regardless of religious beliefs
- Cannot propagate specific faith

**Conclusion:** ACA might not qualify due to spiritual nature of 12-step programs.

---

## 6. Comparison Matrix

### 6.1 AI Translation APIs Comparison

| Tool | Input Cost | Output Cost | Free Tier | Estonian Quality | Terminology Support | Best For |
|------|------------|-------------|-----------|------------------|---------------------|----------|
| **DeepL API** | €4.99/M chars | Same | 500k chars/month | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Glossaries | Best quality |
| **Claude Sonnet 4.5** | $3/M tokens | $15/M tokens | None | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Prompts | Long docs, caching |
| **GPT-4o** | $3/M tokens | $10/M tokens | None | ⭐⭐⭐ Good | ⭐⭐⭐ Prompts | General purpose |
| **LibreTranslate** | Free | Free | Unlimited | ⭐⭐ Fair | ⭐⭐ Limited | Privacy, self-hosted |

**10,000 word document (~50,000 chars / ~15,000 tokens):**
- DeepL: ~€0.25 after free tier
- Claude Sonnet 4.5: ~$0.27 (or $0.03-0.10 with caching)
- GPT-4o: ~$0.20
- LibreTranslate: Free

---

### 6.2 Translation Platforms Comparison

| Platform | Open Source | Free Tier | Paid Start | Estonian | Terminology | Review | Self-Host | Best For |
|----------|-------------|-----------|------------|----------|-------------|--------|-----------|----------|
| **Weblate** | ✅ GPL | ✅ 160k strings (public) | €45/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | Public OSS |
| **Tolgee** | ✅ | ✅ Unlimited (self-host) | Free | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | Modern UI |
| **POEditor** | ❌ | ✅ 1k strings | $14.99/mo | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ | Budget paid |
| **Crowdin** | ❌ | ❌ 60k words | $59/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | Enterprise OSS |
| **Transifex** | ❌ | ❌ None | $70/mo | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ❌ | Not recommended |
| **Lokalise** | ❌ | ✅ 500 keys | $120/mo | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ | Not for volunteers |
| **translate5** | ✅ | ✅ (self-host) | €250/mo | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | LSP workflows |
| **OmegaT** | ✅ | ✅ Unlimited | Free | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ Desktop | Personal use |

---

## 7. Recommendations by Project Milestone

### Milestone 1: Terminology Database
**Recommended Approach:**
1. **Primary:** Simple structured format (CSV/TSV) in Git repository
   - Easy to version control
   - Compatible with all tools (OmegaT, Weblate, DeepL glossaries)
   - Free and simple
2. **Secondary:** Notion database (for team collaboration and notes)
   - Good for discussions and context
   - Can track term status and decisions
3. **Export formats:** OmegaT glossary (TSV), DeepL glossary (CSV), JSON for API use

**Cost:** Free

---

### Milestone 2: Personal CLI Translation Assistant
**Recommended Stack:**

**Option A - Best Quality:**
- **OmegaT** for desktop translation memory + glossaries
- **DeepL API** for machine translation (free 500k chars/month)
- **Custom CLI** to combine both
- **Cost:** Free for testing, ~€5-10/month if exceeding free tier

**Option B - Most Flexible:**
- **OmegaT** for TM + glossaries
- **Claude API** for context-aware translation with terminology prompts
- **Prompt caching** for terminology consistency
- **Cost:** ~$1-5/month with caching

**Option C - Fully Free:**
- **OmegaT** standalone with custom glossaries
- **LibreTranslate** for MT suggestions
- **Cost:** Free

**Recommendation:** Start with Option C (free), upgrade to Option A (DeepL) when quality is critical.

---

### Milestone 3: Estonian Community Web Tool
**Recommended Platform:**

**Option A - Public Open Source (FREE):**
- **Weblate Libre Plan**
- 160k strings free
- Full features
- Professional quality
- **Requirement:** Must be public project
- **Cost:** Free

**Option B - Private Self-Hosted (FREE but technical):**
- **Tolgee** or **Weblate** self-hosted
- Complete control
- No limits
- Modern UI (Tolgee) or mature features (Weblate)
- **Requirement:** Server + technical expertise
- **Cost:** Free + hosting (~$5-10/month for small VPS)

**Option C - Paid Budget:**
- **POEditor Start Plan**
- $14.99/month for 3,000 strings
- Simple, unlimited collaborators
- **Cost:** $14.99/month

**Recommendation:**
- If public is acceptable: **Weblate Libre** (best value)
- If must be private: **Tolgee self-hosted** (modern UI)
- If no technical skills: **POEditor** (affordable)

---

### Milestone 4: Universal Multi-Language Platform
**Recommended Approach:**

**Option A - Open Source Community:**
- **Weblate** as primary platform
- Either cloud-hosted (paid) or self-hosted
- Scales to millions of strings
- Supports unlimited languages
- Git integration for version control
- Can integrate multiple MT providers
- **Cost:** €45-178/month cloud, or free self-hosted

**Option B - Hybrid Approach:**
- **Custom-built platform** using:
  - **DeepL API** for high-quality translation
  - **Claude API** for context-aware suggestions
  - **OmegaT TMX files** for translation memory
  - **PostgreSQL** for terminology database
  - **React/Next.js** web interface
- Full control and customization
- **Cost:** Development time + API costs (~$50-200/month depending on volume)

**Option C - Enterprise Platform:**
- **Crowdin** (if can maintain open source status)
- Professional features
- Unlimited scale
- **Cost:** Free for open source, $450+/month if commercial

**Recommendation:** **Weblate** provides best balance of features, cost, and open source values for ACA community.

---

## 8. Budget Scenarios

### Scenario 1: Zero Budget (100% Free)
**Stack:**
- Terminology: CSV in Git repository
- Personal CLI: OmegaT + LibreTranslate
- Community Tool: Weblate Libre (public) or Tolgee self-hosted
- MT: LibreTranslate self-hosted or DeepL free tier (testing only)
- **Total Cost:** $0/month (+ optional VPS $5/month for self-hosting)

---

### Scenario 2: Minimal Budget ($10-20/month)
**Stack:**
- Terminology: Notion free + CSV exports
- Personal CLI: OmegaT + DeepL API (~€5-10/month)
- Community Tool: POEditor Start ($14.99/month) or Weblate Libre (free)
- MT: DeepL API
- **Total Cost:** $15-25/month

---

### Scenario 3: Professional Budget ($50-100/month)
**Stack:**
- Terminology: Notion + structured database
- Personal CLI: OmegaT + Claude API with caching (~$5-10/month)
- Community Tool: Weblate 10k plan (€45/month) or POEditor Plus ($44.99/month)
- MT: Claude API + DeepL API as needed
- **Total Cost:** $60-100/month

---

### Scenario 4: Enterprise / Multi-Language ($200+/month)
**Stack:**
- Terminology: Full TMS integration
- Community Tool: Weblate 40k+ plan (€66-178/month) or Crowdin (if OSS qualified)
- MT: DeepL Advanced + Claude API
- Infrastructure: Dedicated hosting
- **Total Cost:** $200-500+/month

---

## 9. Key Decision Factors

### 9.1 Public vs Private Project
- **Public:** Weblate Libre = FREE (160k strings)
- **Private:** Must pay or self-host

### 9.2 Technical Expertise
- **High:** Self-host Weblate or Tolgee (free, full control)
- **Medium:** Use cloud platforms with CLI integration
- **Low:** POEditor or cloud Weblate (managed services)

### 9.3 Translation Quality Priority
- **Highest:** DeepL API (best for Estonian)
- **High:** Claude API with terminology prompts
- **Medium:** GPT-4o
- **Budget:** LibreTranslate

### 9.4 Budget Constraints
- **Zero budget:** Weblate Libre + OmegaT + LibreTranslate
- **<$20/month:** POEditor + DeepL free tier
- **$50-100/month:** Weblate cloud + Claude/DeepL APIs
- **$200+/month:** Professional setup with multiple tools

### 9.5 Team Size
- **1-2 people:** OmegaT + simple glossaries
- **3-10 people:** POEditor or Weblate Libre
- **10+ people:** Weblate cloud or Crowdin
- **Community (unlimited):** Weblate (supports unlimited translators)

---

## 10. Implementation Roadmap Recommendation

### Phase 1: Foundation (Months 1-2)
**Focus:** Milestone 1 + 2
1. Set up terminology database in CSV format
2. Create OmegaT project with glossaries
3. Test DeepL API (use free tier)
4. Build simple CLI that combines OmegaT + DeepL
5. Translate 1-2 sample documents to establish workflow

**Cost:** Free (using DeepL free tier)

---

### Phase 2: Community Beta (Months 3-4)
**Focus:** Milestone 3
1. Decision point: Public or private?
   - **Public:** Set up Weblate Libre (free)
   - **Private:** Deploy Tolgee self-hosted or subscribe to POEditor
2. Import terminology database
3. Upload 5-10 documents
4. Invite 5-10 beta testers
5. Establish review workflow
6. Test MT integrations

**Cost:**
- Public: Free
- Private self-hosted: $5-10/month (hosting)
- Private managed: $15/month (POEditor)

---

### Phase 3: Estonian Community Launch (Months 5-6)
**Focus:** Polish Milestone 3
1. Finalize terminology based on beta feedback
2. Add more ACA literature
3. Create user guides in Estonian
4. Establish translator roles and permissions
5. Launch to broader Estonian ACA community

**Cost:** Same as Phase 2

---

### Phase 4: Multi-Language Expansion (Months 7-12)
**Focus:** Milestone 4
1. Evaluate if Weblate Libre/Tolgee can scale
2. If needed, upgrade to Weblate paid plan or migrate to larger platform
3. Add second language (e.g., Latvian, Lithuanian, Finnish)
4. Create language-agnostic terminology structure
5. Establish community governance model
6. Document process for adding new languages

**Cost:** €45-178/month (depends on volume) or continue free if self-hosted

---

## 11. Risk Considerations

### Technical Risks
1. **Self-hosting complexity:** Requires ongoing maintenance, backups, updates
   - **Mitigation:** Start with cloud-hosted, migrate to self-hosted later if needed

2. **API cost escalation:** Heavy usage could exceed budget
   - **Mitigation:** Set API usage limits, monitor costs, use caching (Claude), prioritize DeepL free tier

3. **Data loss:** Version control issues, accidental deletions
   - **Mitigation:** Use Git for version control, regular backups, Weblate has built-in Git integration

### Community Risks
1. **Low volunteer engagement:** Translation platforms unused
   - **Mitigation:** Start small, provide training, make it very easy to contribute

2. **Quality control:** Poor translations accepted
   - **Mitigation:** Implement review workflow, require 2-person review, terminology enforcement

3. **Terminology disputes:** Disagreement on translations
   - **Mitigation:** Document decision-making process, have terminology committee

### Legal/Licensing Risks
1. **ACA copyright:** Permission required for translations
   - **Mitigation:** Work with ACA Translation Subcommittee, follow official guidelines

2. **Platform terms of service:** Some platforms restrict certain content
   - **Mitigation:** Review ToS, prefer open source self-hosted solutions

3. **Open source compliance:** If using OSS licenses from platforms
   - **Mitigation:** Understand requirements, maintain public repos if required

### Sustainability Risks
1. **Funding:** Reliance on paid services without sustainable income
   - **Mitigation:** Prioritize free/open source solutions, seek ACA organizational support

2. **Maintainer burnout:** Single person maintaining everything
   - **Mitigation:** Build team, document everything, use managed services where possible

3. **Platform lock-in:** Hard to migrate if platform shuts down
   - **Mitigation:** Use standard formats (TMX, XLIFF), regular exports, prefer open source

---

## 12. Final Recommendations Summary

### For Immediate Start (Today)
1. **Create terminology CSV** in Git repository
2. **Download OmegaT** and create first project
3. **Sign up for DeepL API free tier** (500k chars/month)
4. **Test translation workflow** with one sample document

**Cost:** Free

---

### For Personal Use (Milestone 2)
**Recommended:** OmegaT + DeepL API
**Alternative:** OmegaT + Claude API with prompt caching
**Budget:** OmegaT + LibreTranslate

**Cost:** Free to €10/month

---

### For Estonian Community (Milestone 3)
**Recommended:** Weblate Libre (if public is acceptable)
**Alternative 1:** Tolgee self-hosted (if can self-host)
**Alternative 2:** POEditor Start plan (if must be private and can't self-host)

**Cost:** Free to $15/month

---

### For Global ACA Platform (Milestone 4)
**Recommended:** Weblate (cloud-hosted or self-hosted)
**Alternative:** Crowdin (if can maintain open source qualification)

**Cost:** Free (self-hosted) to €45-178/month (cloud)

---

### Translation Quality
**Recommended:** DeepL API for Estonian
**Strength:** Best quality for European languages, built-in glossary support
**Free tier:** 500,000 characters/month

---

### Most Important Success Factor
**Start simple, iterate based on real usage.**

Don't over-engineer upfront. Begin with:
1. CSV terminology file
2. OmegaT for personal translation
3. DeepL free tier for MT
4. Google Docs for review/collaboration

Then upgrade to proper platform (Weblate Libre) once you have:
- 5+ volunteers ready to contribute
- 10+ documents to translate
- Established terminology (100+ terms)
- Proven translation workflow

---

## 13. Additional Resources

### Official Documentation
- **DeepL API:** https://developers.deepl.com/docs
- **Claude API:** https://docs.anthropic.com
- **OpenAI API:** https://platform.openai.com/docs
- **Weblate Docs:** https://docs.weblate.org
- **OmegaT Manual:** https://omegat.sourceforge.io/manual-standard/
- **ACA Translation Guidelines:** https://acawso.org/wp-content/uploads/2019/09/Guidelines-for-Translations.pdf

### Community Resources
- **Weblate Community:** https://github.com/WeblateOrg/weblate
- **OmegaT Support:** https://omegat.org/support
- **Tolgee Community:** https://github.com/tolgee/tolgee-platform
- **ACA Translation Teams:** https://acawso.org/translations/

### Comparison Articles
- "The Definitive Guide to AI Translation Tools" (Medium): DeepL vs GPT-4 vs Claude
- "Translation API Pricing Comparison": https://www.machinetranslation.com/blog/price-comparison-of-popular-machine-translation-apis
- "Transifex vs. Crowdin vs. POEditor vs. Lokalise": https://aboutlocalization.wordpress.com/

---

## Questions for Further Consideration

Before finalizing your approach, consider:

1. **Privacy:** Can ACA translation project be public, or must it be private due to sensitive content?
2. **Official ACA Support:** Have you contacted ACA Translation Subcommittee? Can they provide guidance or support?
3. **Volume:** Approximately how many words/pages of content need translation? (affects platform choice)
4. **Timeline:** What's the urgency? (affects build vs buy decision)
5. **Team Size:** How many translators do you expect? (1? 5? 20? 100?)
6. **Languages:** Just Estonian, or Baltic region (Estonian, Latvian, Lithuanian)?
7. **Technical Skills:** Can you self-host and maintain servers, or prefer managed services?
8. **Budget Reality:** Is this volunteer project with zero budget, or can ACA organization fund it?
9. **Governance:** Who approves translations? Is there a formal review process?
10. **Long-term Vision:** Is this Estonian-only project, or truly aiming for global multi-language platform?

---

**Document Version:** 1.0
**Last Updated:** 2025-10-14
**Researched by:** Claude (Anthropic)
**Project:** ACA/ATL Estonian Translation Initiative
