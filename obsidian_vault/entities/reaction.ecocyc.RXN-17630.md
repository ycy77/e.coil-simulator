---
entity_id: "reaction.ecocyc.RXN-17630"
entity_type: "reaction"
name: "RXN-17630"
source_database: "EcoCyc"
source_id: "RXN-17630"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17630

`reaction.ecocyc.RXN-17630`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17630`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Arginine-Aminocarbinol + WATER -> Protein-L-Arginines + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Arginine-Aminocarbinol + WATER -> Protein-L-Arginines + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein/nucleic acid deglycase 1 (complex.ecocyc.CPLX0-861). Substrates: H2O (molecule.C00001), an Nω-(1-hydroxy-2-oxopropyl)-[protein]-L-arginine (molecule.ecocyc.Protein-Arginine-Aminocarbinol). Products: H+ (molecule.C00080), (R)-Lactate (molecule.C00256), a [protein]-L-arginine (molecule.ecocyc.Protein-L-Arginines).

## Annotation

Protein-Arginine-Aminocarbinol + WATER -> Protein-L-Arginines + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-861|complex.ecocyc.CPLX0-861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-Arginines|molecule.ecocyc.Protein-L-Arginines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Arginine-Aminocarbinol|molecule.ecocyc.Protein-Arginine-Aminocarbinol]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17630`

## Notes

Protein-Arginine-Aminocarbinol + WATER -> Protein-L-Arginines + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT
