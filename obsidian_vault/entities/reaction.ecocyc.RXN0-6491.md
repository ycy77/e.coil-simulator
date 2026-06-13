---
entity_id: "reaction.ecocyc.RXN0-6491"
entity_type: "reaction"
name: "dihydroorotate dehydrogenase"
source_database: "EcoCyc"
source_id: "RXN0-6491"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dihydroorotate dehydrogenase

`reaction.ecocyc.RXN0-6491`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6491`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DI-H-OROTATE + Ubiquinones -> OROTATE + Ubiquinols; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DI-H-OROTATE + Ubiquinones -> OROTATE + Ubiquinols; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrD (protein.P0A7E1). Substrates: (S)-Dihydroorotate (molecule.C00337), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: Orotate (molecule.C00295), Ubiquinol (molecule.C00390).

## Annotation

DI-H-OROTATE + Ubiquinones -> OROTATE + Ubiquinols; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A7E1|protein.P0A7E1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00337|molecule.C00337]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6491`

## Notes

DI-H-OROTATE + Ubiquinones -> OROTATE + Ubiquinols; direction=LEFT-TO-RIGHT
