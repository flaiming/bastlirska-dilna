# Veřejný web bastleni.oram.cz: zdroje ve verejny-web/, výstup v site/ (není v gitu).

SERVER = flaim@oram.cz:/www/bastleni/

.PHONY: web nahled nasadit fotka

# Sestaví site/ z Markdownu a šablony
web:
	python3 -B verejny-web/build.py

# Sestaví web a pustí ho na http://localhost:8765
nahled: web
	python3 -m http.server 8765 --bind 127.0.0.1 --directory site

# Sestaví web a nahraje ho na server
nasadit: web
	rsync -az --delete site/ $(SERVER)

# Připraví fotku pro web: zmenší na 1600 px, odstraní metadata (GPS, datum, telefon), případně otočí.
#   make fotka Z=~/Downloads/IMG_1234.jpg JAKO=auto-novy [OTOCIT=90]
# Pak doplňte popisek do verejny-web/fotky.txt. Na fotce nesmí být obličej dítěte.
fotka:
	@test -n "$(Z)" -a -n "$(JAKO)" || { echo "Použití: make fotka Z=soubor.jpg JAKO=nazev [OTOCIT=90]"; exit 1; }
	@tmp=$$(mktemp -d) && \
	sips -s format png $(if $(OTOCIT),-r $(OTOCIT)) -Z 1600 "$(Z)" --out "$$tmp/f.png" >/dev/null && \
	sips -s format jpeg -s formatOptions 82 "$$tmp/f.png" --out "verejny-web/static/foto/$(JAKO).jpg" >/dev/null && \
	rm -r "$$tmp" && echo "verejny-web/static/foto/$(JAKO).jpg"
