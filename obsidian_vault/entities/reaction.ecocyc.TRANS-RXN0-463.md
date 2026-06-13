---
entity_id: "reaction.ecocyc.TRANS-RXN0-463"
entity_type: "reaction"
name: "TRANS-RXN0-463"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-463"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-463

`reaction.ecocyc.TRANS-RXN0-463`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-463`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

E. coli mutants which lack the ability to synthesize 5,6-dimethylbenzimidazole (DMB) are able to grow when supplied with exogenous DMB and cobinamide . EcoCyc reaction equation: DIMETHYLBENZIMIDAZOLE -> DIMETHYLBENZIMIDAZOLE; direction=LEFT-TO-RIGHT. E. coli mutants which lack the ability to synthesize 5,6-dimethylbenzimidazole (DMB) are able to grow when supplied with exogenous DMB and cobinamide .

## Biological Role

Substrates: Dimethylbenzimidazole (molecule.C03114). Products: Dimethylbenzimidazole (molecule.C03114).

## Annotation

E. coli mutants which lack the ability to synthesize 5,6-dimethylbenzimidazole (DMB) are able to grow when supplied with exogenous DMB and cobinamide .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C03114|molecule.C03114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03114|molecule.C03114]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-463`

## Notes

DIMETHYLBENZIMIDAZOLE -> DIMETHYLBENZIMIDAZOLE; direction=LEFT-TO-RIGHT
