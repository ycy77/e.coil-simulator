---
entity_id: "reaction.ecocyc.5.3.4.1-RXN"
entity_type: "reaction"
name: "5.3.4.1-RXN"
source_database: "EcoCyc"
source_id: "5.3.4.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-S REARRANGASE"
---

# 5.3.4.1-RXN

`reaction.ecocyc.5.3.4.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5.3.4.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

This reaction rearranges the disulfide bonds of proteins. EcoCyc reaction equation: Proteins-with-incorrect-disulfides -> Proteins-with-correct-disulfides; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction rearranges the disulfide bonds of proteins.

## Biological Role

Catalyzed by protein disulfide isomerase DsbC (complex.ecocyc.DSBC-CPLX), protein sulfenic acid reductase and chaperone DsbG (complex.ecocyc.DSBG-CPLX).

## Annotation

This reaction rearranges the disulfide bonds of proteins.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.DSBC-CPLX|complex.ecocyc.DSBC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DSBG-CPLX|complex.ecocyc.DSBG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## External IDs

- `EcoCyc:5.3.4.1-RXN`

## Notes

Proteins-with-incorrect-disulfides -> Proteins-with-correct-disulfides; direction=PHYSIOL-LEFT-TO-RIGHT
