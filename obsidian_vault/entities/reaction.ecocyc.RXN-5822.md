---
entity_id: "reaction.ecocyc.RXN-5822"
entity_type: "reaction"
name: "RXN-5822"
source_database: "EcoCyc"
source_id: "RXN-5822"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-5822

`reaction.ecocyc.RXN-5822`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-5822`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This reaction is part of the alternation of NAD and NADP. EcoCyc reaction equation: NADP + WATER -> NAD + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the alternation of NAD and NADP.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), NADPPHOSPHAT-MONOMER (protein.ecocyc.NADPPHOSPHAT-MONOMER). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006). Products: NAD+ (molecule.C00003), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Annotation

This reaction is part of the alternation of NAD and NADP.

## Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.ecocyc.NADPPHOSPHAT-MONOMER|protein.ecocyc.NADPPHOSPHAT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-5822`

## Notes

NADP + WATER -> NAD + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
