---
entity_id: "reaction.ecocyc.TRANS-RXN0-448"
entity_type: "reaction"
name: "TRANS-RXN0-448"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-448"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-448

`reaction.ecocyc.TRANS-RXN0-448`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-448`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Labeled 1-deoxy-D-xylulose, added to the culture medium, is incorporated into the ubiquinone of wild type E.coli EcoCyc reaction equation: CPD-1093 -> CPD-1093; direction=LEFT-TO-RIGHT. Labeled 1-deoxy-D-xylulose, added to the culture medium, is incorporated into the ubiquinone of wild type E.coli

## Biological Role

Substrates: 1-deoxy-D-xylulose (molecule.ecocyc.CPD-1093). Products: 1-deoxy-D-xylulose (molecule.ecocyc.CPD-1093).

## Annotation

Labeled 1-deoxy-D-xylulose, added to the culture medium, is incorporated into the ubiquinone of wild type E.coli

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-1093|molecule.ecocyc.CPD-1093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-1093|molecule.ecocyc.CPD-1093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-448`

## Notes

CPD-1093 -> CPD-1093; direction=LEFT-TO-RIGHT
