---
entity_id: "reaction.ecocyc.RXN-23945"
entity_type: "reaction"
name: "RXN-23945"
source_database: "EcoCyc"
source_id: "RXN-23945"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23945

`reaction.ecocyc.RXN-23945`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23945`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Valyl-tRNAIle + WATER -> ILE-tRNAs + VAL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Valyl-tRNAIle + WATER -> ILE-tRNAs + VAL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ileS (protein.P00956). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), L-Valine (molecule.C00183).

## Annotation

Valyl-tRNAIle + WATER -> ILE-tRNAs + VAL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P00956|protein.P00956]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23945`

## Notes

Valyl-tRNAIle + WATER -> ILE-tRNAs + VAL + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
