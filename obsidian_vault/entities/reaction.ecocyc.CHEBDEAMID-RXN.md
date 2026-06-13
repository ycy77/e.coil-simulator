---
entity_id: "reaction.ecocyc.CHEBDEAMID-RXN"
entity_type: "reaction"
name: "CHEBDEAMID-RXN"
source_database: "EcoCyc"
source_id: "CHEBDEAMID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "GLUTAMINYLPEPTIDE GLUTAMINASE"
  - "PEPTIDOGLUTAMINASE II"
---

# CHEBDEAMID-RXN

`reaction.ecocyc.CHEBDEAMID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHEBDEAMID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + Protein-L-glutamine -> Protein-alpha-L-Glutamates + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Protein-L-glutamine -> Protein-alpha-L-Glutamates + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cheB (protein.P07330). Substrates: H2O (molecule.C00001), a [protein]-L-glutamine (molecule.ecocyc.Protein-L-glutamine). Products: ammonium (molecule.ecocyc.AMMONIUM), a [protein]-α-L-glutamate (molecule.ecocyc.Protein-alpha-L-Glutamates).

## Annotation

WATER + Protein-L-glutamine -> Protein-alpha-L-Glutamates + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07330|protein.P07330]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-alpha-L-Glutamates|molecule.ecocyc.Protein-alpha-L-Glutamates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-glutamine|molecule.ecocyc.Protein-L-glutamine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CHEBDEAMID-RXN`

## Notes

WATER + Protein-L-glutamine -> Protein-alpha-L-Glutamates + AMMONIUM; direction=LEFT-TO-RIGHT
