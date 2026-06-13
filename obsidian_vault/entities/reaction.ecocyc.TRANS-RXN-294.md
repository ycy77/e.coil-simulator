---
entity_id: "reaction.ecocyc.TRANS-RXN-294"
entity_type: "reaction"
name: "TRANS-RXN-294"
source_database: "EcoCyc"
source_id: "TRANS-RXN-294"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-294

`reaction.ecocyc.TRANS-RXN-294`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-294`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Represents (imperfectly) the flipping of lysophospholipids across the inner membrane. EcoCyc reaction equation: 2-ACYL-GPE -> 2-ACYL-GPE; direction=REVERSIBLE. Represents (imperfectly) the flipping of lysophospholipids across the inner membrane.

## Biological Role

Catalyzed by lplT (protein.P39196). Substrates: 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973). Products: 2-Acyl-sn-glycero-3-phosphoethanolamine (molecule.C05973).

## Annotation

Represents (imperfectly) the flipping of lysophospholipids across the inner membrane.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P39196|protein.P39196]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05973|molecule.C05973]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-294`

## Notes

2-ACYL-GPE -> 2-ACYL-GPE; direction=REVERSIBLE
