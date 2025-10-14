# SNAP TARKVARA JUHEND

## 1. OTSING
```bash
snap search [tarkvara_nimi]
```
**Näited:**
- `snap search whisper` - audio transkriptsioon
- `snap search firefox` - veebibrauser
- `snap search code` - koodiredaktor
- `snap search gimp` - pildiredaktor

## 2. ÜKSIKASJALIK INFO
```bash
snap info [paketi_nimi]
```
**Näide:**
```bash
snap info whisper-gael
```

## 3. INSTALLIMINE
```bash
sudo snap install [paketi_nimi]
```

## 4. INSTALLITUD PAKETID
```bash
snap list
```

## 5. KÄSU LEIDMINE
```bash
ls /snap/bin/ | grep [nimi]
```

## 6. EEMALDAMINE
```bash
sudo snap remove [paketi_nimi]
```

## 7. UUENDAMINE
```bash
sudo snap refresh [paketi_nimi]
# Või kõik korraga:
sudo snap refresh
```

## EELISED:
- ✅ Automaatsed sõltuvused
- ✅ Turvalisus (isoleeritud)
- ✅ Lihtne install/uninstall
- ✅ Automaatsed uuendused

**Alati proovi snap enne pip/apt installimist!**

## NÄIDE: Whisper installimine
1. `snap search whisper`
2. `sudo snap install whisper-gael`
3. `ls /snap/bin/ | grep whisper`
4. `whisper-gael.whisper --help`