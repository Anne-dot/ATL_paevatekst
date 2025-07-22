# Discord Päevamõtete Automatiseerimise Plaan

## Olukorra kirjeldus

**Praegune situatsioon:**
- ATL-i päevamõtted on Google Drive'is
- **12 eraldi dokumenti** - igal kuul oma fail ✅ UUENDATUD
- Tekstid kasutavad **H2 pealkirju** kuupäevade jaoks (nt "## 22. juuli") ✅ UUENDATUD
- Üks päev võib olla mitu rida pikk
- Käsitsi Discord'i postitamine on tüütu

**Eesmärk:**
Automatiseerida eestikeelsete päevamõtete postitamine Discord serverisse

## Lahenduse strateegia

### Lühiajaline lahendus (1-2 nädalat)
**MEE6 bot ajutiseks lahenduseks:**
- Lisa MEE6 bot Discord serverisse (arvutis)
- Sisesta järgmise nädala tekstid käsitsi
- Seadista automaatne ajastus (nt iga hommik kell 9:00)
- Kalendri meeldetuletus nädala lõpus uuendamiseks

### Pikaajaline lahendus (automatiseerimine)

## Tehnilised lahendused

### Kinnitatud Arhitektuur: Webhook + GitHub Actions

**Arhitektuur:**
```
Google Drive API → GitHub Actions skript → Discord Webhook → Discord kanal
```

**Komponendid:**
1. **Discord Webhook** ✅ KINNITATUD
   - Server Settings → Integrations → Webhooks
   - URL on nagu "tagauks" sõnumite saatmiseks
   - Lihtne ja tasuta (KISS printsiip)

2. **Google Drive API** ✅ KINNITATUD
   - **12 hardcode'itud URL-i** GitHub Actions keskkonnamuutujates ✅ UUENDATUD
   - Kasutab olemasolevat ligipääsu
   - Tõlkimise ja redigeerimise faasis mõistlik
   - Pole vaja failide otsingut või kopeerimist

3. **Teksti töötluse loogika:** ✅ UUENDATUD
   - Vali õige kuu URL hardcode'itud loetelust
   - Leia H2 pealkiri tänase kuupäevaga (nt "## 22. juuli")
   - Kogu tekst kuni järgmise H2 pealkirjani
   - Postita Discord'i

4. **GitHub Actions ajastus** ✅ KINNITATUD
   - Tasuta pilveteenus (2000 min/kuu tasuta)
   - Käivitub iga päev määratud kellaajal
   - Pole vaja oma serverit
   - Lihtne üleandmine (repo transfer)
   - Usaldusväärsus: GitHub'i infrastruktuur

## Vigade käsitlemine ✅ KINNITATUD

**Lihtne lähenemine (KISS):**
- Logi edu/ebaõnnestumine
- Jätka homme uuesti
- EI taaspostitamist (eelmise päeva tekst ei ole mõistlik)
- EI emaili teavitusi praegu (näed Discordis kui puudub)
- Tuleviku parendus: teadete süsteem

## Failide struktuur näide ✅ UUENDATUD

```
Google Drive fail "Jaanuar_2025.txt":

## 11. jaanuar
Tänane inspiratsioon tekst siin...
Võib olla mitu rida pikk
ja sisaldab erinevaid mõtteid.

## 12. jaanuar  
Uus päev algab uute võimalustega...
Jätkame lugemist...
Rohkem sisu siin...

## 13. jaanuar
Homne tekst algab siit...
```

**12 kuufaili:**
- Jaanuar_2025.txt
- Veebruar_2025.txt
- Märts_2025.txt
- ... jne

## Ajakulu hinnang (juunior programmeerijale)

**Kokku: 6-12 tundi** (jaotatud mitmele päevale)

- **Päev 1 (2-4h):** Google Drive API seadistamine
- **Päev 2 (2-3h):** Faili lugemine ja teksti töötlus
- **Päev 3 (1-2h):** Discord webhook
- **Päev 4 (1-3h):** GitHub Actions ja testimine

