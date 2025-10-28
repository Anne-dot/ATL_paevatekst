# 🤝 ATL Päevamõtete Bot - Üleandmisjuhend

## 📞 Kontakt
**Küsimused üleandmise kohta:** ruusmann@gmail.com

---

## 🔄 1. Ligipääsude Üleandmine

### 🤖 Google Service Account
1. **Google Cloud Console ligipääs**
   - Mine: https://console.cloud.google.com
   - Projekt: "ATL päevamõtted"
   - Anna uuele isikule Project Owner õigused
   
2. **Service Account kontroll**
   - Email: `atl-paevamotte-bot@atl-paevamotted.iam.gserviceaccount.com`
   - Õigused: Google Drive API read-only
   - ATL dokumendid juba jagatud sellega ✅

### 📁 GitHub Repository
1. **Repo üleandmine**
   - Repository: `Anne-dot/ATL_paevatekst`
   - Settings → Manage access → Invite collaborator
   - Anna "Admin" õigused
   
2. **Secrets kontroll**
   - `DISCORD_WEBHOOK_URL` ✅ (tootmise kanal)
   - `DISCORD_WEBHOOK_TEST_URL` ✅ (testikanal)
   - `GOOGLE_CREDENTIALS` ✅ (Google Drive API)

### 💬 Discord Ligipääs
1. **Discord admin õigused vajalikud**
   - Uus isik peab saama Discord serveri admin õigused
   - **VÕI** olemasolev admin peab tema eest webhook'e haldama

2. **Kanalid**
   - **Tootmise kanal:** ATL päevamõtete kanal (webhook: `DISCORD_WEBHOOK_URL`)
   - **Testikanal:** Privaatne testimiskanal (webhook: `DISCORD_WEBHOOK_TEST_URL`)
   - **Automaatne valik:** Workflow tuvastab event tüübi ja valib õige webhoki
     - `schedule` (cron 6:00) → tootmise kanal
     - `workflow_dispatch` (käsitsi) → testikanal

---

## 🏢 2. Organisatsiooni Kontekst

### ATL (Adult Children of Alcoholics) Eesti
- **Email:** atl.eneseabi@gmail.com
- **Veebileht:** atleesti.wordpress.com
- **Staatus:** Vabatahtlik organisatsioon
- **Lepingud:** Puuduvad - vabatahtlik töö

### Projekti Eesmärk
- Automaatne igapäevane meditatsiooni postitamine
- Eesti ACA kogukonna toetamine
- Püsiv vaimne praktika Discord'i kaudu

---

## 🔧 3. Tehnilised Detailid

### Süsteemi Ülevaade
- **Ajastus:** Iga päev kell 06:00 Eesti aeg
- **Allikas:** 12 kuist Google Drive dokumenti
- **Sihtkoht:** Discord kanal webhook kaudu
- **Platform:** GitHub Actions (cloud)

### Failide Struktuur
```
ATL_paevatekst/
├── main.py              # Peamine skript
├── config.py            # Konfiguratsioon ja dokument ID-d
├── drive_client.py      # Google Drive API
├── discord_client.py    # Discord webhook
├── date_utils.py        # Kuupäeva töötlus
├── SETUP.md            # Seadistamisjuhend
└── TROUBLESHOOTING.md  # Veaotsing
```

### Google Drive Dokumendid
- 12 kuud, iga kuu oma dokument
- ID-d on hardcoded `config.py` failis
- Service Account'il on read-only ligipääs ✅

---

## 📋 4. Regulaarsed Hooldusülesanded

### Igapäevane
- **Automaatne:** Bot käivitub ise kell 06:00
- **🚨 PUUDUB: Discord monitoring** - admin ei saa teada, kui bot ebaõnnestub

### Kuine
- **Kontrolli:** Kas uue kuu dokument on õigesti seadistatud
- **Test:** Käivita workflow käsitsi GitHubis (Actions → "Run workflow")
  - Postitus läheb automaatselt **testikanali** ✅
  - Kontrollid tänast kuupäeva ja uue kuu dokumenti

### Aastane/Vajaduse järgi
- **Credentials rotation:** Kui vajalik (Google keys, Discord webhook)
- **Dokumentide uuendamine:** Kui ATL muudab Google Drive struktuuri

---

## 🔒 5. Backup ja Disaster Recovery

### Backup
- **Kood:** GitHub repository ✅
- **Credentials:** GitHub Secrets ✅
- **Konfiguratsioon:** `config.py` failis ✅

### Disaster Recovery
1. **Kui bot ei tööta:**
   - Vaata TROUBLESHOOTING.md
   - Kontrolli GitHub Actions loge
   
2. **Kui kõik kaob:**
   - Fork repository
   - Seadista uued secrets
   - Testi kohalikult

---

## 🚨 6. Puuduvad Funktsioonid (Vaja Lisada)

### Kriitilised
- [ ] **Discord monitoring kanal** - admin'i teavitamine vigadest
- [ ] **Email backup notifications** - kui Discord ei tööta
- [ ] **GitHub Actions failure alerts** - automaatne teavitamine

### Mugavused
- [ ] **Manuaalne retry funktsioon** - kui päev jäi vahele
- [ ] **Status dashboard** - viimaste postituste ülevaade
- [ ] **Automated testing** - kuude vahetuse test

---

## 📝 7. Viimased Täiendused (Oktoober 2025)

### ✅ Lahendatud Probleemid
- **Issue #13:** `ModuleNotFoundError: No module named 'packaging'`
  - Lisatud kriitilised implitsiitsed sõltuvused `requirements.txt` faili
  - `google-api-core>=2.0.0` ja `packaging>=21.0`

- **Issue #14:** Automaatne test/production webhook valik
  - Workflow tuvastab automaatselt event tüübi
  - Ei pea enam käsitsi secreti vahetama testimiseks
  - Käsitsi "Run workflow" → testikanal
  - Automaatne cron → tootmise kanal

### 🔧 Tehnilised Detailid
- Workflow fail: `.github/workflows/daily-meditation.yml`
- Event tuvastamine: `github.event_name` muutuja
- Ternary operator: `${{ condition && value_if_true || value_if_false }}`

---

## ✅ Üleandmise Kontroll-list

### Enne üleandmist
- [ ] Google Cloud Project ligipääs antud
- [ ] GitHub repo admin õigused antud
- [ ] Discord admin õigused antud/koordineeritud
- [ ] Uus isik testinud käsitsi workflow
- [ ] Kontaktandmed vahetatud

### Pärast üleandmist  
- [ ] Vana ligipääs eemaldatud (kui vajalik)
- [ ] Dokumentatsioon üle vaadatud
- [ ] Esimene kuu monitooritud koos

---

**Kontakt:** ruusmann@gmail.com