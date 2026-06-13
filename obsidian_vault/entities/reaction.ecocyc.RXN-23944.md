---
entity_id: "reaction.ecocyc.RXN-23944"
entity_type: "reaction"
name: "RXN-23944"
source_database: "EcoCyc"
source_id: "RXN-23944"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23944

`reaction.ecocyc.RXN-23944`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23944`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ILE-tRNAs + VAL + ATP -> Valyl-tRNAIle + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ILE-tRNAs + VAL + ATP -> Valyl-tRNAIle + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ileS (protein.P00956). Substrates: ATP (molecule.C00002), L-Valine (molecule.C00183). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

ILE-tRNAs + VAL + ATP -> Valyl-tRNAIle + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00956|protein.P00956]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23944`

## Notes

ILE-tRNAs + VAL + ATP -> Valyl-tRNAIle + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
