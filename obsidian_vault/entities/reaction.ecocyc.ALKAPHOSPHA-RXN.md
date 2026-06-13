---
entity_id: "reaction.ecocyc.ALKAPHOSPHA-RXN"
entity_type: "reaction"
name: "ALKAPHOSPHA-RXN"
source_database: "EcoCyc"
source_id: "ALKAPHOSPHA-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALKAPHOSPHA-RXN

`reaction.ecocyc.ALKAPHOSPHA-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALKAPHOSPHA-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction is part of the phosphate acquisition and transport system in the cell. EcoCyc reaction equation: Orthophosphoric-Monoesters + WATER -> Alcohols + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the phosphate acquisition and transport system in the cell.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Orthophosphoric monoester (molecule.C01153). Products: an alcohol (molecule.ecocyc.Alcohols), phosphate (molecule.ecocyc.Pi).

## Annotation

This reaction is part of the phosphate acquisition and transport system in the cell.

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01153|molecule.C01153]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06232|molecule.C06232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C20679|molecule.C20679]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4422|molecule.ecocyc.CPD-4422]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4584|molecule.ecocyc.CPD-4584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.THIOGLYCOLATE|molecule.ecocyc.THIOGLYCOLATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALKAPHOSPHA-RXN`

## Notes

Orthophosphoric-Monoesters + WATER -> Alcohols + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
