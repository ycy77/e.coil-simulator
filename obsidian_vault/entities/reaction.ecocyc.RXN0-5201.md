---
entity_id: "reaction.ecocyc.RXN0-5201"
entity_type: "reaction"
name: "β-alanine:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-5201"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# β-alanine:proton symport

`reaction.ecocyc.RXN0-5201`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5201`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + B-ALANINE -> PROTON + B-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + B-ALANINE -> PROTON + B-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by cycA (protein.P0AAE0). Substrates: H+ (molecule.C00080), beta-Alanine (molecule.C00099). Products: H+ (molecule.C00080), beta-Alanine (molecule.C00099).

## Annotation

PROTON + B-ALANINE -> PROTON + B-ALANINE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AAE0|protein.P0AAE0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00099|molecule.C00099]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00099|molecule.C00099]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5201`

## Notes

PROTON + B-ALANINE -> PROTON + B-ALANINE; direction=REVERSIBLE
