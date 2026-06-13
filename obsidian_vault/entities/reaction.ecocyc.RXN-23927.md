---
entity_id: "reaction.ecocyc.RXN-23927"
entity_type: "reaction"
name: "RXN-23927"
source_database: "EcoCyc"
source_id: "RXN-23927"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23927

`reaction.ecocyc.RXN-23927`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23927`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HOMO-SER + ATP -> CPD-15554 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HOMO-SER + ATP -> CPD-15554 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), L-Homoserine (molecule.C00263). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-homoserine lactone (molecule.ecocyc.CPD-15554).

## Annotation

HOMO-SER + ATP -> CPD-15554 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23927`

## Notes

HOMO-SER + ATP -> CPD-15554 + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
