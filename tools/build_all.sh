#!/usr/bin/env bash
# Rebuild every book in the top folder from src/content. Run from the repository root.
set -euo pipefail
declare -A BOOKS=(
 [1.1]=contracts-1 [1.2]=constitution-1 [1.3]=torts [1.4]=crimes-1 [1.5]=family-1
 [2.1]=contracts-2 [2.2]=constitution-2 [2.3]=environmental [2.4]=jurisprudence [2.5]=administrative
 [3.1]=property [3.2]=labour-1 [3.3]=company [3.4]=pil [3.5]=interpretation
 [4.1]=labour-2 [4.2]=family-2 [4.3]=taxation [4.4]=ipr [4.5]=land
 [5.1]=cpc [5.2]=bnss [5.3]=bsa [5.4]=banking [5.5]=media
 [6.1]=drafting [6.2]=ethics [6.3]=adr [6.4]=moot [6.5]=penology
 [maxims]=maxims [writing]=writing [bail]=bail
)
for src in "${!BOOKS[@]}"; do
  python3 src/build.py "src/content/$src.txt" "${BOOKS[$src]}.html"
done
