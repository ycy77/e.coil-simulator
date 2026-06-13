---
entity_id: "complex.ecocyc.CPLX0-3601"
entity_type: "complex"
name: "ribonuclease BN"
source_database: "EcoCyc"
source_id: "CPLX0-3601"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "binuclear zinc phosphodiesterase"
  - "tRNase Z"
  - "RNase BN"
  - "ZiPD"
  - "RNase Z"
---

# ribonuclease BN

`complex.ecocyc.CPLX0-3601`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3601`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8V0|protein.P0A8V0]]

## Enriched Summary

Ribonuclease BN (RNase BN) cleaves the 3'-terminal portion of precursor tRNAs and can also cleave mRNAs , various short unstructured RNAs , and 6S-RNA . Although earlier work suggested that it is an exoribonuclease , it was subsequently suggested to be an endoribonuclease , or both an exo- and endoribonuclease depending on substrate and metal ion cofactor . The enzyme has also been identified as a binuclear zinc phosphodiesterase (ZiPD) . RNase BN was first characterized in E. coli B. A mutant strain BN lacking the enzyme cannot process 3' residues on some bacteriophage T4 tRNA precursors . The gene encoding RNase BN was originally incorrectly identified as yihY , but was later identified as elaC and renamed rbn . Although E. coli RNase BN is a homolog of the 3' pre-tRNA processing endoribonuclease RNase Z (tRNase Z) found in eukaryotes, archaea, and some eubacteria such as Bacillus subtilis, it does not function in pre-tRNA processing in E. coli . RNase Z cleaves after the discriminator nucleotide to allow addition of the universal 3' CCA of mature tRNA. However, in E. coli RNase Z activity is not needed for pre-tRNA maturation because all of E. coli's pre-tRNAs contain the CCA sequence. Subsequent work indicated RNase BN can endoribonucleolytically cleave synthetic unstructured RNA in vitro . In E...

## Biological Role

Catalyzes RXN0-4222 (reaction.ecocyc.RXN0-4222), RXN0-6525 (reaction.ecocyc.RXN0-6525), RXN0-7473 (reaction.ecocyc.RXN0-7473). Bound by Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305).

## Annotation

Ribonuclease BN (RNase BN) cleaves the 3'-terminal portion of precursor tRNAs and can also cleave mRNAs , various short unstructured RNAs , and 6S-RNA . Although earlier work suggested that it is an exoribonuclease , it was subsequently suggested to be an endoribonuclease , or both an exo- and endoribonuclease depending on substrate and metal ion cofactor . The enzyme has also been identified as a binuclear zinc phosphodiesterase (ZiPD) . RNase BN was first characterized in E. coli B. A mutant strain BN lacking the enzyme cannot process 3' residues on some bacteriophage T4 tRNA precursors . The gene encoding RNase BN was originally incorrectly identified as yihY , but was later identified as elaC and renamed rbn . Although E. coli RNase BN is a homolog of the 3' pre-tRNA processing endoribonuclease RNase Z (tRNase Z) found in eukaryotes, archaea, and some eubacteria such as Bacillus subtilis, it does not function in pre-tRNA processing in E. coli . RNase Z cleaves after the discriminator nucleotide to allow addition of the universal 3' CCA of mature tRNA. However, in E. coli RNase Z activity is not needed for pre-tRNA maturation because all of E. coli's pre-tRNAs contain the CCA sequence. Subsequent work indicated RNase BN can endoribonucleolytically cleave synthetic unstructured RNA in vitro . In E. coli RNase BN (ElaC) can endonucleolytically process Bacillus subtilis tRNA precursors that lack a 3' terminal CCA both in vivo and in vitro, demonstrating tRNase Z activity . RNase BN was later shown to cleave the 3' terminal CCA residues from precursor and mature E. coli tRNAs in vitro , although other studies showed no removal of the CCA from tRNA precursors . RNase BN (ElaC) can endonucleolytically cleave in vitro specific transcripts of Bacillus subtilis cloned into E.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4222|reaction.ecocyc.RXN0-4222]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6525|reaction.ecocyc.RXN0-6525]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7473|reaction.ecocyc.RXN0-7473]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8V0|protein.P0A8V0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3601`
- `QSPROTEOME:QS00181861`

## Notes

2*protein.P0A8V0
