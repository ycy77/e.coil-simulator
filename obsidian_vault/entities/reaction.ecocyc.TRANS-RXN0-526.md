---
entity_id: "reaction.ecocyc.TRANS-RXN0-526"
entity_type: "reaction"
name: "TRANS-RXN0-526"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-526"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-526

`reaction.ecocyc.TRANS-RXN0-526`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-526`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

EG10719-MONOMER activity in E. coli K-12 results in the production of methane which can be detected in the headspace of liquid cultures grown in minimal media with phosphonate as sole carbon source . EcoCyc reaction equation: CH4 -> CH4; direction=LEFT-TO-RIGHT. EG10719-MONOMER activity in E. coli K-12 results in the production of methane which can be detected in the headspace of liquid cultures grown in minimal media with phosphonate as sole carbon source .

## Biological Role

Substrates: Methane (molecule.C01438). Products: Methane (molecule.C01438).

## Annotation

EG10719-MONOMER activity in E. coli K-12 results in the production of methane which can be detected in the headspace of liquid cultures grown in minimal media with phosphonate as sole carbon source .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C01438|molecule.C01438]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01438|molecule.C01438]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-526`

## Notes

CH4 -> CH4; direction=LEFT-TO-RIGHT
