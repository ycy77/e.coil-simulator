---
entity_id: "reaction.ecocyc.RXN0-7489"
entity_type: "reaction"
name: "RXN0-7489"
source_database: "EcoCyc"
source_id: "RXN0-7489"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7489

`reaction.ecocyc.RXN0-7489`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7489`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD-17947 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD-17947 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ycbB (protein.P22525), ynhG (protein.P76193). Substrates: a donor peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE), an acceptor peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE). Products: D-Alanine (molecule.C00133), a peptidoglycan with L,D cross links (meso-diaminopimelate containing) (molecule.ecocyc.CPD-17947).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD-17947 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P22525|protein.P22525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76193|protein.P76193]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17947|molecule.ecocyc.CPD-17947]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE|molecule.ecocyc.A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE|molecule.ecocyc.AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-22376|molecule.ecocyc.CPD-22376]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9231|molecule.ecocyc.CPD-9231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2600|molecule.ecocyc.CPD0-2600]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2611|molecule.ecocyc.CPD0-2611]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7489`

## Notes

A-DONOR-PG-WITH-MESODAP-TETRAPEPTIDE + AN-ACCEPTOR-PG-WITH-MESODAP-TETRAPEPTIDE -> CPD-17947 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
