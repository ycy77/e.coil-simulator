---
entity_id: "complex.ecocyc.CPLX0-7940"
entity_type: "complex"
name: "CP4-6 prophage; 2-dehydro-3-deoxygluconate aldolase"
source_database: "EcoCyc"
source_id: "CPLX0-7940"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# CP4-6 prophage; 2-dehydro-3-deoxygluconate aldolase

`complex.ecocyc.CPLX0-7940`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7940`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75682|protein.P75682]]

## Enriched Summary

The presence of 2-keto-3-deoxygalactonate (KDGal) in the crystal structure suggests that YagE functions as a KDG aldolase . Genetic evidence suggests that YagE may also function as a 2-dehydro-3-deoxy-D-pentonate aldolase . The enzyme was predicted to be a dihydropicolinate synthase-like protein, a member of the NAL subfamily of proteins , but does not appear to have N-acetylneuraminate lyase (NAL) or dihydropicolinate synthase (DHDPS) activity . The crystal structure of YagE suggests that the protein is a homotetramer . Co-crystal structures of YagE in the presence of pyruvate and 2-keto-3-deoxygalactonate have been solved . A yjhH yagE double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain 2-dehydro-3-deoxy-D-pentonate aldolase activity. Both phenotypes are complemented by providing yjhH on a plasmid . Overexpression of yagE has been used for metabolic engineering of glycolate production . yagE is part of the prophage CP4-6. The presence of 2-keto-3-deoxygalactonate (KDGal) in the crystal structure suggests that YagE functions as a KDG aldolase . Genetic evidence suggests that YagE may also function as a 2-dehydro-3-deoxy-D-pentonate aldolase...

## Biological Role

Catalyzes 4.1.2.28-RXN (reaction.ecocyc.4.1.2.28-RXN), DHDOGALDOL-RXN (reaction.ecocyc.DHDOGALDOL-RXN).

## Annotation

The presence of 2-keto-3-deoxygalactonate (KDGal) in the crystal structure suggests that YagE functions as a KDG aldolase . Genetic evidence suggests that YagE may also function as a 2-dehydro-3-deoxy-D-pentonate aldolase . The enzyme was predicted to be a dihydropicolinate synthase-like protein, a member of the NAL subfamily of proteins , but does not appear to have N-acetylneuraminate lyase (NAL) or dihydropicolinate synthase (DHDPS) activity . The crystal structure of YagE suggests that the protein is a homotetramer . Co-crystal structures of YagE in the presence of pyruvate and 2-keto-3-deoxygalactonate have been solved . A yjhH yagE double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain 2-dehydro-3-deoxy-D-pentonate aldolase activity. Both phenotypes are complemented by providing yjhH on a plasmid . Overexpression of yagE has been used for metabolic engineering of glycolate production . yagE is part of the prophage CP4-6.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.4.1.2.28-RXN|reaction.ecocyc.4.1.2.28-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DHDOGALDOL-RXN|reaction.ecocyc.DHDOGALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P75682|protein.P75682]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7940`
- `QSPROTEOME:QS00181819`

## Notes

4*protein.P75682
