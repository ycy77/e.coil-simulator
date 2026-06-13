---
entity_id: "reaction.ecocyc.3.4.13.9-RXN"
entity_type: "reaction"
name: "3.4.13.9-RXN"
source_database: "EcoCyc"
source_id: "3.4.13.9-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Proline dipeptidase"
  - "Imidodipeptidase"
  - "Prolidase"
  - "Peptidase D"
---

# 3.4.13.9-RXN

`reaction.ecocyc.3.4.13.9-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.13.9-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dipeptides-With-Proline-Carboxy + WATER -> PRO + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Dipeptides-With-Proline-Carboxy + WATER -> PRO + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Xaa-Pro dipeptidase (complex.ecocyc.CPLX0-8156). Substrates: H2O (molecule.C00001), a dipeptide with a C-terminal L-proline (molecule.ecocyc.Dipeptides-With-Proline-Carboxy). Products: L-Proline (molecule.C00148), a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

Dipeptides-With-Proline-Carboxy + WATER -> PRO + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8156|complex.ecocyc.CPLX0-8156]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Dipeptides-With-Proline-Carboxy|molecule.ecocyc.Dipeptides-With-Proline-Carboxy]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.13.9-RXN`

## Notes

Dipeptides-With-Proline-Carboxy + WATER -> PRO + Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT
