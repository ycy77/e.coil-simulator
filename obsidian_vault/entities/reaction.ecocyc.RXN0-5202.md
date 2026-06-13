---
entity_id: "reaction.ecocyc.RXN0-5202"
entity_type: "reaction"
name: "L-alanine:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-5202"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-alanine:proton symport

`reaction.ecocyc.RXN0-5202`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5202`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + L-ALPHA-ALANINE -> PROTON + L-ALPHA-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + L-ALPHA-ALANINE -> PROTON + L-ALPHA-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: L-Alanine (molecule.C00041), H+ (molecule.C00080). Products: L-Alanine (molecule.C00041), H+ (molecule.C00080).

## Annotation

PROTON + L-ALPHA-ALANINE -> PROTON + L-ALPHA-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5202`

## Notes

PROTON + L-ALPHA-ALANINE -> PROTON + L-ALPHA-ALANINE; direction=REVERSIBLE
