---
entity_id: "reaction.ecocyc.GALPMUT-RXN"
entity_type: "reaction"
name: "GALPMUT-RXN"
source_database: "EcoCyc"
source_id: "GALPMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALPMUT-RXN

`reaction.ecocyc.GALPMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALPMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes UDP-galactofuranose, part of the O antigen. EcoCyc reaction equation: CPD-14553 -> UDP-D-GALACTO-14-FURANOSE; direction=REVERSIBLE. This reaction synthesizes UDP-galactofuranose, part of the O antigen.

## Biological Role

Catalyzed by UDP-galactopyranose mutase (complex.ecocyc.CPLX0-8582). Substrates: UDP-alpha-D-galactose (molecule.C00052). Products: UDP-alpha-D-galactofuranose (molecule.C03733).

## Enriched Pathways

- `ecocyc.OANTIGEN-PWY` O-antigen building blocks biosynthesis (E. coli) (EcoCyc)

## Annotation

This reaction synthesizes UDP-galactofuranose, part of the O antigen.

## Pathways

- `ecocyc.OANTIGEN-PWY` O-antigen building blocks biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8582|complex.ecocyc.CPLX0-8582]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03733|molecule.C03733]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1053|molecule.ecocyc.CPD0-1053]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GALPMUT-RXN`

## Notes

CPD-14553 -> UDP-D-GALACTO-14-FURANOSE; direction=REVERSIBLE
