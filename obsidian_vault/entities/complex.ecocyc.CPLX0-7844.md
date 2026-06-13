---
entity_id: "complex.ecocyc.CPLX0-7844"
entity_type: "complex"
name: "p-aminobenzoyl-glutamate hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7844"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# p-aminobenzoyl-glutamate hydrolase

`complex.ecocyc.CPLX0-7844`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7844`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76052|protein.P76052]], [[protein.P77357|protein.P77357]]

## Enriched Summary

p-aminobenzoyl-glutamate hydrolase (PGH) may be involved in the utilization of p-aminobenzoyl-glutamate, the major end product of folate catabolism in humans . Based on gel filtration analysis, the enzyme appears to be a tetramer consisting of two subunits each of AbgA and AbgB . Mutations that appear to enhance expression of abgABT allow a pabA mutant to utilize p-aminobenzoyl-glutamate as a source of p-aminobenzoate for folate biosynthesis. However, the abgAB genes are not essential for utilization of p-aminobenzoyl-glutamate; thus, there may be a second PGH activity present in E. coli . p-aminobenzoyl-glutamate hydrolase (PGH) may be involved in the utilization of p-aminobenzoyl-glutamate, the major end product of folate catabolism in humans . Based on gel filtration analysis, the enzyme appears to be a tetramer consisting of two subunits each of AbgA and AbgB . Mutations that appear to enhance expression of abgABT allow a pabA mutant to utilize p-aminobenzoyl-glutamate as a source of p-aminobenzoate for folate biosynthesis. However, the abgAB genes are not essential for utilization of p-aminobenzoyl-glutamate; thus, there may be a second PGH activity present in E. coli .

## Biological Role

Catalyzes RXN0-5040 (reaction.ecocyc.RXN0-5040). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

p-aminobenzoyl-glutamate hydrolase (PGH) may be involved in the utilization of p-aminobenzoyl-glutamate, the major end product of folate catabolism in humans . Based on gel filtration analysis, the enzyme appears to be a tetramer consisting of two subunits each of AbgA and AbgB . Mutations that appear to enhance expression of abgABT allow a pabA mutant to utilize p-aminobenzoyl-glutamate as a source of p-aminobenzoate for folate biosynthesis. However, the abgAB genes are not essential for utilization of p-aminobenzoyl-glutamate; thus, there may be a second PGH activity present in E. coli .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5040|reaction.ecocyc.RXN0-5040]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76052|protein.P76052]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P77357|protein.P77357]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7844`
- `QSPROTEOME:QS00049445`

## Notes

2*protein.P76052|2*protein.P77357
