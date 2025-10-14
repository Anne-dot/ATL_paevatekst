#!/bin/bash
# Skript Sõnaveeb terminibaasi terminite kogumiseks
# Kasutamine: ./kogub_terminid.sh <terminibaasi_kood> <väljund_fail>
# Näide: ./kogub_terminid.sh skt skeemiteraapia_terminid.txt

if [ $# -lt 2 ]; then
    echo "Kasutamine: $0 <terminibaasi_kood> <väljund_fail>"
    echo "Näited:"
    echo "  $0 skt skeemiteraapia_terminid.txt   # Skeemiteraapia"
    echo "  $0 dkt dkt_terminid.txt               # DKT/DBT"
    echo "  $0 kriis kriis_terminid.txt           # Kriisinõustamine"
    echo "  $0 TAI tervis_terminid.txt            # Tervisesõnastik"
    exit 1
fi

TERMINIBAAS="$1"
VALJUND="$2"
BASE_URL="https://sonaveeb.ee/ds/${TERMINIBAAS}"

echo "Kogun termineid terminibaasist: $TERMINIBAAS"
echo "Salvestamine faili: $VALJUND"
echo ""

# Tühjenda väljundfail
> "$VALJUND"

# Käi läbi kõik tähestiku tähed
for TAHT in a b c d e f g h i j k l m n o p q r s t u v w x y z õ ä ö ü; do
    echo "Töötlen täht: $TAHT"

    # Lae leht ja erista terminite lingid
    curl -s "${BASE_URL}/${TAHT}" | \
        grep -oP '<a href="/search/unif/dlall/'"${TERMINIBAAS}"'/[^"]*">[^<]+</a>' | \
        sed -E 's|<a href="/search/unif/dlall/'"${TERMINIBAAS}"'/[^"]*">([^<]+)</a>|\1|' | \
        while read -r termin; do
            # URL-decode (asenda %20 tühikutega jne)
            termin_decoded=$(echo "$termin" | sed 's/%20/ /g; s/%C3%A4/ä/g; s/%C3%B5/õ/g; s/%C3%BC/ü/g; s/%C3%B6/ö/g')
            echo "$termin_decoded" >> "$VALJUND"
        done

    sleep 0.5  # Väike paus, et serverit mitte üle koormata
done

# Eemalda duplikaadid ja sorteeri
sort -u "$VALJUND" -o "$VALJUND"

echo ""
echo "Valmis! Kogutud $(wc -l < "$VALJUND") terminit."
echo "Terminid salvestatud faili: $VALJUND"
