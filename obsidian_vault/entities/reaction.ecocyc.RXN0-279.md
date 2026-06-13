---
entity_id: "reaction.ecocyc.RXN0-279"
entity_type: "reaction"
name: "RXN0-279"
source_database: "EcoCyc"
source_id: "RXN0-279"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-279

`reaction.ecocyc.RXN0-279`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-279`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-SULFINOALANINE + WATER -> PROTON + L-ALPHA-ALANINE + SO3; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-SULFINOALANINE + WATER -> PROTON + L-ALPHA-ALANINE + SO3; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cysteine sulfinate desulfinase (complex.ecocyc.CPLX0-7838). Substrates: H2O (molecule.C00001), 3-Sulfino-L-alanine (molecule.C00606). Products: L-Alanine (molecule.C00041), H+ (molecule.C00080), Sulfite (molecule.C00094).

## Annotation

3-SULFINOALANINE + WATER -> PROTON + L-ALPHA-ALANINE + SO3; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7838|complex.ecocyc.CPLX0-7838]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00606|molecule.C00606]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-279`

## Notes

3-SULFINOALANINE + WATER -> PROTON + L-ALPHA-ALANINE + SO3; direction=PHYSIOL-LEFT-TO-RIGHT
