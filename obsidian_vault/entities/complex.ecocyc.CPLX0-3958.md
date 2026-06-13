---
entity_id: "complex.ecocyc.CPLX0-3958"
entity_type: "complex"
name: "EcoKI restriction-modification system"
source_database: "EcoCyc"
source_id: "CPLX0-3958"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# EcoKI restriction-modification system

`complex.ecocyc.CPLX0-3958`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3958`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08957|protein.P08957]], [[protein.P08956|protein.P08956]], [[protein.P05719|protein.P05719]]

## Enriched Summary

EcoKI is the type IA restriction-modification enzyme complex responsible for identifying and restricting unmethylated, foreign DNA and for modifying native, hemimethylated DNA by methylation for self-identification. The three proteins which make up EcoKI-HsdR, HsdM, and HsdS-are all required for restriction. There is a complex that can form-HsdM2HsdS1-with only methyltransferase activity. HsdM and HsdS are required for methylation. HsdM contains a methyltransferase active site and a site for cofactor binding. The cofactor S-adenosylmethionine (AdoMet) acts as the methyl donor for modification. Hemimethylated DNA is preferred over unmethylated DNA as substrate for modification. Interaction of HsdS with DNA requires HsdM. HsdS contains two target recognition domains which recognize the sequence 5'AAC(N6)GTGC. One recognizes the AAC sequence, while the other recognizes the GTGC sequence. HsdR couples DNA translocation to ATP hydrolysis and contains the catalytic site for restriction of the DNA. When the EcoKI binds its target sequence, it makes another contact with the DNA which begins translocation of the DNA while still remaining bound to the target sequence, creating loops...

## Biological Role

Catalyzes 3.1.21.3-RXN (reaction.ecocyc.3.1.21.3-RXN).

## Annotation

EcoKI is the type IA restriction-modification enzyme complex responsible for identifying and restricting unmethylated, foreign DNA and for modifying native, hemimethylated DNA by methylation for self-identification. The three proteins which make up EcoKI-HsdR, HsdM, and HsdS-are all required for restriction. There is a complex that can form-HsdM2HsdS1-with only methyltransferase activity. HsdM and HsdS are required for methylation. HsdM contains a methyltransferase active site and a site for cofactor binding. The cofactor S-adenosylmethionine (AdoMet) acts as the methyl donor for modification. Hemimethylated DNA is preferred over unmethylated DNA as substrate for modification. Interaction of HsdS with DNA requires HsdM. HsdS contains two target recognition domains which recognize the sequence 5'AAC(N6)GTGC. One recognizes the AAC sequence, while the other recognizes the GTGC sequence. HsdR couples DNA translocation to ATP hydrolysis and contains the catalytic site for restriction of the DNA. When the EcoKI binds its target sequence, it makes another contact with the DNA which begins translocation of the DNA while still remaining bound to the target sequence, creating loops. Restriction occurs when translocation becomes stalled because enzymes run into each other, when DNA becomes too supercoiled, when the loop of DNA between two dimerized enzymes becomes taut, and when the enzyme becomes blocked, such as at Holliday junctions. Endonucleolytic activity requires Mg2+, ATP, and AdoMet .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.21.3-RXN|reaction.ecocyc.3.1.21.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P05719|protein.P05719]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P08956|protein.P08956]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P08957|protein.P08957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3958`
- `PDB:2Y7C`
- `PDB:2Y7H`
- `QSPROTEOME:QS00173487`

## Notes

2*protein.P08957|2*protein.P08956|1*protein.P05719
