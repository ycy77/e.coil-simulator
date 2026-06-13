---
entity_id: "reaction.ecocyc.RXN-25083"
entity_type: "reaction"
name: "RXN-25083"
source_database: "EcoCyc"
source_id: "RXN-25083"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25083

`reaction.ecocyc.RXN-25083`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25083`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

IscU + FE+2 -> IscU-Fe; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: IscU + FE+2 -> IscU-Fe; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by iscU (protein.P0ACD4). Substrates: Fe2+ (molecule.C14818).

## Enriched Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Annotation

IscU + FE+2 -> IscU-Fe; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8566` [2Fe-2S] iron-sulfur cluster biosynthesis (bacterial IscS system) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0ACD4|protein.P0ACD4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25083`

## Notes

IscU + FE+2 -> IscU-Fe; direction=PHYSIOL-LEFT-TO-RIGHT
