---
entity_id: "complex.ecocyc.CPLX0-3041"
entity_type: "complex"
name: "peptidase T"
source_database: "EcoCyc"
source_id: "CPLX0-3041"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aminotripeptidase"
  - "tripeptide aminopeptidase"
---

# peptidase T

`complex.ecocyc.CPLX0-3041`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3041`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P29745|protein.P29745]]

## Enriched Summary

Peptidase T is a tripeptidase that can cleave the amino-terminal leucine, lysine, methionine or phenylalanine residue from certain tripeptides . Expression of PepT is upregulated during biofilm development and anaerobic growth . A crystal structure of PepT has been solved . Peptidase T is a tripeptidase that can cleave the amino-terminal leucine, lysine, methionine or phenylalanine residue from certain tripeptides . Expression of PepT is upregulated during biofilm development and anaerobic growth . A crystal structure of PepT has been solved .

## Biological Role

Catalyzes 3.4.11.4-RXN (reaction.ecocyc.3.4.11.4-RXN).

## Annotation

Peptidase T is a tripeptidase that can cleave the amino-terminal leucine, lysine, methionine or phenylalanine residue from certain tripeptides . Expression of PepT is upregulated during biofilm development and anaerobic growth . A crystal structure of PepT has been solved .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.11.4-RXN|reaction.ecocyc.3.4.11.4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P29745|protein.P29745]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3041`
- `QSPROTEOME:QS00181881`

## Notes

2*protein.P29745
