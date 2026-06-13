---
entity_id: "reaction.ecocyc.GLUTAMATESYN-RXN"
entity_type: "reaction"
name: "GLUTAMATESYN-RXN"
source_database: "EcoCyc"
source_id: "GLUTAMATESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTAMATESYN-RXN

`reaction.ecocyc.GLUTAMATESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTAMATESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reaction is reductive amination of 2-oxoglutarate. It catalyzes the utilization of the amide nitrogen of glutamine in biosynthesis. EcoCyc reaction equation: GLT + NADP -> PROTON + GLN + 2-KETOGLUTARATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT. The reaction is reductive amination of 2-oxoglutarate. It catalyzes the utilization of the amide nitrogen of glutamine in biosynthesis.

## Biological Role

Catalyzed by glutamate synthase (complex.ecocyc.GLUTAMATESYN-CPLX). Substrates: NADP+ (molecule.C00006), L-Glutamate (molecule.C00025). Products: NADPH (molecule.C00005), 2-Oxoglutarate (molecule.C00026), L-Glutamine (molecule.C00064), H+ (molecule.C00080).

## Annotation

The reaction is reductive amination of 2-oxoglutarate. It catalyzes the utilization of the amide nitrogen of glutamine in biosynthesis.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.GLUTAMATESYN-CPLX|complex.ecocyc.GLUTAMATESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00217|molecule.C00217]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00402|molecule.C00402]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTAMATESYN-RXN`

## Notes

GLT + NADP -> PROTON + GLN + 2-KETOGLUTARATE + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
