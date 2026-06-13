---
entity_id: "reaction.ecocyc.RXN-24399"
entity_type: "reaction"
name: "RXN-24399"
source_database: "EcoCyc"
source_id: "RXN-24399"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24399

`reaction.ecocyc.RXN-24399`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24399`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

tyrosylated-ssDNA + WATER -> 5-phosphooligonucleotides + A-DNMP-L-TYROSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: tyrosylated-ssDNA + WATER -> 5-phosphooligonucleotides + A-DNMP-L-TYROSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by exodeoxyribonuclease VII (complex.ecocyc.CPLX-3946). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a 5'-phosphooligonucleotide (molecule.ecocyc.5-phosphooligonucleotides), a 2'-deoxyribonucleoside 5'-monophosphate-L-tyrosine (molecule.ecocyc.A-DNMP-L-TYROSINE).

## Annotation

tyrosylated-ssDNA + WATER -> 5-phosphooligonucleotides + A-DNMP-L-TYROSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX-3946|complex.ecocyc.CPLX-3946]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-phosphooligonucleotides|molecule.ecocyc.5-phosphooligonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.A-DNMP-L-TYROSINE|molecule.ecocyc.A-DNMP-L-TYROSINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24399`

## Notes

tyrosylated-ssDNA + WATER -> 5-phosphooligonucleotides + A-DNMP-L-TYROSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
