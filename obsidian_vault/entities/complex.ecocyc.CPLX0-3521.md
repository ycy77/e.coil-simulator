---
entity_id: "complex.ecocyc.CPLX0-3521"
entity_type: "complex"
name: "polynucleotide phosphorylase"
source_database: "EcoCyc"
source_id: "CPLX0-3521"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PNPase"
---

# polynucleotide phosphorylase

`complex.ecocyc.CPLX0-3521`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3521`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05055|protein.P05055]]

## Enriched Summary

Polynucleotide phosphorylase (PNPase) is a 3' to 5' exonuclease and a 3'-terminal oligonucleotide polymerase. It degrades various mRNAs, including those paired to Hfq-dependent sRNA, is involved in cold shock regulation, is a part of tRNA maturation and degradation, adds heteropolymeric tails to some RNAs and is a component of the CPLX0-2381, a multienzyme complex that carries out RNA degradation. PNPase is involved in general phosphorolytic mRNA degradation. Loss of PNPase leads to an increase in steady-state levels of mRNA, as well as increasing mRNA half lives in the absence of the 3' exonuclease EG11620-MONOMER . PNPase also has a role in mRNA degradation during carbon starvation, where it may be required for breakdown of small rRNA fragments produced by other RNases . A number of specific PNPase substrates have been identified. PNPase is involved in degradation of lac mRNA, rnb mRNA, mRNA coding for ribosomal protein S20, and the RNA-OUT antisense RNA . It also degrades sok antisense RNA and thrS and rpsO mRNA following cleavage by RNase E . PNPase binds to but does not degrade RNA containing 8-oxoguanine . PNPase-mediated degradation is required for regulation of the cold shock response. PNPase degrades a number of mRNAs induced by cold shock, including those coding for CspA, RbfA, CsdA, RpoE, RseA, Rnr and many others...

## Biological Role

Catalyzes 2.7.7.8-RXN (reaction.ecocyc.2.7.7.8-RXN), poly(A)-specific ribonuclease (reaction.ecocyc.RXN0-7463), RXN0-7477 (reaction.ecocyc.RXN0-7477), RXN0-7482 (reaction.ecocyc.RXN0-7482), RXN0-7483 (reaction.ecocyc.RXN0-7483). Component of degradosome (complex.ecocyc.CPLX0-2381). Bound by Magnesium cation (molecule.C00305).

## Annotation

Polynucleotide phosphorylase (PNPase) is a 3' to 5' exonuclease and a 3'-terminal oligonucleotide polymerase. It degrades various mRNAs, including those paired to Hfq-dependent sRNA, is involved in cold shock regulation, is a part of tRNA maturation and degradation, adds heteropolymeric tails to some RNAs and is a component of the CPLX0-2381, a multienzyme complex that carries out RNA degradation. PNPase is involved in general phosphorolytic mRNA degradation. Loss of PNPase leads to an increase in steady-state levels of mRNA, as well as increasing mRNA half lives in the absence of the 3' exonuclease EG11620-MONOMER . PNPase also has a role in mRNA degradation during carbon starvation, where it may be required for breakdown of small rRNA fragments produced by other RNases . A number of specific PNPase substrates have been identified. PNPase is involved in degradation of lac mRNA, rnb mRNA, mRNA coding for ribosomal protein S20, and the RNA-OUT antisense RNA . It also degrades sok antisense RNA and thrS and rpsO mRNA following cleavage by RNase E . PNPase binds to but does not degrade RNA containing 8-oxoguanine . PNPase-mediated degradation is required for regulation of the cold shock response. PNPase degrades a number of mRNAs induced by cold shock, including those coding for CspA, RbfA, CsdA, RpoE, RseA, Rnr and many others . The isolated PNPase S1 RNA-binding domain can complement a deletion in four cold-shock genes . The 3' to 5' processive cleavage of RNA by PNPase depends on the composition and structure of the 3' end of the substrate . RhlB and poly(A) polymerase I (PAP I) in concert with the degradosome are required for PNPase-mediated degradation of cistrons with 3' REP-stabilizers . Loss-of-function mutant studies with pnp and with hfq found that PNPase contrib

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.2.7.7.8-RXN|reaction.ecocyc.2.7.7.8-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7463|reaction.ecocyc.RXN0-7463]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7477|reaction.ecocyc.RXN0-7477]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7482|reaction.ecocyc.RXN0-7482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7483|reaction.ecocyc.RXN0-7483]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05055|protein.P05055]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-3521`
- `QSPROTEOME:QS00181753`

## Notes

3*protein.P05055
