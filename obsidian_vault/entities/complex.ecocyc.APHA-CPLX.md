---
entity_id: "complex.ecocyc.APHA-CPLX"
entity_type: "complex"
name: "acid phosphatase / phosphotransferase"
source_database: "EcoCyc"
source_id: "APHA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AphA"
---

# acid phosphatase / phosphotransferase

`complex.ecocyc.APHA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:APHA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AE22|protein.P0AE22]]

## Enriched Summary

EcoCyc complex APHA-CPLX

## Biological Role

Catalyzes 3-NUCLEOTID-RXN (reaction.ecocyc.3-NUCLEOTID-RXN), 5-NUCLEOTID-RXN (reaction.ecocyc.5-NUCLEOTID-RXN), ACID-PHOSPHATASE-RXN (reaction.ecocyc.ACID-PHOSPHATASE-RXN), DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN (reaction.ecocyc.DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN), RXN-14473 (reaction.ecocyc.RXN-14473), RXN-14505 (reaction.ecocyc.RXN-14505), RXN-14522 (reaction.ecocyc.RXN-14522), RXN-14523 (reaction.ecocyc.RXN-14523), and 5 more. Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex APHA-CPLX

## Outgoing Edges (13)

- `catalyzes` --> [[reaction.ecocyc.3-NUCLEOTID-RXN|reaction.ecocyc.3-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.5-NUCLEOTID-RXN|reaction.ecocyc.5-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACID-PHOSPHATASE-RXN|reaction.ecocyc.ACID-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN|reaction.ecocyc.DEOXYNUCLEOTIDE-3-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14473|reaction.ecocyc.RXN-14473]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14505|reaction.ecocyc.RXN-14505]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14522|reaction.ecocyc.RXN-14522]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14523|reaction.ecocyc.RXN-14523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14524|reaction.ecocyc.RXN-14524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14525|reaction.ecocyc.RXN-14525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14534|reaction.ecocyc.RXN-14534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5114|reaction.ecocyc.RXN0-5114]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AE22|protein.P0AE22]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:APHA-CPLX`
- `QSPROTEOME:QS00181685`

## Notes

4*protein.P0AE22
