---
entity_id: "complex.ecocyc.CPLX0-8311"
entity_type: "complex"
name: "ribosome-dependent mRNA interferase toxin YoeB"
source_database: "EcoCyc"
source_id: "CPLX0-8311"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ribosome-dependent mRNA interferase toxin YoeB

`complex.ecocyc.CPLX0-8311`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8311`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69348|protein.P69348]]

## Enriched Summary

YoeB is the toxin of the YoeB-YefM toxin-antitoxin pair and is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . The YoeB toxin induces cleavage of translated mRNAs . YoeB inhibits translation initiation by interacting with the A site of the ribosome , leading to mRNA cleavage after the second position in the A-site codon and producing a 3'-phosphate product . Under heat shock conditions, the YoeB mRNAse activity is induced and mediates ribosomal A-site mRNA cleavage. YoeB activity under these conditions does not lead to growth arrest, and no cleavage of endogenous mRNAs was detected. YoeB is therefore proposed to function in the recycling of stalled ribosomes under heat stress . A monomeric mutant variant of YoeB retains mRNA cleavage activity, but is significantly less thermally stable than the homodimeric form . Earlier experiments showed that YoeB is an endoribonuclease that preferentially cleaves at the 3' end of purine ribonucleotides . The activity is dependent on mRNA translation in vivo, and the cleavage pattern is determined by the reading frame . An analysis of the targets and site specificity of YoeB showed some cleavage site specificity, favoring an A immediately upstream of the cleavage site, a preference for cleavage within the 5' end of mRNAs, and high codon position preference. Like other E...

## Biological Role

Catalyzes RXN0-4701 (reaction.ecocyc.RXN0-4701).

## Annotation

YoeB is the toxin of the YoeB-YefM toxin-antitoxin pair and is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . The YoeB toxin induces cleavage of translated mRNAs . YoeB inhibits translation initiation by interacting with the A site of the ribosome , leading to mRNA cleavage after the second position in the A-site codon and producing a 3'-phosphate product . Under heat shock conditions, the YoeB mRNAse activity is induced and mediates ribosomal A-site mRNA cleavage. YoeB activity under these conditions does not lead to growth arrest, and no cleavage of endogenous mRNAs was detected. YoeB is therefore proposed to function in the recycling of stalled ribosomes under heat stress . A monomeric mutant variant of YoeB retains mRNA cleavage activity, but is significantly less thermally stable than the homodimeric form . Earlier experiments showed that YoeB is an endoribonuclease that preferentially cleaves at the 3' end of purine ribonucleotides . The activity is dependent on mRNA translation in vivo, and the cleavage pattern is determined by the reading frame . An analysis of the targets and site specificity of YoeB showed some cleavage site specificity, favoring an A immediately upstream of the cleavage site, a preference for cleavage within the 5' end of mRNAs, and high codon position preference. Like other E. coli endoribonuclease toxins, YoeB activity does not affect mature ribosomes, but inhibits ribosome biogenesis, likely by affecting the translation of a specific set of ribosomal proteins . A crystal structure of YoeB bound to a 70S ribosome has been solved. A YoeB dimer was found to bind to the ribosomal A site . A rebuilt structure enabled modeling of nucleotide recognition by YoeB . A crystal structure of YoeB bound to a 30S subu

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4701|reaction.ecocyc.RXN0-4701]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69348|protein.P69348]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8311`
- `QSPROTEOME:QS00203709`

## Notes

2*protein.P69348
