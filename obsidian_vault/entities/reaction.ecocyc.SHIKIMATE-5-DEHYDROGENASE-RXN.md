---
entity_id: "reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "SHIKIMATE-5-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "SHIKIMATE-5-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SHIKIMATE-5-DEHYDROGENASE-RXN

`reaction.ecocyc.SHIKIMATE-5-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SHIKIMATE-5-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in the shikimate pathway. EcoCyc reaction equation: NADP + SHIKIMATE -> PROTON + NADPH + 3-DEHYDRO-SHIKIMATE; direction=PHYSIOL-RIGHT-TO-LEFT. This is the fourth step in the shikimate pathway.

## Biological Role

Catalyzed by aroE (protein.P15770). Substrates: NADP+ (molecule.C00006), Shikimate (molecule.C00493). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Dehydroshikimate (molecule.C02637).

## Enriched Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Annotation

This is the fourth step in the shikimate pathway.

## Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P15770|protein.P15770]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02637|molecule.C02637]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SHIKIMATE-5-DEHYDROGENASE-RXN`

## Notes

NADP + SHIKIMATE -> PROTON + NADPH + 3-DEHYDRO-SHIKIMATE; direction=PHYSIOL-RIGHT-TO-LEFT
