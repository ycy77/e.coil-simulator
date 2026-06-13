---
entity_id: "reaction.ecocyc.RXN-17634"
entity_type: "reaction"
name: "RXN-17634"
source_database: "EcoCyc"
source_id: "RXN-17634"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17634

`reaction.ecocyc.RXN-17634`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17634`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Cysteine-Hemithioacetal + WATER -> PROT-CYS + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Cysteine-Hemithioacetal + WATER -> PROT-CYS + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein/nucleic acid deglycase 1 (complex.ecocyc.CPLX0-861). Substrates: H2O (molecule.C00001), an S-(1-hydroxy-2-oxopropyl)-[protein]-L-cysteine (molecule.ecocyc.Protein-Cysteine-Hemithioacetal). Products: H+ (molecule.C00080), (R)-Lactate (molecule.C00256), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS).

## Annotation

Protein-Cysteine-Hemithioacetal + WATER -> PROT-CYS + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-861|complex.ecocyc.CPLX0-861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Cysteine-Hemithioacetal|molecule.ecocyc.Protein-Cysteine-Hemithioacetal]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17634`

## Notes

Protein-Cysteine-Hemithioacetal + WATER -> PROT-CYS + D-LACTATE + PROTON; direction=LEFT-TO-RIGHT
