---
entity_id: "reaction.ecocyc.3.1.26.3-RXN"
entity_type: "reaction"
name: "3.1.26.3-RXN"
source_database: "EcoCyc"
source_id: "3.1.26.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "RNase O"
  - "RNase D"
---

# 3.1.26.3-RXN

`reaction.ecocyc.3.1.26.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.26.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the endonucleolytic cleavage of double-stranded RNA to yield a 5'-phosphate and a 3'-hydroxyl. EcoCyc reaction equation: RNASE-III-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-III-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the endonucleolytic cleavage of double-stranded RNA to yield a 5'-phosphate and a 3'-hydroxyl.

## Biological Role

Catalyzed by RNase III (complex.ecocyc.CPLX0-3281). Substrates: H2O (molecule.C00001).

## Annotation

This reaction is the endonucleolytic cleavage of double-stranded RNA to yield a 5'-phosphate and a 3'-hydroxyl.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3281|complex.ecocyc.CPLX0-3281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.26.3-RXN`

## Notes

RNASE-III-MRNA-PROCESSING-SUBSTRATE + WATER -> RNASE-III-PROCESSING-PRODUCT-MRNA + mRNA-Fragments; direction=PHYSIOL-LEFT-TO-RIGHT
