---
entity_id: "reaction.ecocyc.ABC-22-RXN"
entity_type: "reaction"
name: "ABC-22-RXN"
source_database: "EcoCyc"
source_id: "ABC-22-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ABC-22-RXN

`reaction.ecocyc.ABC-22-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ABC-22-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ATP + Peptides + WATER -> ADP + Pi + Peptides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + Peptides + WATER -> ADP + Pi + Peptides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ATP (molecule.C00002), a peptide (molecule.ecocyc.Peptides). Products: ADP (molecule.C00008), H+ (molecule.C00080), a peptide (molecule.ecocyc.Peptides), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + Peptides + WATER -> ADP + Pi + Peptides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Peptides|molecule.ecocyc.Peptides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Peptides|molecule.ecocyc.Peptides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ABC-22-RXN`

## Notes

ATP + Peptides + WATER -> ADP + Pi + Peptides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
