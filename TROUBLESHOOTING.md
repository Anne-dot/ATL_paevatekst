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
- **"Webhook not found"** → Kontrolli `DISCORD_WEBHOOK_URL` või `DISCORD_WEBHOOK_TEST_URL` secret
- **Vale kanal** → Kontrolli, kas kasutad õiget webhoki:
  - Automaatne cron (6:00) → `DISCORD_WEBHOOK_URL` (tootmine)
  - Käsitsi "Run workflow" → `DISCORD_WEBHOOK_TEST_URL` (test)
- **Testi webhook'i**
  ```bash
  # Tootmise webhook
  curl -X POST "$DISCORD_WEBHOOK_URL" \
    -H "Content-Type: application/json" \
    -d '{"content": "Test post - production"}'

  # Testi webhook
  curl -X POST "$DISCORD_WEBHOOK_TEST_URL" \
    -H "Content-Type: application/json" \
    -d '{"content": "Test post - test channel"}'
  ```

### GitHub Actions ei käivitu
- Kontrolli cron schedule: `0 3 * * *` (06:00 Eesti aeg)
- Käivita käsitsi: `gh workflow run daily-meditation.yml`

### Python sõltuvuste vead
- **"ModuleNotFoundError: No module named 'packaging'"**
  - **Põhjus:** Puuduv implitsiitne sõltuvus (Issue #13, okt 2025)
  - **Lahendus:** Kontrolli `requirements.txt` sisaldab:
    ```
    google-api-core>=2.0.0
    packaging>=21.0
    ```
  - **Test lokaalses keskkonnas:**
    ```bash
    python3 -m venv test_env
    test_env/bin/pip install -r requirements.txt
    test_env/bin/python -c "from drive_client import get_current_month_meditation_text"
    ```

- **Muud import vead**
  - Kontrolli, kas kõik paketid on `requirements.txt` failis
  - GitHub Actions logis peaks olema `pip install -r requirements.txt` edukas
  - Vaata täpset veateadet: `gh run view --log`

---

## 📋 GitHub Secrets
```bash
gh secret list
```
Peaks näitama:
- `DISCORD_WEBHOOK_URL` - Tootmise kanal (automaatne cron)
- `DISCORD_WEBHOOK_TEST_URL` - Testikanal (käsitsi "Run workflow")
- `GOOGLE_CREDENTIALS` - Google Drive API autentimine

---

## 🔄 See on arenev dokument
Uued probleemid ja lahendused lisatakse siia järk-järgult.

**Kontakt:** ruusmann@gmail.com