# 🔧 ATL Päevamõtete Bot - Veaotsing

## 📞 Kontakt
**Probleem?** Võta ühendust: ruusmann@gmail.com

---

## ⚡ Kiired Lahendused

### Bot ei postita Discord'i
1. **Kontrolli GitHub Actions**
   ```bash
   gh run list --limit 5
   ```
2. **Vaata viimast workflow logi**
   ```bash
   gh run view --log
   ```
3. **Käivita käsitsi test**
   ```bash
   gh workflow run daily-meditation.yml
   ```

### Google Drive viga
- **"Authentication failed"** → Kontrolli `GOOGLE_CREDENTIALS` secret
- **"Document not found"** → Kontrolli `config.py` dokumendi ID-d

### Discord webhook viga
- **"Webhook not found"** → Kontrolli `DISCORD_WEBHOOK_URL` secret
- **Testi webhook'i**
  ```bash
  curl -X POST "$DISCORD_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d '{"content": "Test post"}'
  ```

### GitHub Actions ei käivitu
- Kontrolli cron schedule: `0 3 * * *` (06:00 Eesti aeg)
- Käivita käsitsi: `gh workflow run daily-meditation.yml`

---

## 📋 GitHub Secrets
```bash
gh secret list
```
Peaks näitama:
- `DISCORD_WEBHOOK_URL`
- `GOOGLE_CREDENTIALS`

---

## 🔄 See on arenev dokument
Uued probleemid ja lahendused lisatakse siia järk-järgult.

**Kontakt:** ruusmann@gmail.com