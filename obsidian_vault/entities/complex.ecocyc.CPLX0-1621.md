---
entity_id: "complex.ecocyc.CPLX0-1621"
entity_type: "complex"
name: "RNase G"
source_database: "EcoCyc"
source_id: "CPLX0-1621"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribonuclease G"
---

# RNase G

`complex.ecocyc.CPLX0-1621`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1621`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9J0|protein.P0A9J0]]

## Enriched Summary

The rng gene encodes ribonuclease G (RNase G), an endoribonuclease which acts in maturation of the 5' end of the 16S rRNA precursor . The final three nucleotides are removed by G6634-MONOMER . Rng is also involved in RNA turnover . A large-scale study of RNAs affected by RNase G and RNase E is presented . Analysis of in vivo RNA-seq data suggests that RNase G may have a wide role in 5'-sequence removal from transcripts . The T4 bacteriophage endoribonuclease RegB cleaves early phage mRNA transcripts that are then processed by E. coli RNases G and E . RNase G has a role along with RNase E in processing the short precursor of 6S RNA to generate the mature sequence . RNase G can cleave a Bacillus subtilis aprE leader-lacZ mRNA in an AU-rich sequence in the stem-loop region, probably when it is in an open conformation . RNase G activity is distributed and is not directional with respect to the RNA substrate, in contrast to RNase E activity . The substrate sequence specificity of the enzyme has been examined . The preferred RNA substrate has a 5' monophosphate ; the 5' monophosphate appears to enhance the catalytic potency of the enzyme rather than improve substrate binding . In contrast, found that the interaction of RNase G with a 5'-monophosphorylated end can enhance substrate binding in vitro and the decay of mRNA in vivo...

## Biological Role

Catalyzes RXN0-6523 (reaction.ecocyc.RXN0-6523).

## Annotation

The rng gene encodes ribonuclease G (RNase G), an endoribonuclease which acts in maturation of the 5' end of the 16S rRNA precursor . The final three nucleotides are removed by G6634-MONOMER . Rng is also involved in RNA turnover . A large-scale study of RNAs affected by RNase G and RNase E is presented . Analysis of in vivo RNA-seq data suggests that RNase G may have a wide role in 5'-sequence removal from transcripts . The T4 bacteriophage endoribonuclease RegB cleaves early phage mRNA transcripts that are then processed by E. coli RNases G and E . RNase G has a role along with RNase E in processing the short precursor of 6S RNA to generate the mature sequence . RNase G can cleave a Bacillus subtilis aprE leader-lacZ mRNA in an AU-rich sequence in the stem-loop region, probably when it is in an open conformation . RNase G activity is distributed and is not directional with respect to the RNA substrate, in contrast to RNase E activity . The substrate sequence specificity of the enzyme has been examined . The preferred RNA substrate has a 5' monophosphate ; the 5' monophosphate appears to enhance the catalytic potency of the enzyme rather than improve substrate binding . In contrast, found that the interaction of RNase G with a 5'-monophosphorylated end can enhance substrate binding in vitro and the decay of mRNA in vivo. Determinants for 5'-monophosphate-assisted RNA cleavage by RNase G in vitro include a requirement for at least two and preferably three or more unpaired 5'-terminal nucleotides, and six nucleotides provide optimal spacing between the 5'-end and the scissile phosphate bond. Any sequence of unpaired nucleotides at the 5'-end is tolerated . In the 5' untranslated region of adhE mRNA, a stem-loop structure containing a bubble in the stem is required for it

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6523|reaction.ecocyc.RXN0-6523]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9J0|protein.P0A9J0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1621`
- `QSPROTEOME:QS00049597`

## Notes

2*protein.P0A9J0
