---
entity_id: "reaction.ecocyc.RXN-24006"
entity_type: "reaction"
name: "RXN-24006"
source_database: "EcoCyc"
source_id: "RXN-24006"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24006

`reaction.ecocyc.RXN-24006`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24006`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Dithiols + Ox-Thioredoxin -> Protein-Disulfides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Protein-Dithiols + Ox-Thioredoxin -> Protein-Disulfides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dsbD (protein.P36655). Substrates: a [protein]-dithiol (molecule.ecocyc.Protein-Dithiols). Products: a [protein]-disulfide (molecule.ecocyc.Protein-Disulfides).

## Enriched Pathways

- `ecocyc.THIOREDOX-PWY` thioredoxin pathway (NADPH) (EcoCyc)

## Annotation

Protein-Dithiols + Ox-Thioredoxin -> Protein-Disulfides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.THIOREDOX-PWY` thioredoxin pathway (NADPH) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P36655|protein.P36655]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-Disulfides|molecule.ecocyc.Protein-Disulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-Dithiols|molecule.ecocyc.Protein-Dithiols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24006`

## Notes

Protein-Dithiols + Ox-Thioredoxin -> Protein-Disulfides + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
