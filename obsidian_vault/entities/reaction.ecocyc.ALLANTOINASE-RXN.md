---
entity_id: "reaction.ecocyc.ALLANTOINASE-RXN"
entity_type: "reaction"
name: "ALLANTOINASE-RXN"
source_database: "EcoCyc"
source_id: "ALLANTOINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALLANTOINASE-RXN

`reaction.ecocyc.ALLANTOINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALLANTOINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ALLANTOIN + WATER -> PROTON + ALLANTOATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S-ALLANTOIN + WATER -> PROTON + ALLANTOATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by allantoinase (complex.ecocyc.CPLX-64). Substrates: H2O (molecule.C00001), (S)-Allantoin (molecule.C02350). Products: H+ (molecule.C00080), Allantoate (molecule.C00499).

## Enriched Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Annotation

S-ALLANTOIN + WATER -> PROTON + ALLANTOATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5698` allantoin degradation to ureidoglycolate II (ammonia producing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX-64|complex.ecocyc.CPLX-64]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00499|molecule.C00499]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02350|molecule.C02350]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALLANTOINASE-RXN`

## Notes

S-ALLANTOIN + WATER -> PROTON + ALLANTOATE; direction=LEFT-TO-RIGHT
