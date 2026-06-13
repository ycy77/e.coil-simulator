---
entity_id: "complex.ecocyc.CPLX0-245"
entity_type: "complex"
name: "alkyl hydroperoxide reductase"
source_database: "EcoCyc"
source_id: "CPLX0-245"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# alkyl hydroperoxide reductase

`complex.ecocyc.CPLX0-245`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-245`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AE08|protein.P0AE08]], [[protein.P35340|protein.P35340]]

## Enriched Summary

Alkyl hydroperoxide reductase converts alkyl hydroperoxides to their corresponding alcohols. By similarity to the enzyme from Salmonella typhimurium, the AhpC component catalyzes the peroxide reductase reaction, while the AhpF component restores the reduced state of AhpC by transferring electrons from NADH to AhpC. Based on structural data, a model of the catalytic cycle has been proposed . The binding interface between AhpC and AhpF was mapped by NMR. The C-terminal tail of AhpC wraps around the N-terminal domain of AhpF and slows dissociation. Upon reduction, a conformational change of the CTD of AhpC mediates release of AhpF . A solution structure of the enzymatically active complex reveals how the extended conformation of dimeric AhpF enables contacts with the redox-active disulfide center of AhpC and electron transfer Alkyl hydroperoxide reductase is responsible for scavenging HYDROGEN-PEROXIDE at low concentrations, while catalase is responsible for scavenging H2O2 at high concentrations . Overexpression of alkyl hydroperoxide reductase leads to increased resistance to cumene hydroperoxide and other redox-cycling agents . An ahpCF mutant is more sensitive to the increased endogenous production of peroxides during phosphate starvation and has a severe growth defect when grown on phenylethylamine . An insertion mutant in the ahpC promoter region is cold sensitive...

## Biological Role

Catalyzes R4-RXN (reaction.ecocyc.R4-RXN). Bound by FAD (molecule.C00016).

## Annotation

Alkyl hydroperoxide reductase converts alkyl hydroperoxides to their corresponding alcohols. By similarity to the enzyme from Salmonella typhimurium, the AhpC component catalyzes the peroxide reductase reaction, while the AhpF component restores the reduced state of AhpC by transferring electrons from NADH to AhpC. Based on structural data, a model of the catalytic cycle has been proposed . The binding interface between AhpC and AhpF was mapped by NMR. The C-terminal tail of AhpC wraps around the N-terminal domain of AhpF and slows dissociation. Upon reduction, a conformational change of the CTD of AhpC mediates release of AhpF . A solution structure of the enzymatically active complex reveals how the extended conformation of dimeric AhpF enables contacts with the redox-active disulfide center of AhpC and electron transfer Alkyl hydroperoxide reductase is responsible for scavenging HYDROGEN-PEROXIDE at low concentrations, while catalase is responsible for scavenging H2O2 at high concentrations . Overexpression of alkyl hydroperoxide reductase leads to increased resistance to cumene hydroperoxide and other redox-cycling agents . An ahpCF mutant is more sensitive to the increased endogenous production of peroxides during phosphate starvation and has a severe growth defect when grown on phenylethylamine . An insertion mutant in the ahpC promoter region is cold sensitive . An ahpCF mutant shows increased doubling time under conditions of high osmolality . A multiomics analysis of an Ahp knockout mutant exhibited morphological changes, increased levels of H2O2 and other reactive oxygen species, activated the oxidative stress regulator, PD00214 OxyR, disrupted the cellular redox balance and shifted to anaerobic respiration and fermentation even when sufficient O2 was present

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.R4-RXN|reaction.ecocyc.R4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AE08|protein.P0AE08]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10
- `is_component_of` <-- [[protein.P35340|protein.P35340]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-245`
- `QSPROTEOME:QS00170511`

## Notes

10*protein.P0AE08|2*protein.P35340
