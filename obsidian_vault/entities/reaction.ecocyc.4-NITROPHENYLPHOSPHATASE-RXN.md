---
entity_id: "reaction.ecocyc.4-NITROPHENYLPHOSPHATASE-RXN"
entity_type: "reaction"
name: "4-NITROPHENYLPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "4-NITROPHENYLPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4-NITROPHENYLPHOSPHATASE-RXN

`reaction.ecocyc.4-NITROPHENYLPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4-NITROPHENYLPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-194 + WATER -> P-NITROPHENOL + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-194 + WATER -> P-NITROPHENOL + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), ushA (protein.P07024). Substrates: H2O (molecule.C00001), 4-Nitrophenyl phosphate (molecule.C03360). Products: H+ (molecule.C00080), 4-Nitrophenol (molecule.C00870), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-194 + WATER -> P-NITROPHENOL + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00870|molecule.C00870]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03360|molecule.C03360]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:4-NITROPHENYLPHOSPHATASE-RXN`

## Notes

CPD-194 + WATER -> P-NITROPHENOL + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
