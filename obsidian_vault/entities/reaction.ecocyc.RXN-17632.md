---
entity_id: "reaction.ecocyc.RXN-17632"
entity_type: "reaction"
name: "RXN-17632"
source_database: "EcoCyc"
source_id: "RXN-17632"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17632

`reaction.ecocyc.RXN-17632`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17632`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Lysine-Aminocarbinol + WATER -> Protein-L-lysine + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Lysine-Aminocarbinol + WATER -> Protein-L-lysine + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein/nucleic acid deglycase 3 (complex.ecocyc.CPLX0-7960), protein/nucleic acid deglycase 1 (complex.ecocyc.CPLX0-861), yhbO (protein.P45470). Substrates: H2O (molecule.C00001), an N6-(1-hydroxy-2-oxopropyl)-[protein]-L-lysine (molecule.ecocyc.Protein-Lysine-Aminocarbinol). Products: (R)-Lactate (molecule.C00256), Protein lysine (molecule.C02188).

## Annotation

Protein-Lysine-Aminocarbinol + WATER -> Protein-L-lysine + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7960|complex.ecocyc.CPLX0-7960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-861|complex.ecocyc.CPLX0-861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P45470|protein.P45470]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Lysine-Aminocarbinol|molecule.ecocyc.Protein-Lysine-Aminocarbinol]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17632`

## Notes

Protein-Lysine-Aminocarbinol + WATER -> Protein-L-lysine + D-LACTATE; direction=PHYSIOL-LEFT-TO-RIGHT
