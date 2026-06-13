---
entity_id: "complex.ecocyc.OROPRIBTRANS-CPLX"
entity_type: "complex"
name: "orotate phosphoribosyltransferase"
source_database: "EcoCyc"
source_id: "OROPRIBTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# orotate phosphoribosyltransferase

`complex.ecocyc.OROPRIBTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:OROPRIBTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7E3|protein.P0A7E3]]

## Enriched Summary

Orotate phosphoribosyltransferase (PyrE) catalyzes the transfer of the phosphoribosyl moiety to the pyrimidine ring in the de novo biosynthesis of pyrimidine nucleotides. A crystal structure of PyrE has been solved . Expression of PyrE is regulated in response to UTP levels by transcriptional attenuation at a terminator structure between the EG10863 and pyrE genes in the rph-pyrE operon . Efficient translation of the upstream ORF also leads to higher PyrE expression , and inefficient translation leads to enhanced regulation of PyrE expression by the UTP pool . Coupling between transcription and translation is required for proper regulation of PyrE expression . Lysine acetylation of PyrE in a ΔG6577 background at residues K26 and K103 significantly reduced activity in vitro and in vivo suggesting a means of regulating PWY-5686 . Low levels of PyrE are found in E. coli strain W1485 and its daughter strains W3110 and MG1655 because of a frame shift mutation in rph, affecting transcription of pyrE . An 82 bp deletion in the rph-pyrE operon was found in the majority of cultures that had undergone laboratory evolution and may relieve the defect in pyrimidine biosynthesis of the MG1655 parent...

## Biological Role

Catalyzes OROPRIBTRANS-RXN (reaction.ecocyc.OROPRIBTRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Orotate phosphoribosyltransferase (PyrE) catalyzes the transfer of the phosphoribosyl moiety to the pyrimidine ring in the de novo biosynthesis of pyrimidine nucleotides. A crystal structure of PyrE has been solved . Expression of PyrE is regulated in response to UTP levels by transcriptional attenuation at a terminator structure between the EG10863 and pyrE genes in the rph-pyrE operon . Efficient translation of the upstream ORF also leads to higher PyrE expression , and inefficient translation leads to enhanced regulation of PyrE expression by the UTP pool . Coupling between transcription and translation is required for proper regulation of PyrE expression . Lysine acetylation of PyrE in a ΔG6577 background at residues K26 and K103 significantly reduced activity in vitro and in vivo suggesting a means of regulating PWY-5686 . Low levels of PyrE are found in E. coli strain W1485 and its daughter strains W3110 and MG1655 because of a frame shift mutation in rph, affecting transcription of pyrE . An 82 bp deletion in the rph-pyrE operon was found in the majority of cultures that had undergone laboratory evolution and may relieve the defect in pyrimidine biosynthesis of the MG1655 parent . Disruption of EG10808 (for the sake of optimizing industrial OROTATE production) resulted in unbalanced cell metabolism and accumulation of large amount of acetate, which was eliminated by reducing the flux of glycolysis . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.OROPRIBTRANS-RXN|reaction.ecocyc.OROPRIBTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7E3|protein.P0A7E3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:OROPRIBTRANS-CPLX`
- `QSPROTEOME:QS00188633`

## Notes

2*protein.P0A7E3
