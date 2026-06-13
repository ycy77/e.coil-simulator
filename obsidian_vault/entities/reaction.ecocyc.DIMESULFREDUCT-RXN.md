---
entity_id: "reaction.ecocyc.DIMESULFREDUCT-RXN"
entity_type: "reaction"
name: "DIMESULFREDUCT-RXN"
source_database: "EcoCyc"
source_id: "DIMESULFREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIMESULFREDUCT-RXN

`reaction.ecocyc.DIMESULFREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIMESULFREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This is a terminal reductase during anaerobic growth. EcoCyc reaction equation: Menaquinones + CPD-7670 + WATER -> Menaquinols + DMSO; direction=PHYSIOL-RIGHT-TO-LEFT. This is a terminal reductase during anaerobic growth.

## Biological Role

Catalyzed by dimethyl sulfoxide reductase (complex.ecocyc.DIMESULFREDUCT-CPLX). Substrates: H2O (molecule.C00001), Dimethyl sulfide (molecule.C00580), Menaquinone (molecule.C00828). Products: Menaquinol (molecule.C05819), Dimethyl sulfoxide (molecule.C11143).

## Enriched Pathways

- `ecocyc.PWY0-1348` NADH to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1356` formate to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1577` hydrogen to dimethyl sulfoxide electron transfer (EcoCyc)

## Annotation

This is a terminal reductase during anaerobic growth.

## Pathways

- `ecocyc.PWY0-1348` NADH to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1356` formate to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1577` hydrogen to dimethyl sulfoxide electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.DIMESULFREDUCT-CPLX|complex.ecocyc.DIMESULFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11143|molecule.C11143]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00580|molecule.C00580]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIMESULFREDUCT-RXN`

## Notes

Menaquinones + CPD-7670 + WATER -> Menaquinols + DMSO; direction=PHYSIOL-RIGHT-TO-LEFT
