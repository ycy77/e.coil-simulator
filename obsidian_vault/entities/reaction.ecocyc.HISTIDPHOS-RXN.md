---
entity_id: "reaction.ecocyc.HISTIDPHOS-RXN"
entity_type: "reaction"
name: "HISTIDPHOS-RXN"
source_database: "EcoCyc"
source_id: "HISTIDPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HISTIDPHOS-RXN

`reaction.ecocyc.HISTIDPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HISTIDPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This is the ninth step of the histidine biosynthesis pathway EcoCyc reaction equation: L-HISTIDINOL-P + WATER -> HISTIDINOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This is the ninth step of the histidine biosynthesis pathway

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase (complex.ecocyc.IMIDHISTID-CPLX). Substrates: H2O (molecule.C00001), L-Histidinol phosphate (molecule.C01100). Products: L-Histidinol (molecule.C00860), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

This is the ninth step of the histidine biosynthesis pathway

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.IMIDHISTID-CPLX|complex.ecocyc.IMIDHISTID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00860|molecule.C00860]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01100|molecule.C01100]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00860|molecule.C00860]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HISTIDPHOS-RXN`

## Notes

L-HISTIDINOL-P + WATER -> HISTIDINOL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
