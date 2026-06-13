---
entity_id: "reaction.ecocyc.DCTP-DEAM-RXN"
entity_type: "reaction"
name: "DCTP-DEAM-RXN"
source_database: "EcoCyc"
source_id: "DCTP-DEAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DCTP-DEAM-RXN

`reaction.ecocyc.DCTP-DEAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DCTP-DEAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of pyrimidine nucleotide metabolism. EcoCyc reaction equation: PROTON + WATER + DCTP -> AMMONIUM + DUTP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of pyrimidine nucleotide metabolism.

## Biological Role

Catalyzed by dCTP deaminase (complex.ecocyc.DCTP-DEAM-CPLX). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), dCTP (molecule.C00458). Products: dUTP (molecule.C00460), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction is part of pyrimidine nucleotide metabolism.

## Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.DCTP-DEAM-CPLX|complex.ecocyc.DCTP-DEAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00460|molecule.C00460]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DCTP-DEAM-RXN`

## Notes

PROTON + WATER + DCTP -> AMMONIUM + DUTP; direction=PHYSIOL-LEFT-TO-RIGHT
