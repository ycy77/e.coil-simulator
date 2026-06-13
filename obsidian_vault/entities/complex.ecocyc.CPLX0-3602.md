---
entity_id: "complex.ecocyc.CPLX0-3602"
entity_type: "complex"
name: "ribonuclease T"
source_database: "EcoCyc"
source_id: "CPLX0-3602"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribonuclease T

`complex.ecocyc.CPLX0-3602`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3602`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30014|protein.P30014]]

## Enriched Summary

Ribonuclease T (RNase T) is a 3'→5' exoribonuclease responsible for 3' trimming of many stable RNAs, including tRNAs. It is also capable of degrading single-stranded DNA and may have a role in DNA repair. RNase T participates in tRNA maturation as and can compensate for the lack of RNases II, D, BN, and PH, which also carry out tRNA maturation . RNase T favors tRNAs with a 3'-terminal adenosine . RNase E, rather than RNase T or any of the other 3'→5' exonucleases, appears to be involved in maturation of the 3' ends of the three proline tRNAs in E. coli . See PWY0-1628 and PWY0-1625 as well as individual tRNA processing pathways. In addition to its role in tRNA 3'-end maturation, RNase T can reduce or block the addition of short poly(A) tails on pre-tRNAs by poly(A) polymerase I, suggesting a mechanism for regulating the intracellular levels of functional tRNAs . The tRNA 3'-end turnover activity of RNase T — removal of the 3' terminal "A" nucleotide from the -CCA tail of tRNAs — appears to serve as an additional quality control mechanism; RNase T is unable to process the CCACCA-tailed ends of defective tRNAs . RNase T is one of several RNases that can carry out 3' exoribonucleolytic cleavage of small, stable RNAs such as M1, 10Sa, 6S and 4.5S RNA. It appears to be able to cleave more closely to predicted double-stranded secondary structure than other 3' exoribonucleases...

## Biological Role

Catalyzes 3'-exoribonuclease (reaction.ecocyc.RXN0-4223), RXN0-6480 (reaction.ecocyc.RXN0-6480), RXN0-6482 (reaction.ecocyc.RXN0-6482), RXN0-6483 (reaction.ecocyc.RXN0-6483), RXN0-6484 (reaction.ecocyc.RXN0-6484), RXN0-7473 (reaction.ecocyc.RXN0-7473). Bound by Magnesium cation (molecule.C00305).

## Annotation

Ribonuclease T (RNase T) is a 3'→5' exoribonuclease responsible for 3' trimming of many stable RNAs, including tRNAs. It is also capable of degrading single-stranded DNA and may have a role in DNA repair. RNase T participates in tRNA maturation as and can compensate for the lack of RNases II, D, BN, and PH, which also carry out tRNA maturation . RNase T favors tRNAs with a 3'-terminal adenosine . RNase E, rather than RNase T or any of the other 3'→5' exonucleases, appears to be involved in maturation of the 3' ends of the three proline tRNAs in E. coli . See PWY0-1628 and PWY0-1625 as well as individual tRNA processing pathways. In addition to its role in tRNA 3'-end maturation, RNase T can reduce or block the addition of short poly(A) tails on pre-tRNAs by poly(A) polymerase I, suggesting a mechanism for regulating the intracellular levels of functional tRNAs . The tRNA 3'-end turnover activity of RNase T — removal of the 3' terminal "A" nucleotide from the -CCA tail of tRNAs — appears to serve as an additional quality control mechanism; RNase T is unable to process the CCACCA-tailed ends of defective tRNAs . RNase T is one of several RNases that can carry out 3' exoribonucleolytic cleavage of small, stable RNAs such as M1, 10Sa, 6S and 4.5S RNA. It appears to be able to cleave more closely to predicted double-stranded secondary structure than other 3' exoribonucleases . RNase T is required for 5S RNA maturation, with its absence resulting in two extra 3' nucleotides that can be removed with purified RNase T in vitro . It is also involved in maturation of 23S rRNA, being required for removal of the last few 3' precursor nucleotides . The 23S rRNA precursor, and some tRNAs, contain an RNase T stalling sequence that prevents premature processing by RNase T . A Δrnt strai

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4223|reaction.ecocyc.RXN0-4223]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6480|reaction.ecocyc.RXN0-6480]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6482|reaction.ecocyc.RXN0-6482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6483|reaction.ecocyc.RXN0-6483]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6484|reaction.ecocyc.RXN0-6484]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7473|reaction.ecocyc.RXN0-7473]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P30014|protein.P30014]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3602`
- `QSPROTEOME:QS00183193`

## Notes

2*protein.P30014
