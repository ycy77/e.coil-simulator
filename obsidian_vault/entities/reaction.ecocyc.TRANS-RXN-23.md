---
entity_id: "reaction.ecocyc.TRANS-RXN-23"
entity_type: "reaction"
name: "2-oxoglutarate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-23"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-oxoglutarate:proton symport

`reaction.ecocyc.TRANS-RXN-23`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-23`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + 2-KETOGLUTARATE -> PROTON + 2-KETOGLUTARATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + 2-KETOGLUTARATE -> PROTON + 2-KETOGLUTARATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by kgtP (protein.P0AEX3). Substrates: 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080). Products: 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Annotation

PROTON + 2-KETOGLUTARATE -> PROTON + 2-KETOGLUTARATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEX3|protein.P0AEX3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-23`

## Notes

PROTON + 2-KETOGLUTARATE -> PROTON + 2-KETOGLUTARATE; direction=REVERSIBLE
