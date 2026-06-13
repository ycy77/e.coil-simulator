---
entity_id: "reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "ARGININE-N-SUCCINYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "ARGININE-N-SUCCINYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARGININE-N-SUCCINYLTRANSFERASE-RXN

`reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARGININE-N-SUCCINYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ARG + SUC-COA -> PROTON + CPD-421 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARG + SUC-COA -> PROTON + CPD-421 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by astA (protein.P0AE37). Substrates: L-Arginine (molecule.C00062), Succinyl-CoA (molecule.C00091). Products: CoA (molecule.C00010), H+ (molecule.C00080), N2-Succinyl-L-arginine (molecule.C03296).

## Enriched Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Annotation

ARG + SUC-COA -> PROTON + CPD-421 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AE37|protein.P0AE37]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03296|molecule.C03296]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ARGININE-N-SUCCINYLTRANSFERASE-RXN`

## Notes

ARG + SUC-COA -> PROTON + CPD-421 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
