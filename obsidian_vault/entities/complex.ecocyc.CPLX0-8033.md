---
entity_id: "complex.ecocyc.CPLX0-8033"
entity_type: "complex"
name: "acetylesterase"
source_database: "EcoCyc"
source_id: "CPLX0-8033"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetylesterase

`complex.ecocyc.CPLX0-8033`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8033`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23872|protein.P23872]]

## Enriched Summary

Aes catalyzes hydrolysis of p-nitrophenyl esters of fatty acids, preferring substrates with short (cat and decreasing Km, respectively . Overexpression of aes results in increased p-nitrophenyl acetate hydrolysis, compared to wild type, and this strain shows growth on triacetyl glycerol and repression of the maltose transport system . A genetic interaction between malT and aes has been observed . Mutations in MalT have differential effects on the sensitivity of MalT to Aes and MalY, which inhibit the activator in similar, yet distinct, ways . Aes is identical to esterase B, a protein marker used to distinguish E. coli phylogenetic groups . Aes: "acetyl esterase" Aes catalyzes hydrolysis of p-nitrophenyl esters of fatty acids, preferring substrates with short (cat and decreasing Km, respectively . Overexpression of aes results in increased p-nitrophenyl acetate hydrolysis, compared to wild type, and this strain shows growth on triacetyl glycerol and repression of the maltose transport system . A genetic interaction between malT and aes has been observed . Mutations in MalT have differential effects on the sensitivity of MalT to Aes and MalY, which inhibit the activator in similar, yet distinct, ways . Aes is identical to esterase B, a protein marker used to distinguish E. coli phylogenetic groups . Aes: "acetyl esterase"

## Biological Role

Catalyzes ACETYLESTERASE-RXN (reaction.ecocyc.ACETYLESTERASE-RXN).

## Annotation

Aes catalyzes hydrolysis of p-nitrophenyl esters of fatty acids, preferring substrates with short (cat and decreasing Km, respectively . Overexpression of aes results in increased p-nitrophenyl acetate hydrolysis, compared to wild type, and this strain shows growth on triacetyl glycerol and repression of the maltose transport system . A genetic interaction between malT and aes has been observed . Mutations in MalT have differential effects on the sensitivity of MalT to Aes and MalY, which inhibit the activator in similar, yet distinct, ways . Aes is identical to esterase B, a protein marker used to distinguish E. coli phylogenetic groups . Aes: "acetyl esterase"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ACETYLESTERASE-RXN|reaction.ecocyc.ACETYLESTERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P23872|protein.P23872]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8033`
- `QSPROTEOME:QS00190117`

## Notes

2*protein.P23872
