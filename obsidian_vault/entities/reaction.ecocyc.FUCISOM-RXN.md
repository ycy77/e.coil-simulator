---
entity_id: "reaction.ecocyc.FUCISOM-RXN"
entity_type: "reaction"
name: "FUCISOM-RXN"
source_database: "EcoCyc"
source_id: "FUCISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FUCISOM-RXN

`reaction.ecocyc.FUCISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FUCISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step in fucose catabolism. EcoCyc reaction equation: CPD-10329 -> L-FUCULOSE; direction=REVERSIBLE. The first step in fucose catabolism.

## Biological Role

Catalyzed by L-fucose isomerase (complex.ecocyc.CPLX0-7631). Substrates: alpha-L-Fucopyranose (molecule.C20835). Products: L-Fuculose (molecule.C01721).

## Enriched Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Annotation

The first step in fucose catabolism.

## Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7631|complex.ecocyc.CPLX0-7631]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01721|molecule.C01721]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20835|molecule.C20835]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FUCISOM-RXN`

## Notes

CPD-10329 -> L-FUCULOSE; direction=REVERSIBLE
