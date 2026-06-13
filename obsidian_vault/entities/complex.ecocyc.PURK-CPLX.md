---
entity_id: "complex.ecocyc.PURK-CPLX"
entity_type: "complex"
name: "5-(carboxyamino)imidazole ribonucleotide synthase"
source_database: "EcoCyc"
source_id: "PURK-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-(carboxyamino)imidazole ribonucleotide synthase

`complex.ecocyc.PURK-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PURK-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09029|protein.P09029]]

## Enriched Summary

PurK and PurE were previously thought to be two subunits of AIR carboxylase , although later studies showed the enzymes to be subunits of a distinct carboxylase and mutase, respectively . PurK converts 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR) to the unstable intermediate N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) (the carbamate of AIR) in an ATP-dependent manner by the ligation of bicarbonate to the N5 amino group of AIR . Crystal structures have been determined for PurK in complex with sulfate and MgADP . A later report refined the crystal structure for PurK to 1.6 Å resolution with MgATP, or MgADP/P(i) bound to the active site. The proposed reaction mechanism involves a carboxyphosphate intermediate. The enzyme is not found in humans and is of interest as a target for the design of antimicrobial drugs . While this three domain protein is a member of the ATP grasp superfamily, it lacks conservation within the substrate specificity (Ω) loop . PurK exhibits AIR-dependent ATPase activity that does not show bicarbonate dependence and AIR is not carboxylated during ATP hydrolysis . A high concentration of bicarbonate partially rescues the defect of a purK mutant during growth in the absence of purines, probably by perturbing the balance of AIR toward N5-CAIR. An overproduction of PurE further increases rescue in the presence of bicarbonate...

## Biological Role

Catalyzes RXN0-742 (reaction.ecocyc.RXN0-742).

## Annotation

PurK and PurE were previously thought to be two subunits of AIR carboxylase , although later studies showed the enzymes to be subunits of a distinct carboxylase and mutase, respectively . PurK converts 5-amino-1-(5-phospho-D-ribosyl)imidazole (AIR) to the unstable intermediate N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) (the carbamate of AIR) in an ATP-dependent manner by the ligation of bicarbonate to the N5 amino group of AIR . Crystal structures have been determined for PurK in complex with sulfate and MgADP . A later report refined the crystal structure for PurK to 1.6 Å resolution with MgATP, or MgADP/P(i) bound to the active site. The proposed reaction mechanism involves a carboxyphosphate intermediate. The enzyme is not found in humans and is of interest as a target for the design of antimicrobial drugs . While this three domain protein is a member of the ATP grasp superfamily, it lacks conservation within the substrate specificity (Ω) loop . PurK exhibits AIR-dependent ATPase activity that does not show bicarbonate dependence and AIR is not carboxylated during ATP hydrolysis . A high concentration of bicarbonate partially rescues the defect of a purK mutant during growth in the absence of purines, probably by perturbing the balance of AIR toward N5-CAIR. An overproduction of PurE further increases rescue in the presence of bicarbonate . Nonenzymatic carboxylation of AIR occurs, although under physiological conditions ATP must be added as a second substrate for the AIR carboxylation reaction to occur. PurK is required for AIR conversion to 5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate (CAIR) under low bicarbonate concentrations . The overproduction and purification of PurK has been reported . Analysis of the purE locus at the nucleotide sequence le

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-742|reaction.ecocyc.RXN0-742]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P09029|protein.P09029]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PURK-CPLX`
- `QSPROTEOME:QS00188559`

## Notes

2*protein.P09029
