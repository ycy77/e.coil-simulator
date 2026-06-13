---
entity_id: "reaction.ecocyc.RXN-20757"
entity_type: "reaction"
name: "RXN-20757"
source_database: "EcoCyc"
source_id: "RXN-20757"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20757

`reaction.ecocyc.RXN-20757`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20757`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

mnm5SeP2U + WATER -> Mnm5Se2U-containing-tRNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: mnm5SeP2U + WATER -> Mnm5Se2U-containing-tRNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a 5-methylaminomethyl-2-(Se-phospho)selenouridine34 in tRNA (molecule.ecocyc.mnm5SeP2U). Products: a 5-methylaminomethyl-2-selenouridine34 in tRNA (molecule.ecocyc.Mnm5Se2U-containing-tRNAs), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

mnm5SeP2U + WATER -> Mnm5Se2U-containing-tRNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Mnm5Se2U-containing-tRNAs|molecule.ecocyc.Mnm5Se2U-containing-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.mnm5SeP2U|molecule.ecocyc.mnm5SeP2U]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20757`

## Notes

mnm5SeP2U + WATER -> Mnm5Se2U-containing-tRNAs + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
