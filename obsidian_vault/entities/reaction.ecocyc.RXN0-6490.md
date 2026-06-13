---
entity_id: "reaction.ecocyc.RXN0-6490"
entity_type: "reaction"
name: "RXN0-6490"
source_database: "EcoCyc"
source_id: "RXN0-6490"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6490

`reaction.ecocyc.RXN0-6490`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6490`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The redox potential is very speculative, but it should be less than for the MQ/MQ2 couple, if the overall electron transfer reaction for dihydroorotate dehydrogenase is supposed to proceed in E. coli. EcoCyc reaction equation: OROTATE + PROTON + E- -> DI-H-OROTATE; direction=LEFT-TO-RIGHT. The redox potential is very speculative, but it should be less than for the MQ/MQ2 couple, if the overall electron transfer reaction for dihydroorotate dehydrogenase is supposed to proceed in E. coli.

## Biological Role

Substrates: H+ (molecule.C00080), Orotate (molecule.C00295). Products: (S)-Dihydroorotate (molecule.C00337).

## Annotation

The redox potential is very speculative, but it should be less than for the MQ/MQ2 couple, if the overall electron transfer reaction for dihydroorotate dehydrogenase is supposed to proceed in E. coli.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00337|molecule.C00337]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6490`

## Notes

OROTATE + PROTON + E- -> DI-H-OROTATE; direction=LEFT-TO-RIGHT
