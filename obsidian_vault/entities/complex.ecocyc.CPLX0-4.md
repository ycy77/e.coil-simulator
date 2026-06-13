---
entity_id: "complex.ecocyc.CPLX0-4"
entity_type: "complex"
name: "aromatic carboxylic acid efflux pump"
source_database: "EcoCyc"
source_id: "CPLX0-4"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AaeAB"
---

# aromatic carboxylic acid efflux pump

`complex.ecocyc.CPLX0-4`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-4`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P46482|protein.P46482]], [[protein.P46481|protein.P46481]]

## Enriched Summary

The aaeA and aaeB genes are members of the aaeXAB operon. Informatics analysis indicates that AaeA is a membrane fusion protein (MFP) family protein, and forms an efflux pump with AaeB , which is a member of the putative efflux transport (PET) family of proteins. PET family proteins are often located in operons with MFP family proteins that function in efflux transport. PET family proteins are believed to be membrane localized, having 12 predicted transmembrane segments in gram-negative bacteria . DNA microarray analysis has shown that the aaeXAB operon is upregulated by growth in p-hydroxybenzoic acid (pHBA). Growth inhibition tests and Phenotype Microarrays show that an aaeB mutant is hypersensitive to hydroxylated, aromatic carboxylic acids including pHBA, 6-hydroxy-2-naphthoic acid, and 2-hydroxycinnamate. In a mutant of AaeR, which mutation and gene fusion studies show is a positive transcription factor for the divergently transcribed aaeXAB operon, mutation and expression studies show that both AaeA and AaeB are required for pHBA resistance and presumably function together as an efflux system for hydroxylated, aromatic carboxylic acids . The aaeA and aaeB genes are members of the aaeXAB operon...

## Biological Role

Catalyzes 4-hydroxybenzoate:proton antiport (reaction.ecocyc.TRANS-RXN0-233). Transports 4-Hydroxybenzoate (molecule.C00156), hν (molecule.ecocyc.Light).

## Annotation

The aaeA and aaeB genes are members of the aaeXAB operon. Informatics analysis indicates that AaeA is a membrane fusion protein (MFP) family protein, and forms an efflux pump with AaeB , which is a member of the putative efflux transport (PET) family of proteins. PET family proteins are often located in operons with MFP family proteins that function in efflux transport. PET family proteins are believed to be membrane localized, having 12 predicted transmembrane segments in gram-negative bacteria . DNA microarray analysis has shown that the aaeXAB operon is upregulated by growth in p-hydroxybenzoic acid (pHBA). Growth inhibition tests and Phenotype Microarrays show that an aaeB mutant is hypersensitive to hydroxylated, aromatic carboxylic acids including pHBA, 6-hydroxy-2-naphthoic acid, and 2-hydroxycinnamate. In a mutant of AaeR, which mutation and gene fusion studies show is a positive transcription factor for the divergently transcribed aaeXAB operon, mutation and expression studies show that both AaeA and AaeB are required for pHBA resistance and presumably function together as an efflux system for hydroxylated, aromatic carboxylic acids .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-233|reaction.ecocyc.TRANS-RXN0-233]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00156|molecule.C00156]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P46481|protein.P46481]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P46482|protein.P46482]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-4`
- `QSPROTEOME:QS00196519`

## Notes

protein.P46482|protein.P46481
