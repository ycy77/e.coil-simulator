---
entity_id: "complex.ecocyc.PC00103"
entity_type: "complex"
name: "DNA-binding transcriptional repressor MngR"
source_database: "EcoCyc"
source_id: "PC00103"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FarR"
  - "MngR"
---

# DNA-binding transcriptional repressor MngR

`complex.ecocyc.PC00103`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00103`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P13669|protein.P13669]]

## Enriched Summary

According to microarray analysis, the "mannosyl-d-glycerate regulator," MngR, regulates only two genes, mngA and mngB, involved in 2-O-α-mannosyl-D-glycerate utilization . This regulator also autoregulates its own synthesis . Previously, MngR, also called FarR, for fatty acyl-responsive regulator, had been proposed to regulate genes involved in the citric acid cycle in response to fatty acids, which release MngR from its DNA-binding site . However, when it was found that this protein only regulates two genes, the suggestion was rejected and it was proposed that probably high concentrations of fatty acids could degrade the protein instead of it binding to the regulator . By using synthetic gene circuits, it was demonstrated that MngR, contrary to what has been observed for other repressors, represses transcription without evidence of stabilization of RNA polymerase (RNAP) at specific positions relative to the promoter . In contrast, Parisutham et al. reported in vivo measurements consistent with the "stabilizing TF" regime for MngR, in which fold-changes scale approximately with the reciprocal of promoter basal activity, suggesting buffering of promoter-to-promoter variability across promoter contexts and perturbations...

## Annotation

According to microarray analysis, the "mannosyl-d-glycerate regulator," MngR, regulates only two genes, mngA and mngB, involved in 2-O-α-mannosyl-D-glycerate utilization . This regulator also autoregulates its own synthesis . Previously, MngR, also called FarR, for fatty acyl-responsive regulator, had been proposed to regulate genes involved in the citric acid cycle in response to fatty acids, which release MngR from its DNA-binding site . However, when it was found that this protein only regulates two genes, the suggestion was rejected and it was proposed that probably high concentrations of fatty acids could degrade the protein instead of it binding to the regulator . By using synthetic gene circuits, it was demonstrated that MngR, contrary to what has been observed for other repressors, represses transcription without evidence of stabilization of RNA polymerase (RNAP) at specific positions relative to the promoter . In contrast, Parisutham et al. reported in vivo measurements consistent with the "stabilizing TF" regime for MngR, in which fold-changes scale approximately with the reciprocal of promoter basal activity, suggesting buffering of promoter-to-promoter variability across promoter contexts and perturbations . MngR belongs to the GntR family of transcriptional regulators and has a helix-turn-helix motif in the N-terminal domain and a UbiC transcription regulator-associated domain that is predicted to be a sensor for small molecules. This domain is found in proteins such as UbiC from Escherichia coli, TreR from Bacillus subtilis, and HutC from Pseudomonas aeruginosa . The mntR gene is transcribed divergently from the mngAB operon. They share a regulatory region that contains two sites of 21 bp each, one with two direct repeat sequences of 10 bp that are bound b

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P13669|protein.P13669]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PC00103`
- `QSPROTEOME:QS00049744`

## Notes

2*protein.P13669