## Jätkusuutlikkus

**Praegune plaan:**
- Sinu GitHub konto (repo üleandmine on lihtne)
- ATL-i Google Drive ligipääs (juba olemas)
- Discord webhook (jääb serverisse)

**Üleandmise võimalused:**
- GitHub repository transfer (mõni klikk)
- Dokumentatsioon tehnilisele inimesele
- Google Drive API seadistamine uuele inimesele

## Alternatiivid (kaalutud ja tagasi lükatud)

### Discord Bot vs Webhook
- **Bot:** Rohkem funktsioone, keerulisem seadistamine
- **Webhook:** ✅ VALITUD - lihtne, teeb kõik vajalik

### Kohalik vs Pilveteenus
- **Kohalik:** Vajab alati töötavat arvutit
- **Pilveteenustus (GitHub Actions):** ✅ VALITUD - usaldusväärne, lihtne üleandmine

### Sisu salvestamine
- **JSON/tekstifailid:** Vajaks käsitsi uuendamist
- **Google Drive:** ✅ VALITUD - juba olemas, tõlkimisfaasis sobib

## Riskid ja lahendused

**Webhook'i ohud:**
- URL leke → regenereeri uus
- Spam võimalus → jälgi logisid
- Rate limit → max 30 sõnumit/min

**Drive API:**
- Ligipääsu kadumine → dokumenteeri seadistust
- API muudatused → kasuta stabiilset versiooni

**GitHub Actions:**
- Tasuta limiit → praegu piisav (150 min/kuu)
- Repo üleandmine → lihtne protsess

## Järgmised sammud

### Kohe (kui arvuti kätte saad):
1. **Testi MEE6 boti** - ajutine lahendus
2. **Seadista webhook** - testi käsurealt
3. **Proovi Drive API** - loe üks fail

### Hiljem (kui eelmine projekt valmis):
1. **Teksti töötluse skript**
2. **GitHub Actions ajastus**
3. **Testimine ja viimistlus**
4. **Dokumentatsiooni kirjutamine**

## Tehnilised märkmed ✅ UUENDATUD

**Webhook URL näide:**
```
https://discord.com/api/webhooks/123456789/abcdef...
```

**Lihtne webhook test:**
```bash
curl -X POST "WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"content": "**Tänane mõte:**\nTekst siia..."}'
```

**Google Drive URL-ide hardcoding GitHub Actions keskkonnas:**
```yaml
env:
  JANUARY_URL: "https://drive.google.com/file/d/1ABC123.../view"
  FEBRUARY_URL: "https://drive.google.com/file/d/1DEF456.../view"
  MARCH_URL: "https://drive.google.com/file/d/1GHI789.../view"
  # ... kõik 12 kuud
```

**Python loogika näide:**
```python
MONTHLY_URLS = {
    1: os.getenv('JANUARY_URL'),
    2: os.getenv('FEBRUARY_URL'),
    # ... kõik 12
}

current_month = datetime.now().month
file_url = MONTHLY_URLS[current_month]

# Leia H2 pealkiri: "## 22. juuli"
heading_pattern = f"## {current_day}\\. {estonian_month_name}"
```

**Google Drive API scopes:**
- `https://www.googleapis.com/auth/drive.readonly`

**Kasutatud tehnoloogiad:**
- Python või JavaScript
- Google APIs Client Library
- Discord Webhooks
- GitHub Actions (YAML)

---

*Plaan koostatud: 22.07.2025*
*Viimati uuendatud: 22.07.2025*
*Staatus: Arhitektuur kinnitatud, URL-ide hardcoding lisatud*
*Kinnitatud lahendused: Webhook + GitHub Actions + Google Drive (12 hardcode'itud URL-i) + Lihtne vigade käsitlemine + H2 pealkirjad*