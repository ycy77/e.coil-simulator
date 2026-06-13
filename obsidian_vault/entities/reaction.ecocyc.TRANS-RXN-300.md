---
entity_id: "reaction.ecocyc.TRANS-RXN-300"
entity_type: "reaction"
name: "succinate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-300"
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

`reaction.ecocyc.TRANS-RXN-300`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-300`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SUC + PROTON -> SUC + PROTON; direction=REVERSIBLE EcoCyc reaction equation: SUC + PROTON -> SUC + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuC (protein.P0ABP3). Substrates: Succinate (molecule.C00042), H+ (molecule.C00080). Products: Succinate (molecule.C00042), H+ (molecule.C00080).

## Annotation

SUC + PROTON -> SUC + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABP3|protein.P0ABP3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-300`

## Notes

SUC + PROTON -> SUC + PROTON; direction=REVERSIBLE
