---
entity_id: "reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "CYSTEINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "CYSTEINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "CYSTEINYL-TRNA SYNTHETASE"
---

# CYSTEINE--TRNA-LIGASE-RXN

`reaction.ecocyc.CYSTEINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYSTEINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CYS-tRNAs + CYS + ATP -> Charged-CYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CYS-tRNAs + CYS + ATP -> Charged-CYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysS (protein.P21888). Substrates: ATP (molecule.C00002), L-Cysteine (molecule.C00097). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

CYS-tRNAs + CYS + ATP -> Charged-CYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21888|protein.P21888]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CYSTEINE--TRNA-LIGASE-RXN`

## Notes

CYS-tRNAs + CYS + ATP -> Charged-CYS-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
