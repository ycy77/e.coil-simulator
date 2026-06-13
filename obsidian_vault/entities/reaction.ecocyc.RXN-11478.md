---
entity_id: "reaction.ecocyc.RXN-11478"
entity_type: "reaction"
name: "RXN-11478"
source_database: "EcoCyc"
source_id: "RXN-11478"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11478

`reaction.ecocyc.RXN-11478`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11478`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glutaryl-ACP-methyl-esters + NAD -> Enoylglutaryl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: Glutaryl-ACP-methyl-esters + NAD -> Enoylglutaryl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Glutaryl-ACP-methyl-esters + NAD -> Enoylglutaryl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT

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

- `EcoCyc:RXN-11478`

## Notes

Glutaryl-ACP-methyl-esters + NAD -> Enoylglutaryl-ACP-methyl-esters + NADH + PROTON; direction=RIGHT-TO-LEFT
