---
entity_id: "complex.ecocyc.CPLX0-11245"
entity_type: "complex"
name: "tRNA cmo5U34 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-11245"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA cmo5U34 methyltransferase

`complex.ecocyc.CPLX0-11245`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-11245`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P36566|protein.P36566]]

## Enriched Summary

CmoM catalyzes the transfer of a methyl group from S-adenosyl-L-methionine (SAM) to cmo5U in tRNA. This reaction is the final step in the biosynthesis of the 5-methoxycarbonylmethoxyuridine (mcmo5U) modification at the U34 wobble base of certain tRNAs . CmoM belongs to the class I SAM-dependent methyltransferases . Active site mutants R26A, D73A, W124A, Y150A, R209A, D213A and R246A do not restore methylation of cmo5U in a cmoM deletion mutant . A crystal structure has been obtained of CmoM complexed to serT-tRNA that contains a cmo5U34 at the 5'end of the anticodon and an analog of the SAM substrate, sinefungin. This high resolution (2.2 Å) structure revealed a dimeric structure for the CmoM and the specific residues and local conformational changes responsible for tRNA binding, the most extensive of which is the modified U34 nucleotide on the tRNA . A ΔcmoM mutant lacks the mcmo5U modification and contains higher levels of the cmo5U modification . A cmoM null mutant is able to grow on minimal medium and does not show a detectable morphological defect . The smtA-39 mutant allele shows synthetic lethality with recA; the phenotype is likely due to a polar effect of the mutant allele on the downstream mukFEB genes...

## Biological Role

Catalyzes RXN0-7167 (reaction.ecocyc.RXN0-7167).

## Annotation

CmoM catalyzes the transfer of a methyl group from S-adenosyl-L-methionine (SAM) to cmo5U in tRNA. This reaction is the final step in the biosynthesis of the 5-methoxycarbonylmethoxyuridine (mcmo5U) modification at the U34 wobble base of certain tRNAs . CmoM belongs to the class I SAM-dependent methyltransferases . Active site mutants R26A, D73A, W124A, Y150A, R209A, D213A and R246A do not restore methylation of cmo5U in a cmoM deletion mutant . A crystal structure has been obtained of CmoM complexed to serT-tRNA that contains a cmo5U34 at the 5'end of the anticodon and an analog of the SAM substrate, sinefungin. This high resolution (2.2 Å) structure revealed a dimeric structure for the CmoM and the specific residues and local conformational changes responsible for tRNA binding, the most extensive of which is the modified U34 nucleotide on the tRNA . A ΔcmoM mutant lacks the mcmo5U modification and contains higher levels of the cmo5U modification . A cmoM null mutant is able to grow on minimal medium and does not show a detectable morphological defect . The smtA-39 mutant allele shows synthetic lethality with recA; the phenotype is likely due to a polar effect of the mutant allele on the downstream mukFEB genes . SmtA: "S-adenosylmethionine-dependent methyltransferase A" CmoM: "cmo5U methyltransferase"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7167|reaction.ecocyc.RXN0-7167]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P36566|protein.P36566]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-11245`
- `QSPROTEOME:QS00182053`

## Notes

2*protein.P36566
