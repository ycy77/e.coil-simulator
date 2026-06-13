---
entity_id: "reaction.ecocyc.RXN-11482"
entity_type: "reaction"
name: "RXN-11482"
source_database: "EcoCyc"
source_id: "RXN-11482"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11482

`reaction.ecocyc.RXN-11482`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11482`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pimeloyl-ACP-methyl-esters + NAD -> Enoylpimeloyl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: Pimeloyl-ACP-methyl-esters + NAD -> Enoylpimeloyl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Pimeloyl-ACP-methyl-esters + NAD -> Enoylpimeloyl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11482`

## Notes

Pimeloyl-ACP-methyl-esters + NAD -> Enoylpimeloyl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT
