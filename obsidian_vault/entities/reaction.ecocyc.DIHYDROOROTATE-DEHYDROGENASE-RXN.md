---
entity_id: "reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "DIHYDROOROTATE-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROOROTATE-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDROOROTATE-DEHYDROGENASE-RXN

`reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROOROTATE-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + DI-H-OROTATE -> ETR-Quinols + OROTATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ETR-Quinones + DI-H-OROTATE -> ETR-Quinols + OROTATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyrD (protein.P0A7E1). Substrates: (S)-Dihydroorotate (molecule.C00337). Products: Orotate (molecule.C00295).

## Enriched Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

ETR-Quinones + DI-H-OROTATE -> ETR-Quinols + OROTATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7E1|protein.P0A7E1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00337|molecule.C00337]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDROOROTATE-DEHYDROGENASE-RXN`

## Notes

ETR-Quinones + DI-H-OROTATE -> ETR-Quinols + OROTATE; direction=LEFT-TO-RIGHT
