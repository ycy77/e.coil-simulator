---
entity_id: "reaction.ecocyc.TRANS-RXN-22"
entity_type: "reaction"
name: "glycerol-3-phosphate:phosphate antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-22"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# glycerol-3-phosphate:phosphate antiport

`reaction.ecocyc.TRANS-RXN-22`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-22`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Pi + GLYCEROL-3P -> Pi + GLYCEROL-3P; direction=REVERSIBLE EcoCyc reaction equation: Pi + GLYCEROL-3P -> Pi + GLYCEROL-3P; direction=REVERSIBLE.

## Biological Role

Catalyzed by glpT (protein.P08194). Substrates: sn-Glycerol 3-phosphate (molecule.C00093), phosphate (molecule.ecocyc.Pi). Products: sn-Glycerol 3-phosphate (molecule.C00093), phosphate (molecule.ecocyc.Pi).

## Annotation

Pi + GLYCEROL-3P -> Pi + GLYCEROL-3P; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08194|protein.P08194]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-5401|molecule.ecocyc.CPD-5401]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-22`

## Notes

Pi + GLYCEROL-3P -> Pi + GLYCEROL-3P; direction=REVERSIBLE
