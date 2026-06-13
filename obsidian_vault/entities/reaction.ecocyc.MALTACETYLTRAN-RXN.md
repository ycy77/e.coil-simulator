---
entity_id: "reaction.ecocyc.MALTACETYLTRAN-RXN"
entity_type: "reaction"
name: "MALTACETYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "MALTACETYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALTACETYLTRAN-RXN

`reaction.ecocyc.MALTACETYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALTACETYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction acetylates free sugars in the cell, perhaps playing a detoxifying role. EcoCyc reaction equation: MALTOSE + ACETYL-COA -> CPD-18529 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction acetylates free sugars in the cell, perhaps playing a detoxifying role.

## Biological Role

Catalyzed by maltose O-acetyltransferase (complex.ecocyc.MALTACETYLTRAN-CPLX). Substrates: Acetyl-CoA (molecule.C00024), Maltose (molecule.C00208). Products: CoA (molecule.C00010), 6-O-acetyl-α-D-glucopyranosyl-(1→4)-D-glucose (molecule.ecocyc.CPD-18529).

## Annotation

This reaction acetylates free sugars in the cell, perhaps playing a detoxifying role.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.MALTACETYLTRAN-CPLX|complex.ecocyc.MALTACETYLTRAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18529|molecule.ecocyc.CPD-18529]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALTACETYLTRAN-RXN`

## Notes

MALTOSE + ACETYL-COA -> CPD-18529 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
