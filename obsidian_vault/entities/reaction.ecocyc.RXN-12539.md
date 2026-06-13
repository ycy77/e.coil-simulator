---
entity_id: "reaction.ecocyc.RXN-12539"
entity_type: "reaction"
name: "RXN-12539"
source_database: "EcoCyc"
source_id: "RXN-12539"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12539

`reaction.ecocyc.RXN-12539`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12539`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Unlike E.coli B SPAO which is a known ethylenogenic strain , E. coli K-12 does not produce ethylene from the degradation of methionine via the intermediate 2-oxo-4-methylthiobutanoate (MetaCyc pathway PWY-6854) . reported minimal production of ethylene by E. coli K-12 during growth on nutrient broth supplemented with 2-oxo-4-methylthiobutanoate and no ethylene production when supplemented with methionine. This reaction is thus considered not to be physiologically relevent in E. coli K-12. EcoCyc reaction equation: CPD-479 + CPD-12377 -> ETHYLENE-CMPD + CPD-7671 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. Unlike E.coli B SPAO which is a known ethylenogenic strain , E. coli K-12 does not produce ethylene from the degradation of methionine via the intermediate 2-oxo-4-methylthiobutanoate (MetaCyc pathway PWY-6854) . reported minimal production of ethylene by E. coli K-12 during growth on nutrient broth supplemented with 2-oxo-4-methylthiobutanoate and no ethylene production when supplemented with methionine. This reaction is thus considered not to be physiologically relevent in E. coli K-12.

## Biological Role

Substrates: 4-Methylthio-2-oxobutanoic acid (molecule.C01180), hydroxyl radical (molecule.ecocyc.CPD-12377). Products: CO2 (molecule.C00011), Methanethiol (molecule.C00409), Ethylene (molecule.C06547).

## Annotation

Unlike E.coli B SPAO which is a known ethylenogenic strain , E. coli K-12 does not produce ethylene from the degradation of methionine via the intermediate 2-oxo-4-methylthiobutanoate (MetaCyc pathway PWY-6854) . reported minimal production of ethylene by E. coli K-12 during growth on nutrient broth supplemented with 2-oxo-4-methylthiobutanoate and no ethylene production when supplemented with methionine. This reaction is thus considered not to be physiologically relevent in E. coli K-12.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00409|molecule.C00409]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06547|molecule.C06547]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01180|molecule.C01180]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12377|molecule.ecocyc.CPD-12377]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12539`

## Notes

CPD-479 + CPD-12377 -> ETHYLENE-CMPD + CPD-7671 + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
