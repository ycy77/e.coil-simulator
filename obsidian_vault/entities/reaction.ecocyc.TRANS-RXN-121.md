---
entity_id: "reaction.ecocyc.TRANS-RXN-121"
entity_type: "reaction"
name: "succinate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-121"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# succinate:proton symport

`reaction.ecocyc.TRANS-RXN-121`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-121`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + SUC -> PROTON + SUC; direction=REVERSIBLE EcoCyc reaction equation: PROTON + SUC -> PROTON + SUC; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830), satP (protein.P0AC98), dauA (protein.P0AFR2). Substrates: Succinate (molecule.C00042), H+ (molecule.C00080). Products: Succinate (molecule.C00042), H+ (molecule.C00080).

## Annotation

PROTON + SUC -> PROTON + SUC; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AC98|protein.P0AC98]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFR2|protein.P0AFR2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-121`

## Notes

PROTON + SUC -> PROTON + SUC; direction=REVERSIBLE
