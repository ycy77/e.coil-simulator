---
entity_id: "reaction.ecocyc.RXN-19726"
entity_type: "reaction"
name: "RXN-19726"
source_database: "EcoCyc"
source_id: "RXN-19726"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19726

`reaction.ecocyc.RXN-19726`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19726`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

glycyl-tRNAAla + WATER -> GLY + ALA-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: glycyl-tRNAAla + WATER -> GLY + ALA-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alanine—tRNA ligase/DNA-binding transcriptional repressor (complex.ecocyc.ALAS-CPLX), D-aminoacyl-tRNA deacylase (complex.ecocyc.CPLX0-3581). Substrates: H2O (molecule.C00001). Products: Glycine (molecule.C00037), H+ (molecule.C00080).

## Annotation

glycyl-tRNAAla + WATER -> GLY + ALA-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALAS-CPLX|complex.ecocyc.ALAS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3581|complex.ecocyc.CPLX0-3581]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19726`

## Notes

glycyl-tRNAAla + WATER -> GLY + ALA-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
