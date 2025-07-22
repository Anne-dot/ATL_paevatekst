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

## 🔄 Järgmised sammud
- [ ] Google Drive API seadistamine
- [ ] Python skripti loomine  
- [ ] GitHub Actions päevane ajastus

---