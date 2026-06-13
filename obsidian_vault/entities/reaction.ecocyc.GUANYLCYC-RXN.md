---
entity_id: "reaction.ecocyc.GUANYLCYC-RXN"
entity_type: "reaction"
name: "GUANYLCYC-RXN"
source_database: "EcoCyc"
source_id: "GUANYLCYC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GUANYLCYC-RXN

`reaction.ecocyc.GUANYLCYC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANYLCYC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes cyclic GMP. EcoCyc reaction equation: GTP -> CGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes cyclic GMP.

## Biological Role

Catalyzed by GUANYLCYC-MONOMER (protein.ecocyc.GUANYLCYC-MONOMER). Substrates: GTP (molecule.C00044). Products: Diphosphate (molecule.C00013), 3',5'-Cyclic GMP (molecule.C00942).

## Annotation

This reaction synthesizes cyclic GMP.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.ecocyc.GUANYLCYC-MONOMER|protein.ecocyc.GUANYLCYC-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00942|molecule.C00942]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GUANYLCYC-RXN`

## Notes

GTP -> CGMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
