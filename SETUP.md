# 🛠️ ATL Päevamõtete Bot - Seadistamise Juhis

## 📋 Ülevaade
See dokument sisaldab sammhaaval juhiseid ATL päevamõtete Discord boti seadistamiseks.

---

## ✅ 1. Discord Webhook Seadistamine

### 📝 Sammud
1. **🔒 Loo privaatne testimiskanal**
   - Discord serveris: loo uus kanal (nt #bot-test-privaatne)
   - Edit Channel → Permissions → @everyone → View Channel: ❌
   - Ainult sina näed seda kanalit

2. **🔗 Loo webhook**
   - Server Settings → Integrations → Webhooks
   - "Create Webhook" → Nimi: "ATL päevamõtted"
   - Vali privaatne testimiskanal
   - Kopeeri webhook URL

3. **🧪 Testi webhook'i käsurealt**
   ```bash
   curl -X POST "WEBHOOK_URL" \
     -H "Content-Type: application/json" \
     -d '{"content": "🧪 Test post - ATL päevamõtete bot testimine"}'
   ```

4. **🔐 Salvesta GitHub secret'ina**
   ```bash
   gh secret set DISCORD_WEBHOOK_URL --body "WEBHOOK_URL"
   ```

5. **✅ Testi GitHub Actions'iga**
   - Käivita manual workflow: "Test Discord Webhook Secret"
   - Peaksid nägema uut sõnumit Discord kanalises

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

## 🔄 Järgmised sammud
- [ ] Python skripti loomine  
- [ ] GitHub Actions päevane ajastus

---