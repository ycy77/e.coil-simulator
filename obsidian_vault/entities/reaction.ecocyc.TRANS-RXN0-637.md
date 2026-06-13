---
entity_id: "reaction.ecocyc.TRANS-RXN0-637"
entity_type: "reaction"
name: "TRANS-RXN0-637"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-637"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-637

`reaction.ecocyc.TRANS-RXN0-637`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-637`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

OXIDIZED-GLUTATHIONE + ATP + WATER -> OXIDIZED-GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: OXIDIZED-GLUTATHIONE + ATP + WATER -> OXIDIZED-GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathione ABC transporter (complex.ecocyc.ABC-49-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Glutathione disulfide (molecule.C00127). Products: ADP (molecule.C00008), H+ (molecule.C00080), Glutathione disulfide (molecule.C00127), phosphate (molecule.ecocyc.Pi).

## Annotation

OXIDIZED-GLUTATHIONE + ATP + WATER -> OXIDIZED-GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-49-CPLX|complex.ecocyc.ABC-49-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-637`

## Notes

OXIDIZED-GLUTATHIONE + ATP + WATER -> OXIDIZED-GLUTATHIONE + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
