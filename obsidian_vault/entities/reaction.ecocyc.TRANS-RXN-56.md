---
entity_id: "reaction.ecocyc.TRANS-RXN-56"
entity_type: "reaction"
name: "phenylalanine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-56"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phenylalanine:proton symport

`reaction.ecocyc.TRANS-RXN-56`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-56`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + PHE -> PROTON + PHE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + PHE -> PROTON + PHE; direction=REVERSIBLE.

## Biological Role

Catalyzed by aroP (protein.P15993), pheP (protein.P24207). Substrates: L-Phenylalanine (molecule.C00079), H+ (molecule.C00080). Products: L-Phenylalanine (molecule.C00079), H+ (molecule.C00080).

## Annotation

PROTON + PHE -> PROTON + PHE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P15993|protein.P15993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P24207|protein.P24207]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-56`

## Notes

PROTON + PHE -> PROTON + PHE; direction=REVERSIBLE
