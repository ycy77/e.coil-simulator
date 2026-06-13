---
entity_id: "reaction.ecocyc.TRANS-RXN-146"
entity_type: "reaction"
name: "TRANS-RXN-146"
source_database: "EcoCyc"
source_id: "TRANS-RXN-146"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-146

`reaction.ecocyc.TRANS-RXN-146`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-146`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction represents flipping of an Und-PP linked O16-antigen repeat unit from the cytoplasmic face to the periplasmic face of the inner membrane EcoCyc reaction equation: CPD0-2279 -> CPD0-2279; direction=LEFT-TO-RIGHT. This reaction represents flipping of an Und-PP linked O16-antigen repeat unit from the cytoplasmic face to the periplasmic face of the inner membrane

## Biological Role

Substrates: β-D-Galf-(1→6)-α-D-Glc-(1→3)-α-L-Rha-(1→3)-α-D-GlcNAc-PP-Und (molecule.ecocyc.CPD0-2279). Products: β-D-Galf-(1→6)-α-D-Glc-(1→3)-α-L-Rha-(1→3)-α-D-GlcNAc-PP-Und (molecule.ecocyc.CPD0-2279).

## Annotation

This reaction represents flipping of an Und-PP linked O16-antigen repeat unit from the cytoplasmic face to the periplasmic face of the inner membrane

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-2279|molecule.ecocyc.CPD0-2279]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2279|molecule.ecocyc.CPD0-2279]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-146`

## Notes

CPD0-2279 -> CPD0-2279; direction=LEFT-TO-RIGHT
