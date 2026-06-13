---
entity_id: "complex.ecocyc.CPLX0-7624"
entity_type: "complex"
name: "YhaV-PrlF toxin-antitoxin complex"
source_database: "EcoCyc"
source_id: "CPLX0-7624"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# YhaV-PrlF toxin-antitoxin complex

`complex.ecocyc.CPLX0-7624`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7624`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15373|protein.P15373]], [[protein.P64594|protein.P64594]]

## Enriched Summary

The PrlF-YhaV complex is the nontoxic form of the antitoxin-toxin pair consisting of the antitoxin PrlF and the endonuclease toxin YhaV. Although such pairs are expected to be involved in plasmid maintenance when they are present on plasmids, it is unclear what role this chromosomal pairing plays in the cell. PrlF-YhaV is a classic pairing of a toxin with an antitoxin. In the absence of the antitoxin PrlF, expression of the toxic YhaV protein leads to bacteriostatic growth arrest within thirty minutes. YhaV-based toxicity is due to its general endonuclease activity. Key mutations that disrupt this activity lead to a concomitant reduction in toxicity . The PrlF-YhaV complex consists of four YhaV monomers and two PrlF monomers. This nontoxic form is achieved by cofolding of the components. Simple combination of already folded PrlF with already folded YhaV does not negate YhaV toxicity . PrlF and YhaV are translationally coupled . YhaV-PrlF is a type II toxin-antitoxin system that belongs to the largest subclass of type II TA systems in E. coli, with nearly equal antitoxin-to-toxin mRNA ratio based on analysis of RNA-seq data and a higher protein synthesis rate for the antitoxin based on analysis of Ribo-Seq data . Two copies of the complete PrlF-YhaV complex bind upstream of the prlF promoter, negatively autoregulating the operon...

## Annotation

The PrlF-YhaV complex is the nontoxic form of the antitoxin-toxin pair consisting of the antitoxin PrlF and the endonuclease toxin YhaV. Although such pairs are expected to be involved in plasmid maintenance when they are present on plasmids, it is unclear what role this chromosomal pairing plays in the cell. PrlF-YhaV is a classic pairing of a toxin with an antitoxin. In the absence of the antitoxin PrlF, expression of the toxic YhaV protein leads to bacteriostatic growth arrest within thirty minutes. YhaV-based toxicity is due to its general endonuclease activity. Key mutations that disrupt this activity lead to a concomitant reduction in toxicity . The PrlF-YhaV complex consists of four YhaV monomers and two PrlF monomers. This nontoxic form is achieved by cofolding of the components. Simple combination of already folded PrlF with already folded YhaV does not negate YhaV toxicity . PrlF and YhaV are translationally coupled . YhaV-PrlF is a type II toxin-antitoxin system that belongs to the largest subclass of type II TA systems in E. coli, with nearly equal antitoxin-to-toxin mRNA ratio based on analysis of RNA-seq data and a higher protein synthesis rate for the antitoxin based on analysis of Ribo-Seq data . Two copies of the complete PrlF-YhaV complex bind upstream of the prlF promoter, negatively autoregulating the operon .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P15373|protein.P15373]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P64594|protein.P64594]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7624`
- `QSPROTEOME:QS00247053`

## Notes

2*protein.P15373|4*protein.P64594
