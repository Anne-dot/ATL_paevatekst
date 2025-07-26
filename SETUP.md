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

#### 🧪 Testimise webhook (tulevikuks)
<!--
MÄRKUS: Testimiseks loo eraldi privaatne kanal ja webhook

1. **🔒 Loo privaatne testimiskanal**
   - Discord serveris: loo uus kanal (nt #bot-test-privaatne)
   - Edit Channel → Permissions → @everyone → View Channel: ❌
   - Ainult sina näed seda kanalit

2. **🔗 Loo test webhook**
   - Server Settings → Integrations → Webhooks
   - "Create Webhook" → Nimi: "ATL test bot"
   - Vali privaatne testimiskanal
   - Kopeeri test webhook URL

3. **🧪 Testi käsurealt**
   ```bash
   curl -X POST "TEST_WEBHOOK_URL" \
     -H "Content-Type: application/json" \
     -d '{"content": "🧪 Test post - ATL päevamõtete bot testimine"}'
   ```

4. **🔄 Vaheta testimiseks**
   ```bash
   gh secret set DISCORD_WEBHOOK_URL --body "TEST_WEBHOOK_URL"
   ```
-->

### ⏱️ Ajakulu
~20 minutit

### 📊 Staatus
- [x] Privaatne testimiskanal loodud
- [x] Webhook loodud ja testitud käsurealt
- [x] GitHub secret salvestatud  
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
- [x] Manual käivitamine töötab ✅

---

## 🎯 Projekti Olukord

### ✅ Lõpetatud (7/10 issue)
- Discord webhook seadistamine
- Google Drive API integratsioon  
- Modular Python süsteem (5 faili)
- Tekstide töötlus ja päevase sisu eraldamine
- GitHub Actions workflow
- Secrets ja environment setup
- Täielik end-to-end testimine

### ⏳ Järelejäänud (3/10 issue)
- Dokumentatsiooni finaalviimistlus
- Laiendatud testimine produktsiooni andmetega
- Teksti formateerimise bugi parandamine

**Progress: 70% valmis**

---