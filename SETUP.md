# 🛠️ ATL Päevamõtete Bot - Seadistamise Juhis

## 📋 Ülevaade
See dokument sisaldab sammhaaval juhiseid ATL päevamõtete Discord boti seadistamiseks.

---

## ✅ 1. Discord Webhook Seadistamine

### 📝 Sammud

#### 🚀 Produktsiooni webhook (praegune)
1. **🔗 Loo webhook päris kanali jaoks**
   - Server Settings → Integrations → Webhooks
   - "Create Webhook" → Nimi: "ATL päevamõtted"
   - Vali ATL päevamõtete kanal
   - Kopeeri webhook URL

2. **🔐 Salvesta GitHub secret'ina**
   ```bash
   gh secret set DISCORD_WEBHOOK_URL --body "WEBHOOK_URL"
   ```

3. **✅ Testi GitHub Actions'iga**
   ```bash
   gh workflow run daily-meditation.yml
   ```

#### 🧪 Testimise webhook

**MÄRKUS:** Alates oktoobrist 2025 on testimine automaatne - ei pea enam käsitsi webhookie vahetama!

1. **🔒 Loo privaatne testimiskanal**
   - Discord serveris: loo uus kanal (nt #bot-test-privaatne)
   - Edit Channel → Permissions → @everyone → View Channel: ❌
   - Ainult sina näed seda kanalit

2. **🔗 Loo test webhook**
   - Server Settings → Integrations → Webhooks
   - "Create Webhook" → Nimi: "ATL test bot"
   - Vali privaatne testimiskanal
   - Kopeeri test webhook URL

3. **🔐 Salvesta GitHub secret'ina**
   ```bash
   gh secret set DISCORD_WEBHOOK_TEST_URL --body "TEST_WEBHOOK_URL"
   ```

4. **✅ Automaatne valik töötab:**
   - **Käsitsi "Run workflow"** → kasutab `DISCORD_WEBHOOK_TEST_URL` (testikanal)
   - **Automaatne cron (6:00)** → kasutab `DISCORD_WEBHOOK_URL` (tootmine)

   Workflow tuvastab automaatselt `github.event_name` ja valib õige webhoki.

5. **🧪 Testi GitHubis**
   - Mine Actions → "Daily ATL Meditation Bot"
   - Vajuta "Run workflow"
   - Kontrolli, et postitus ilmub **testikanalis** (mitte tootmises!)

### ⏱️ Ajakulu
~20 minutit

### 📊 Staatus
- [x] Privaatne testimiskanal loodud
- [x] Tootmise webhook loodud (`DISCORD_WEBHOOK_URL`)
- [x] Testimise webhook loodud (`DISCORD_WEBHOOK_TEST_URL`)
- [x] GitHub secretid salvestatud
- [x] Automaatne test/prod valik töötab
- [x] GitHub Actions test töötab

---

## ✅ 2. Google Drive API Seadistamine

### 📝 Sammud
1. **🌐 Google Cloud Console projekt**
   - Mine https://console.cloud.google.com
   - Loo uus projekt: "ATL päevamõtted"

2. **🔌 Drive API lubamine**
   - Otsi "Google Drive API"
   - Kliki "Enable"

3. **🤖 Service Account loomine**
   - APIs & Services → Credentials
   - Create Credentials → Service Account
   - Nimi: "atl-paevamotte-bot"
   - Description: "Bot for posting daily ATL meditations to Discord"

4. **🔑 JSON võtmete loomine**
   - Service Account detailides → Keys tab
   - Add Key → Create new key → JSON
   - Fail laadib automaatselt alla

5. **📂 Drive ligipääsu andmine**
   - Jaga ATL-i kuudokumendid Service Account'iga:
   - Email: `atl-paevamotte-bot@atl-paevamotted.iam.gserviceaccount.com`
   - Role: Viewer (ainult lugemisõigus)

6. **🔐 GitHub secret'ina salvestamine**
   ```bash
   gh secret set GOOGLE_CREDENTIALS --body "$(cat atl-paevamotted-*.json)"
   ```

7. **🧪 Ühenduse testimine**
   - Test Python skriptiga
   - Peaks nägema ATL-i dokumente

### ⏱️ Ajakulu
~43 minutit

### 📊 Staatus
- [x] Google Cloud projekt loodud
- [x] Drive API enabled
- [x] Service Account loodud
- [x] JSON võtmed allalaaditud
- [x] Drive ligipääs antud
- [x] GitHub secret salvestatud
- [x] Ühendus testitud - töötab! 🎉

---

---

## ✅ 3. Python Süsteemi Seadistamine

### 📝 Sammud
1. **📦 Vajalikud paketid**
   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt sisaldab:**
   - `google-api-python-client>=2.0.0` - Google Drive API
   - `google-auth>=2.0.0` - Google autentimine
   - `requests>=2.28.0` - Discord webhook postitamine
   - `python-dotenv>=0.19.0` - Keskkonna muutujad
   - `google-api-core>=2.0.0` - Kriitilised API sõltuvused
   - `packaging>=21.0` - Versioonihaldus (vajalik GitHub Actions keskkonnas)

   **Märkus:** `google-api-core` ja `packaging` on lisatud eksplitsiitselt, et vältida
   `ModuleNotFoundError` GitHubi Actions puhastes keskkondades (Issue #13, okt 2025).

2. **🔧 Kohalik testimine**
   - Pane `atl-paevamotted-*.json` fail projekti kausta
   - Käivita: `python3 drive_client.py` (test Google Drive)
   - Käivita: `python3 main.py` (test kogu süsteem)

3. **📁 Moodulite ülevaade**
   - `config.py` - Konfiguratsiooni ja konstantid
   - `date_utils.py` - Kuupäevade ja tekstilõikude töötlus
   - `drive_client.py` - Google Drive API klient
   - `discord_client.py` - Discord webhook klient
   - `main.py` - Peamine skript

### ⏱️ Ajakulu
~100 minutit (integreeritud)

### 📊 Staatus
- [x] 5 modular Python faili loodud
- [x] Google Drive tekstide lugemine töötab
- [x] Päevase teksti eraldamine töötab
- [x] Discord postitamine töötab
- [x] Kogu süsteem testitud ✅

---

## ✅ 4. GitHub Actions Seadistamine

### 📝 Sammud
1. **⏰ Igapäevane ajastus loodud**
   - Kell 06:00 Eesti aeg (03:00 UTC)
   - Workflow: `.github/workflows/daily-meditation.yml`

2. **🔐 Secrets konfiguratsioon**
   - `DISCORD_WEBHOOK_URL` ✅
   - `GOOGLE_CREDENTIALS` ✅

3. **🧪 Käsitsi testimine**
   ```bash
   gh workflow run daily-meditation.yml
   ```

### ⏱️ Ajakulu
~60 minutit

### 📊 Staatus
- [x] GitHub Actions workflow loodud
- [x] Dual authentication (kohalik + cloud)
- [x] Igapäevane ajastus seadistatud
- [x] Käsitsi käivitamine töötab
- [x] Automaatne test/prod webhook valik (okt 2025)
- [x] Kriitilised sõltuvused lisatud (okt 2025)

---

## 🎯 Projekti Olukord

### ✅ Lõpetatud (10/10 core issues)
- Discord webhook seadistamine
- Google Drive API integratsioon
- Modular Python süsteem (5 faili)
- Tekstide töötlus ja päevase sisu eraldamine
- GitHub Actions workflow
- Secrets ja environment setup
- Täielik end-to-end testimine
- Discord markdown formateerimine (Issue #10)
- Kuupäevade täpne regex (Issue #11)
- Kriitilised sõltuvused (Issue #13, okt 2025)
- Automaatne test/prod valik (Issue #14, okt 2025)

### 🎯 Production Ready
Bot on täielikult tootmisvalnis ja töötab iga päev kell 6:00 Eesti aja järgi.

**Progress: 100% - Projekt lõpetatud ja tootmises**

---