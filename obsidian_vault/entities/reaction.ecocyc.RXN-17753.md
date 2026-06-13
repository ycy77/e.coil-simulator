---
entity_id: "reaction.ecocyc.RXN-17753"
entity_type: "reaction"
name: "RXN-17753"
source_database: "EcoCyc"
source_id: "RXN-17753"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR|CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17753

`reaction.ecocyc.RXN-17753`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17753`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR|CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

CARBAMOYL-P -> CPD-69 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CARBAMOYL-P -> CPD-69 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Carbamoyl phosphate (molecule.C00169). Products: H+ (molecule.C00080), Cyanate (molecule.C01417), phosphate (molecule.ecocyc.Pi).

## Annotation

CARBAMOYL-P -> CPD-69 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00169|molecule.C00169]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17753`

## Notes

CARBAMOYL-P -> CPD-69 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
