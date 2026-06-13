---
entity_id: "reaction.ecocyc.GLYOXIII-RXN"
entity_type: "reaction"
name: "GLYOXIII-RXN"
source_database: "EcoCyc"
source_id: "GLYOXIII-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYOXIII-RXN

`reaction.ecocyc.GLYOXIII-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYOXIII-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction converts methylglyoxal directly into D-lactate without using glutathione. EcoCyc reaction equation: D-LACTATE + PROTON -> METHYL-GLYOXAL + WATER; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction converts methylglyoxal directly into D-lactate without using glutathione.

## Biological Role

Catalyzed by protein/nucleic acid deglycase 1 (complex.ecocyc.CPLX0-861), yhbO (protein.P45470). Substrates: H+ (molecule.C00080), (R)-Lactate (molecule.C00256). Products: H2O (molecule.C00001), Methylglyoxal (molecule.C00546).

## Annotation

This reaction converts methylglyoxal directly into D-lactate without using glutathione.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-861|complex.ecocyc.CPLX0-861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P45470|protein.P45470]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYOXIII-RXN`

## Notes

D-LACTATE + PROTON -> METHYL-GLYOXAL + WATER; direction=PHYSIOL-RIGHT-TO-LEFT
