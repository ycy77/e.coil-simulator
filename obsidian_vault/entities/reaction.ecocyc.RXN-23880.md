---
entity_id: "reaction.ecocyc.RXN-23880"
entity_type: "reaction"
name: "RXN-23880"
source_database: "EcoCyc"
source_id: "RXN-23880"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23880

`reaction.ecocyc.RXN-23880`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23880`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Amino-Acids + ATP + PROTON -> L-Amino-Acid-Adenylates + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Amino-Acids + ATP + PROTON -> L-Amino-Acid-Adenylates + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Amino acid (molecule.C00151). Products: Diphosphate (molecule.C00013), an adenylated L-amino acid (molecule.ecocyc.L-Amino-Acid-Adenylates).

## Annotation

L-Amino-Acids + ATP + PROTON -> L-Amino-Acid-Adenylates + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-Amino-Acid-Adenylates|molecule.ecocyc.L-Amino-Acid-Adenylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00151|molecule.C00151]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23880`

## Notes

L-Amino-Acids + ATP + PROTON -> L-Amino-Acid-Adenylates + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
