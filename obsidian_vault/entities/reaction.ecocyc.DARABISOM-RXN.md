---
entity_id: "reaction.ecocyc.DARABISOM-RXN"
entity_type: "reaction"
name: "DARABISOM-RXN"
source_database: "EcoCyc"
source_id: "DARABISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DARABISOM-RXN

`reaction.ecocyc.DARABISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DARABISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Both E. coli strains B and K-12 can metabolize the uncommon pentose D-arabinose. In the first reaction both strains utilize L-fucose isomerase. EcoCyc reaction equation: D-arabinopyranose -> D-RIBULOSE; direction=REVERSIBLE. Both E. coli strains B and K-12 can metabolize the uncommon pentose D-arabinose. In the first reaction both strains utilize L-fucose isomerase.

## Biological Role

Catalyzed by L-fucose isomerase (complex.ecocyc.CPLX0-7631). Substrates: D-Arabinose (molecule.C00216). Products: D-Ribulose (molecule.C00309).

## Enriched Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Annotation

Both E. coli strains B and K-12 can metabolize the uncommon pentose D-arabinose. In the first reaction both strains utilize L-fucose isomerase.

## Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7631|complex.ecocyc.CPLX0-7631]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00309|molecule.C00309]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00474|molecule.C00474]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00532|molecule.C00532]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01697|molecule.C01697]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DARABISOM-RXN`

## Notes

D-arabinopyranose -> D-RIBULOSE; direction=REVERSIBLE
