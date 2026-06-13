---
entity_id: "reaction.ecocyc.RXN0-3543"
entity_type: "reaction"
name: "RXN0-3543"
source_database: "EcoCyc"
source_id: "RXN0-3543"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3543

`reaction.ecocyc.RXN0-3543`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3543`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + WATER -> PROTON + AMINO-HYDROXYMETHYL-METHYL-PYR-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + WATER -> PROTON + AMINO-HYDROXYMETHYL-METHYL-PYR-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudJ (protein.P0AEI6), cof (protein.P46891). Substrates: H2O (molecule.C00001), 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate (molecule.C04752). Products: H+ (molecule.C00080), 4-Amino-2-methyl-5-(phosphooxymethyl)pyrimidine (molecule.C04556), phosphate (molecule.ecocyc.Pi).

## Annotation

AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + WATER -> PROTON + AMINO-HYDROXYMETHYL-METHYL-PYR-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AEI6|protein.P0AEI6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P46891|protein.P46891]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04556|molecule.C04556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04752|molecule.C04752]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3543`

## Notes

AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + WATER -> PROTON + AMINO-HYDROXYMETHYL-METHYL-PYR-P + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
