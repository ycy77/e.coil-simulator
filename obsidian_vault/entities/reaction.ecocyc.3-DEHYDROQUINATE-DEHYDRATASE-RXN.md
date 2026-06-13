---
entity_id: "reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "3-DEHYDROQUINATE-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "3-DEHYDROQUINATE-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-DEHYDROQUINATE-DEHYDRATASE-RXN

`reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-DEHYDROQUINATE-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in the shikimate pathway EcoCyc reaction equation: DEHYDROQUINATE -> WATER + 3-DEHYDRO-SHIKIMATE; direction=REVERSIBLE. This is the third step in the shikimate pathway

## Biological Role

Catalyzed by 3-dehydroquinate dehydratase (complex.ecocyc.AROD-CPLX). Substrates: 3-Dehydroquinate (molecule.C00944). Products: H2O (molecule.C00001), 3-Dehydroshikimate (molecule.C02637).

## Enriched Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Annotation

This is the third step in the shikimate pathway

## Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.AROD-CPLX|complex.ecocyc.AROD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02637|molecule.C02637]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00944|molecule.C00944]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00944|molecule.C00944]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BH4NA|molecule.ecocyc.BH4NA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-DEHYDROQUINATE-DEHYDRATASE-RXN`

## Notes

DEHYDROQUINATE -> WATER + 3-DEHYDRO-SHIKIMATE; direction=REVERSIBLE
