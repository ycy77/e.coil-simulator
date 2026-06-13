---
entity_id: "reaction.ecocyc.2.3.1.41-RXN"
entity_type: "reaction"
name: "2.3.1.41-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.41-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.41-RXN

`reaction.ecocyc.2.3.1.41-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.41-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Long-Chain-Acyl-ACPs + MALONYL-ACP + PROTON -> Long-Chain-3-oxo-ACPs + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Long-Chain-Acyl-ACPs + MALONYL-ACP + PROTON -> Long-Chain-3-oxo-ACPs + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Annotation

Long-Chain-Acyl-ACPs + MALONYL-ACP + PROTON -> Long-Chain-3-oxo-ACPs + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.3.1.41-RXN`

## Notes

Long-Chain-Acyl-ACPs + MALONYL-ACP + PROTON -> Long-Chain-3-oxo-ACPs + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
