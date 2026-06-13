---
entity_id: "complex.ecocyc.CPLX0-8260"
entity_type: "complex"
name: "dTMP kinase"
source_database: "EcoCyc"
source_id: "CPLX0-8260"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dTMP kinase

`complex.ecocyc.CPLX0-8260`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8260`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A720|protein.P0A720]]

## Enriched Summary

dTMP kinase is responsible for catalyzing the ATP-dependent conversion of dTMP to dTDP . In the absence of external dTMP, the enzyme kinetics of dTMP kinase in vivo appear to be cooperative . Unlike the yeast and human analogs, E. coli dTMP kinase is able to phosphorylate the nucleotide analog AZT-MP almost as well as dTMP . Crystal structures of the enzyme in complexes with bisubstrate inhibitors have been solved, showing that the P-loop residue Glu12 interacts differently with the 3'-hydroxyl group of dTMP than the analogous Asp14 residue in the eukaryotic proteins. The Arg153 residue is postulated to stabilize the transition state during catalysis . The antibacterial compound 1-[3-fluoro-4-(5-methyl-2,4-dioxo-pyrimidin-1-yl)phenyl]-3-[2-(trifluoromethyl)phenyl]urea (AZ1) targets dTMP kinase . It was possible to identify the enzyme as the target of AZ1 in a blinded metabolomics experiment . dTMP kinase is also the target of some rhodanine-containing antibiotics . tmk is essential for growth . A temperature-sensitive mutant with lower dTMP kinase activity has been isolated; the mutant shows a 4.4-fold increase in the intracellular dTMP pool . Hypersensitivity of this mutant to 5-bromo-2'-deoxyuridine (BUdR) was shown to be due to the G146A mutation in tmk-1 . dTMP kinase is responsible for catalyzing the ATP-dependent conversion of dTMP to dTDP...

## Biological Role

Catalyzes DTMPKI-RXN (reaction.ecocyc.DTMPKI-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

dTMP kinase is responsible for catalyzing the ATP-dependent conversion of dTMP to dTDP . In the absence of external dTMP, the enzyme kinetics of dTMP kinase in vivo appear to be cooperative . Unlike the yeast and human analogs, E. coli dTMP kinase is able to phosphorylate the nucleotide analog AZT-MP almost as well as dTMP . Crystal structures of the enzyme in complexes with bisubstrate inhibitors have been solved, showing that the P-loop residue Glu12 interacts differently with the 3'-hydroxyl group of dTMP than the analogous Asp14 residue in the eukaryotic proteins. The Arg153 residue is postulated to stabilize the transition state during catalysis . The antibacterial compound 1-[3-fluoro-4-(5-methyl-2,4-dioxo-pyrimidin-1-yl)phenyl]-3-[2-(trifluoromethyl)phenyl]urea (AZ1) targets dTMP kinase . It was possible to identify the enzyme as the target of AZ1 in a blinded metabolomics experiment . dTMP kinase is also the target of some rhodanine-containing antibiotics . tmk is essential for growth . A temperature-sensitive mutant with lower dTMP kinase activity has been isolated; the mutant shows a 4.4-fold increase in the intracellular dTMP pool . Hypersensitivity of this mutant to 5-bromo-2'-deoxyuridine (BUdR) was shown to be due to the G146A mutation in tmk-1 .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A720|protein.P0A720]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8260`
- `QSPROTEOME:QS00188871`

## Notes

2*protein.P0A720
