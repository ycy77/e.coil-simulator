---
entity_id: "reaction.ecocyc.SHIKIMATE-KINASE-RXN"
entity_type: "reaction"
name: "SHIKIMATE-KINASE-RXN"
source_database: "EcoCyc"
source_id: "SHIKIMATE-KINASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SHIKIMATE-KINASE-RXN

`reaction.ecocyc.SHIKIMATE-KINASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SHIKIMATE-KINASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in the shikimate pathway EcoCyc reaction equation: SHIKIMATE + ATP -> PROTON + SHIKIMATE-5P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fifth step in the shikimate pathway

## Biological Role

Catalyzed by aroK (protein.P0A6D7), aroL (protein.P0A6E1). Substrates: ATP (molecule.C00002), Shikimate (molecule.C00493). Products: ADP (molecule.C00008), H+ (molecule.C00080), Shikimate 3-phosphate (molecule.C03175).

## Enriched Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Annotation

This is the fifth step in the shikimate pathway

## Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A6D7|protein.P0A6D7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6E1|protein.P0A6E1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03175|molecule.C03175]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SHIKIMATE-KINASE-RXN`

## Notes

SHIKIMATE + ATP -> PROTON + SHIKIMATE-5P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
