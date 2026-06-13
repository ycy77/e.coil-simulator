---
entity_id: "reaction.ecocyc.TRANS-RXN-16"
entity_type: "reaction"
name: "galactonate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-16"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# galactonate:proton symport

`reaction.ecocyc.TRANS-RXN-16`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-16`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + D-GALACTONATE -> PROTON + D-GALACTONATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + D-GALACTONATE -> PROTON + D-GALACTONATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by dgoT (protein.P0AA76). Substrates: H+ (molecule.C00080), D-Galactonate (molecule.C00880). Products: H+ (molecule.C00080), D-Galactonate (molecule.C00880).

## Annotation

PROTON + D-GALACTONATE -> PROTON + D-GALACTONATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AA76|protein.P0AA76]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00880|molecule.C00880]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00880|molecule.C00880]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20898|molecule.ecocyc.CPD-20898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-20899|molecule.ecocyc.CPD-20899]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-16`

## Notes

PROTON + D-GALACTONATE -> PROTON + D-GALACTONATE; direction=REVERSIBLE
