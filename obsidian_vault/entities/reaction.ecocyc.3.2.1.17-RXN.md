---
entity_id: "reaction.ecocyc.3.2.1.17-RXN"
entity_type: "reaction"
name: "3.2.1.17-RXN"
source_database: "EcoCyc"
source_id: "3.2.1.17-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Muramidase"
---

# 3.2.1.17-RXN

`reaction.ecocyc.3.2.1.17-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.1.17-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Peptidoglycans + WATER -> Peptide-Peptidoglycan-NAcMur + Peptidoglycan-GlcNAC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Peptidoglycans + WATER -> Peptide-Peptidoglycan-NAcMur + Peptidoglycan-GlcNAC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rrrD (protein.P78285). Substrates: H2O (molecule.C00001), a peptidoglycan (molecule.ecocyc.Peptidoglycans). Products: a peptidoglycan with N-acetylmuramoyl-pentapeptide at the reducing end (molecule.ecocyc.Peptide-Peptidoglycan-NAcMur), a peptidoglycan with N-acetyl-β-D-glucosamine at the non-reducing end (molecule.ecocyc.Peptidoglycan-GlcNAC).

## Annotation

Peptidoglycans + WATER -> Peptide-Peptidoglycan-NAcMur + Peptidoglycan-GlcNAC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P78285|protein.P78285]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Peptide-Peptidoglycan-NAcMur|molecule.ecocyc.Peptide-Peptidoglycan-NAcMur]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Peptidoglycan-GlcNAC|molecule.ecocyc.Peptidoglycan-GlcNAC]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Peptidoglycans|molecule.ecocyc.Peptidoglycans]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.1.17-RXN`

## Notes

Peptidoglycans + WATER -> Peptide-Peptidoglycan-NAcMur + Peptidoglycan-GlcNAC; direction=PHYSIOL-LEFT-TO-RIGHT
