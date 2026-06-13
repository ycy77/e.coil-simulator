---
entity_id: "reaction.ecocyc.RXN0-5227"
entity_type: "reaction"
name: "RXN0-5227"
source_database: "EcoCyc"
source_id: "RXN0-5227"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5227

`reaction.ecocyc.RXN0-5227`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5227`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

CPD0-1082 + WATER -> L-ALA-GAMMA-D-GLU-DAP + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1082 + WATER -> L-ALA-GAMMA-D-GLU-DAP + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by murein tetrapeptide carboxypeptidase (complex.ecocyc.CPLX0-8616). Substrates: H2O (molecule.C00001), L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine (molecule.ecocyc.CPD0-1082). Products: D-Alanine (molecule.C00133), L-alanyl-γ-D-glutamyl-meso-diaminopimelate (molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Annotation

CPD0-1082 + WATER -> L-ALA-GAMMA-D-GLU-DAP + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)
- `ecocyc.PWY0-1546` muropeptide degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8616|complex.ecocyc.CPLX0-8616]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP|molecule.ecocyc.L-ALA-GAMMA-D-GLU-DAP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1082|molecule.ecocyc.CPD0-1082]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5227`

## Notes

CPD0-1082 + WATER -> L-ALA-GAMMA-D-GLU-DAP + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
