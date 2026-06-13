---
entity_id: "reaction.ecocyc.3.4.13.18-RXN"
entity_type: "reaction"
name: "3.4.13.18-RXN"
source_database: "EcoCyc"
source_id: "3.4.13.18-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.13.18-RXN

`reaction.ecocyc.3.4.13.18-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.13.18-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIPEPTIDES + WATER -> Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIPEPTIDES + WATER -> Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by peptidase D (complex.ecocyc.CPLX0-3001). Substrates: H2O (molecule.C00001), a dipeptide (molecule.ecocyc.DIPEPTIDES). Products: a proteinogenic amino acid (molecule.ecocyc.Amino-Acids-20).

## Annotation

DIPEPTIDES + WATER -> Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3001|complex.ecocyc.CPLX0-3001]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Amino-Acids-20|molecule.ecocyc.Amino-Acids-20]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DIPEPTIDES|molecule.ecocyc.DIPEPTIDES]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.13.18-RXN`

## Notes

DIPEPTIDES + WATER -> Amino-Acids-20; direction=PHYSIOL-LEFT-TO-RIGHT
