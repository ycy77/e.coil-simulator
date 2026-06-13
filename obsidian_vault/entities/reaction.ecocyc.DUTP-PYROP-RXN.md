---
entity_id: "reaction.ecocyc.DUTP-PYROP-RXN"
entity_type: "reaction"
name: "DUTP-PYROP-RXN"
source_database: "EcoCyc"
source_id: "DUTP-PYROP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DUTP-PYROP-RXN

`reaction.ecocyc.DUTP-PYROP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DUTP-PYROP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of pyrimidine nucleotide metabolism. EcoCyc reaction equation: DUTP + WATER -> PROTON + DUMP + PPI; direction=LEFT-TO-RIGHT. This reaction is part of pyrimidine nucleotide metabolism.

## Biological Role

Catalyzed by dUTP diphosphatase (complex.ecocyc.DUTP-PYROP-CPLX), nudI (protein.P52006). Substrates: H2O (molecule.C00001), dUTP (molecule.C00460). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), dUMP (molecule.C00365).

## Enriched Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction is part of pyrimidine nucleotide metabolism.

## Pathways

- `ecocyc.PWY-7184` pyrimidine deoxyribonucleotides de novo biosynthesis I (EcoCyc)
- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY-7206` pyrimidine deoxyribonucleotides dephosphorylation (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.DUTP-PYROP-CPLX|complex.ecocyc.DUTP-PYROP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P52006|protein.P52006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00365|molecule.C00365]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00460|molecule.C00460]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01346|molecule.C01346]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12520|molecule.ecocyc.CPD-12520]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EGTA|molecule.ecocyc.EGTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DUTP-PYROP-RXN`

## Notes

DUTP + WATER -> PROTON + DUMP + PPI; direction=LEFT-TO-RIGHT
