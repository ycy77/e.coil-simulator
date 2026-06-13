---
entity_id: "complex.ecocyc.CPLX0-7614"
entity_type: "complex"
name: "ATP phosphoribosyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7614"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP phosphoribosyltransferase

`complex.ecocyc.CPLX0-7614`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7614`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60757|protein.P60757]]

## Enriched Summary

ATP phosphoribosyltransferase (HisG) catalyzes the first step in the HISTSYN-PWY pathway, the synthesis of phosphoribosyl-ATP via a displacement of the first carbon of 5-phosphoribosyl 1-pyrophosphate by the first nitrogen on the purine ring of ATP . The reaction mechanism appears to be a ping-pong type . ATP phosphoribosyltransferase functions as a dimer . Interaction with histidine induces formation of a catalytically inactive hexamer. In this hexameric state, the active site is unavailable. In constrast, AMP inhibits HisG function by binding in the 5-phosphoribosyl 1-pyrophosphate site and occluding the ATP binding site . Crystal structures of HisG bound to AMP and bound to phosphoribosyl-ATP have been solved to 2.7 Å and 2.9 Å resolution, respectively . Conformational changes in HisG has also been studied via spin-label and EPR methods . hisG mutants are histidine auxotrophs . A cold-sensitive allele of hisG is 1000-fold more sensitive to feedback inhibition by histidine . HisG: Review: ATP phosphoribosyltransferase (HisG) catalyzes the first step in the HISTSYN-PWY pathway, the synthesis of phosphoribosyl-ATP via a displacement of the first carbon of 5-phosphoribosyl 1-pyrophosphate by the first nitrogen on the purine ring of ATP . The reaction mechanism appears to be a ping-pong type . ATP phosphoribosyltransferase functions as a dimer...

## Biological Role

Catalyzes ATPPHOSPHORIBOSYLTRANS-RXN (reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN).

## Annotation

ATP phosphoribosyltransferase (HisG) catalyzes the first step in the HISTSYN-PWY pathway, the synthesis of phosphoribosyl-ATP via a displacement of the first carbon of 5-phosphoribosyl 1-pyrophosphate by the first nitrogen on the purine ring of ATP . The reaction mechanism appears to be a ping-pong type . ATP phosphoribosyltransferase functions as a dimer . Interaction with histidine induces formation of a catalytically inactive hexamer. In this hexameric state, the active site is unavailable. In constrast, AMP inhibits HisG function by binding in the 5-phosphoribosyl 1-pyrophosphate site and occluding the ATP binding site . Crystal structures of HisG bound to AMP and bound to phosphoribosyl-ATP have been solved to 2.7 Å and 2.9 Å resolution, respectively . Conformational changes in HisG has also been studied via spin-label and EPR methods . hisG mutants are histidine auxotrophs . A cold-sensitive allele of hisG is 1000-fold more sensitive to feedback inhibition by histidine . HisG: Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN|reaction.ecocyc.ATPPHOSPHORIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60757|protein.P60757]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7614`
- `QSPROTEOME:QS00049626`

## Notes

2*protein.P60757
