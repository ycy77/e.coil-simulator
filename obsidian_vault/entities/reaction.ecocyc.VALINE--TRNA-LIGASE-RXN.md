---
entity_id: "reaction.ecocyc.VALINE--TRNA-LIGASE-RXN"
entity_type: "reaction"
name: "VALINE--TRNA-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "VALINE--TRNA-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "VALYL-TRNA SYNTHETASE"
---

# VALINE--TRNA-LIGASE-RXN

`reaction.ecocyc.VALINE--TRNA-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:VALINE--TRNA-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

VAL-tRNAs + VAL + ATP -> Charged-VAL-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: VAL-tRNAs + VAL + ATP -> Charged-VAL-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by valS (protein.P07118). Substrates: ATP (molecule.C00002), L-Valine (molecule.C00183). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Annotation

VAL-tRNAs + VAL + ATP -> Charged-VAL-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TRNA-CHARGING-PWY` tRNA charging (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07118|protein.P07118]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:VALINE--TRNA-LIGASE-RXN`

## Notes

VAL-tRNAs + VAL + ATP -> Charged-VAL-tRNAs + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
