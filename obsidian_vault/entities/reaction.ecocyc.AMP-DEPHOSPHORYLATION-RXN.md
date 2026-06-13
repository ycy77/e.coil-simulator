---
entity_id: "reaction.ecocyc.AMP-DEPHOSPHORYLATION-RXN"
entity_type: "reaction"
name: "AMP-DEPHOSPHORYLATION-RXN"
source_database: "EcoCyc"
source_id: "AMP-DEPHOSPHORYLATION-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMP-DEPHOSPHORYLATION-RXN

`reaction.ecocyc.AMP-DEPHOSPHORYLATION-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMP-DEPHOSPHORYLATION-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

AMP + WATER -> ADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: AMP + WATER -> ADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), AMP (molecule.C00020). Products: Adenosine (molecule.C00212), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Annotation

AMP + WATER -> ADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AMP-DEPHOSPHORYLATION-RXN`

## Notes

AMP + WATER -> ADENOSINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
