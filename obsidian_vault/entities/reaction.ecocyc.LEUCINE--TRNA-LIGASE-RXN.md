---
entity_id: "reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "LEUCINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "LEUCINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "LEUCYL-TRNA SYNTHETASE"
---

# LEUCINE--TRNA-LIGASE-RXN

`reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LEUCINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LEU-tRNAs + LEU + ATP -> Charged-LEU-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LEU-tRNAs + LEU + ATP -> Charged-LEU-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by leuS (protein.P07813). Substrates: ATP (molecule.C00002), L-Leucine (molecule.C00123). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

LEU-tRNAs + LEU + ATP -> Charged-LEU-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07813|protein.P07813]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LEUCINE--TRNA-LIGASE-RXN`

## Notes

LEU-tRNAs + LEU + ATP -> Charged-LEU-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
