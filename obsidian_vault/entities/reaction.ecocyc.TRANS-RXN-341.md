---
entity_id: "reaction.ecocyc.TRANS-RXN-341"
entity_type: "reaction"
name: "chloramphenicol:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# chloramphenicol:proton antiport

`reaction.ecocyc.TRANS-RXN-341`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-341`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CHLORAMPHENICOL + PROTON -> CHLORAMPHENICOL + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CHLORAMPHENICOL + PROTON -> CHLORAMPHENICOL + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtL (protein.P31462). Substrates: H+ (molecule.C00080), chloramphenicol (molecule.ecocyc.CHLORAMPHENICOL). Products: H+ (molecule.C00080), chloramphenicol (molecule.ecocyc.CHLORAMPHENICOL).

## Annotation

CHLORAMPHENICOL + PROTON -> CHLORAMPHENICOL + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31462|protein.P31462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CHLORAMPHENICOL|molecule.ecocyc.CHLORAMPHENICOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CHLORAMPHENICOL|molecule.ecocyc.CHLORAMPHENICOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-341`

## Notes

CHLORAMPHENICOL + PROTON -> CHLORAMPHENICOL + PROTON; direction=REVERSIBLE
