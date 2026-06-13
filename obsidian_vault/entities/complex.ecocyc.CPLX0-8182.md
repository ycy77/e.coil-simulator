---
entity_id: "complex.ecocyc.CPLX0-8182"
entity_type: "complex"
name: "N6-L-threonylcarbamoyladenine synthase"
source_database: "EcoCyc"
source_id: "CPLX0-8182"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "threonylcarbamoyl transferase complex"
  - "TCT complex"
---

# N6-L-threonylcarbamoyladenine synthase

`complex.ecocyc.CPLX0-8182`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8182`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AF67|protein.P0AF67]], [[complex.ecocyc.CPLX0-8181|complex.ecocyc.CPLX0-8181]]

## Enriched Summary

N6-L-threonylcarbamoyladenine synthase catalyzes the addition of the threonylcarbamoyl group to the adenine residue at position 37 of ANN-decoding tRNAs, generating the modified t6A nucleotide. The enzyme consists of a TsaB-TsaD heterodimer which forms an unstable complex with TsaE. Based on SAXS data, a structural model of the ternary complex has been generated . A mixture of purified G7698-MONOMER TsaC, TsaD, TsaB, and TsaE proteins was shown to catalyze formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . Reviews: N6-L-threonylcarbamoyladenine synthase catalyzes the addition of the threonylcarbamoyl group to the adenine residue at position 37 of ANN-decoding tRNAs, generating the modified t6A nucleotide. The enzyme consists of a TsaB-TsaD heterodimer which forms an unstable complex with TsaE. Based on SAXS data, a structural model of the ternary complex has been generated . A mixture of purified G7698-MONOMER TsaC, TsaD, TsaB, and TsaE proteins was shown to catalyze formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . Reviews:

## Biological Role

Catalyzes RXN-14570 (reaction.ecocyc.RXN-14570).

## Annotation

N6-L-threonylcarbamoyladenine synthase catalyzes the addition of the threonylcarbamoyl group to the adenine residue at position 37 of ANN-decoding tRNAs, generating the modified t6A nucleotide. The enzyme consists of a TsaB-TsaD heterodimer which forms an unstable complex with TsaE. Based on SAXS data, a structural model of the ternary complex has been generated . A mixture of purified G7698-MONOMER TsaC, TsaD, TsaB, and TsaE proteins was shown to catalyze formation of t6A in the presence of a tRNA substrate, ATP, threonine and bicarbonate in vitro . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14570|reaction.ecocyc.RXN-14570]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-8181|complex.ecocyc.CPLX0-8181]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P05852|protein.P05852]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AF67|protein.P0AF67]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76256|protein.P76256]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8182`
- `QSPROTEOME:QS00049462`

## Notes

1*protein.P0AF67|complex.ecocyc.CPLX0-8181
