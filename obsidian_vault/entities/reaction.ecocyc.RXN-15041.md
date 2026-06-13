---
entity_id: "reaction.ecocyc.RXN-15041"
entity_type: "reaction"
name: "RXN-15041"
source_database: "EcoCyc"
source_id: "RXN-15041"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15041

`reaction.ecocyc.RXN-15041`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15041`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-aminoacyl-tRNAs + WATER -> D-Amino-Acids + tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-aminoacyl-tRNAs + WATER -> D-Amino-Acids + tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-aminoacyl-tRNA deacylase (complex.ecocyc.CPLX0-3581). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), a D-amino acid (molecule.ecocyc.D-Amino-Acids).

## Annotation

D-aminoacyl-tRNAs + WATER -> D-Amino-Acids + tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3581|complex.ecocyc.CPLX0-3581]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Amino-Acids|molecule.ecocyc.D-Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15041`

## Notes

D-aminoacyl-tRNAs + WATER -> D-Amino-Acids + tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
