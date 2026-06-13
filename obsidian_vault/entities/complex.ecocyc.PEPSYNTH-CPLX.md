---
entity_id: "complex.ecocyc.PEPSYNTH-CPLX"
entity_type: "complex"
name: "phosphoenolpyruvate synthetase"
source_database: "EcoCyc"
source_id: "PEPSYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoenolpyruvate synthetase

`complex.ecocyc.PEPSYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PEPSYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P23538|protein.P23538]]

## Enriched Summary

During growth on three-carbon substrates that require the GLUCONEO-PWY pathway (such as L-LACTATE or PYRUVATE), PEPSYNTH-CPLX provides the ability to generate PHOSPHO-ENOL-PYRUVATE (PEP), which is required for the synthesis of precursor metabolites for cellular carbon compounds . The reaction is thought to proceed in two steps: hydrolysis of ATP, whereby the γ phosphate is released and the β phosphate is transiently attached to a histidine residue within the enzyme, followed by transfer of the phosphate residue to pyruvate, producing PEP . Using multiple methods N-phosphorylation was detected on histidine residue . Nitrogen availability regulates the amount of histidine phosphorylation on PpsA in vivo, and α-ketoglutarate was shown to inhibit phosphotransfer from phosphorylated PpsA to pyruvate . Regulatory mechanisms of the enzymatic activity of PEP synthetase involve phosphorylation and carbon supplies to the cells. CPLX0-7837 (PSRP) catalyzes both the Pi-dependent activation and ADP/ATP-dependent inactivation of PEP synthetase. PEP synthetase was found to be protected from inactivation by the presence of pyruvate . Studies of glucose metabolism in E. coli strains JM109 and BL21 suggested differences in regulation of ppsA in addition to acs and aceBAK, depending upon glucose supply. In strain JM109, low glucose concentrations enhance transcription of these three genes...

## Biological Role

Catalyzes PEPSYNTH-RXN (reaction.ecocyc.PEPSYNTH-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

During growth on three-carbon substrates that require the GLUCONEO-PWY pathway (such as L-LACTATE or PYRUVATE), PEPSYNTH-CPLX provides the ability to generate PHOSPHO-ENOL-PYRUVATE (PEP), which is required for the synthesis of precursor metabolites for cellular carbon compounds . The reaction is thought to proceed in two steps: hydrolysis of ATP, whereby the γ phosphate is released and the β phosphate is transiently attached to a histidine residue within the enzyme, followed by transfer of the phosphate residue to pyruvate, producing PEP . Using multiple methods N-phosphorylation was detected on histidine residue . Nitrogen availability regulates the amount of histidine phosphorylation on PpsA in vivo, and α-ketoglutarate was shown to inhibit phosphotransfer from phosphorylated PpsA to pyruvate . Regulatory mechanisms of the enzymatic activity of PEP synthetase involve phosphorylation and carbon supplies to the cells. CPLX0-7837 (PSRP) catalyzes both the Pi-dependent activation and ADP/ATP-dependent inactivation of PEP synthetase. PEP synthetase was found to be protected from inactivation by the presence of pyruvate . Studies of glucose metabolism in E. coli strains JM109 and BL21 suggested differences in regulation of ppsA in addition to acs and aceBAK, depending upon glucose supply. In strain JM109, low glucose concentrations enhance transcription of these three genes. In strain BL21, the gluconeogenesis pathway is consitutively active . PEP synthetase mutants do not grow on pyruvate, lactate or alanine as the sole source of carbon . The wild-type expression level of ppsA appears to be suboptimal for growth on pyruvate . Expression of ppsA is increased by growth on acetate as the sole source of carbon . A ppsA mutant shows an increased lag time during the diauxic tran

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPSYNTH-RXN|reaction.ecocyc.PEPSYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23538|protein.P23538]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PEPSYNTH-CPLX`
- `QSPROTEOME:QS00049745`

## Notes

2*protein.P23538
