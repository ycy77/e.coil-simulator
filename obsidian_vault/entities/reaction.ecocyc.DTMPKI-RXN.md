---
entity_id: "reaction.ecocyc.DTMPKI-RXN"
entity_type: "reaction"
name: "DTMPKI-RXN"
source_database: "EcoCyc"
source_id: "DTMPKI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DTMPKI-RXN

`reaction.ecocyc.DTMPKI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DTMPKI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the last unique reaction in the pathway leading to dTTP biosynthesis. EcoCyc reaction equation: TMP + ATP -> TDP + ADP; direction=LEFT-TO-RIGHT. This is the last unique reaction in the pathway leading to dTTP biosynthesis.

## Biological Role

Catalyzed by dTMP kinase (complex.ecocyc.CPLX0-8260). Substrates: ATP (molecule.C00002), dTMP (molecule.C00364). Products: ADP (molecule.C00008), dTDP (molecule.C00363).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

This is the last unique reaction in the pathway leading to dTTP biosynthesis.

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7197` pyrimidine deoxyribonucleotide phosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8260|complex.ecocyc.CPLX0-8260]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00363|molecule.C00363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00364|molecule.C00364]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00365|molecule.C00365]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1508|molecule.ecocyc.CPD0-1508]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DTMPKI-RXN`

## Notes

TMP + ATP -> TDP + ADP; direction=LEFT-TO-RIGHT
