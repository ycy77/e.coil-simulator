---
entity_id: "reaction.ecocyc.RXN0-5513"
entity_type: "reaction"
name: "Long-chain-fatty-acid--acyl-carrier protein ligase"
source_database: "EcoCyc"
source_id: "RXN0-5513"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Long-chain-fatty-acid--acyl-carrier protein ligase

`reaction.ecocyc.RXN0-5513`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5513`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell. EcoCyc reaction equation: ATP + ACP + CPD66-39 -> AMP + PPI + Saturated-Fatty-Acyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell.

## Biological Role

Catalyzed by aas (protein.P31119). Substrates: ATP (molecule.C00002), a 2,3,4-saturated fatty acid (molecule.ecocyc.CPD66-39). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

This reaction is part of the acyl-CoA-independent incorporation of exogenous fatty acids and 2-acyllysophospholipids into the cell.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P31119|protein.P31119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD66-39|molecule.ecocyc.CPD66-39]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.Salts|molecule.ecocyc.Salts]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5513`

## Notes

ATP + ACP + CPD66-39 -> AMP + PPI + Saturated-Fatty-Acyl-ACPs; direction=PHYSIOL-LEFT-TO-RIGHT
