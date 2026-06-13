---
entity_id: "reaction.ecocyc.RXN-20756"
entity_type: "reaction"
name: "RXN-20756"
source_database: "EcoCyc"
source_id: "RXN-20756"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20756

`reaction.ecocyc.RXN-20756`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20756`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SEPO3 + mnm5GeS2U -> mnm5SeP2U + CPD-22373; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SEPO3 + mnm5GeS2U -> mnm5SeP2U + CPD-22373; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Selenophosphoric acid (molecule.C05172), a 5-methylaminomethyl-2-(S-geranyl)thiouridine34 in tRNA (molecule.ecocyc.mnm5GeS2U). Products: (2E)-3,7-dimethylocta-2,6-diene-1-thiol (molecule.ecocyc.CPD-22373), a 5-methylaminomethyl-2-(Se-phospho)selenouridine34 in tRNA (molecule.ecocyc.mnm5SeP2U).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

SEPO3 + mnm5GeS2U -> mnm5SeP2U + CPD-22373; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.CPD-22373|molecule.ecocyc.CPD-22373]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.mnm5SeP2U|molecule.ecocyc.mnm5SeP2U]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05172|molecule.C05172]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.mnm5GeS2U|molecule.ecocyc.mnm5GeS2U]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20756`

## Notes

SEPO3 + mnm5GeS2U -> mnm5SeP2U + CPD-22373; direction=PHYSIOL-LEFT-TO-RIGHT
