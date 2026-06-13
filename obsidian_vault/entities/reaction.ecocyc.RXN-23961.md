---
entity_id: "reaction.ecocyc.RXN-23961"
entity_type: "reaction"
name: "RXN-23961"
source_database: "EcoCyc"
source_id: "RXN-23961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23961

`reaction.ecocyc.RXN-23961`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alanine—tRNA ligase/DNA-binding transcriptional repressor (complex.ecocyc.ALAS-CPLX). Substrates: H2O (molecule.C00001). Products: L-Serine (molecule.C00065), H+ (molecule.C00080).

## Annotation

seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.ALAS-CPLX|complex.ecocyc.ALAS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23961`

## Notes

seryl-tRNAAla + WATER -> ALA-tRNAs + SER + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
