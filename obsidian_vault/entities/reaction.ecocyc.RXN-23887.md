---
entity_id: "reaction.ecocyc.RXN-23887"
entity_type: "reaction"
name: "RXN-23887"
source_database: "EcoCyc"
source_id: "RXN-23887"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23887

`reaction.ecocyc.RXN-23887`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23887`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Amino-Acid-Adenylates + tRNAs -> Charged-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Amino-Acid-Adenylates + tRNAs -> Charged-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an adenylated L-amino acid (molecule.ecocyc.L-Amino-Acid-Adenylates). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

L-Amino-Acid-Adenylates + tRNAs -> Charged-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Amino-Acid-Adenylates|molecule.ecocyc.L-Amino-Acid-Adenylates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23887`

## Notes

L-Amino-Acid-Adenylates + tRNAs -> Charged-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
