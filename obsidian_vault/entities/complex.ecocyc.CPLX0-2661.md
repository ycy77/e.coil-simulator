---
entity_id: "complex.ecocyc.CPLX0-2661"
entity_type: "complex"
name: "McrBC restriction endonuclease"
source_database: "EcoCyc"
source_id: "CPLX0-2661"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# McrBC restriction endonuclease

`complex.ecocyc.CPLX0-2661`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2661`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15005|protein.P15005]], [[protein.P15006|protein.P15006]]

## Enriched Summary

McrBC is a type IV deoxyribonuclease and is one of three restriction systems defending E. coli K-12 against foreign DNA, such as bacteriophages. McrBC is active on many different methylated sites . It recognizes DNA containing two methylated cytosine residues separated by 30-2000 base pairs and cleaves the DNA at multiple sites one to five helical turns away from the methylated sites . A ratio of 3-5 McrB molecules per McrC is optimal for DNA cleavage; McrBS enhances or decreases the DNase activity of McrBC depending on the McrB/McrC ratio . In the presence of GTP, McrBC forms high molecular mass complexes both in the absence and presence of DNA . Cryo-EM shows hexameric ring structures formed by McrB ; crystal structures of the McrBC complex show a dumbbell-shaped structure formed by two hexameric McrB rings that are connected via two McrC molecules . McrBC complex formation appears to precede GTP hydrolysis . Exposure to UV light reduces the activity of the McrBC restriction system on introduced phage DNA in a time- and dose-dependent manner . A later publication disputed this finding. Restriction of methylated DNA is responsible for difficulties with cloning methylcytosine-containing DNA from various sources in E. coli . Mcr: "modified cytosine restriction" Reviews: McrBC is a type IV deoxyribonuclease and is one of three restriction systems defending E...

## Biological Role

Catalyzes RXN0-2941 (reaction.ecocyc.RXN0-2941). Bound by GTP (molecule.C00044), Magnesium cation (molecule.C00305).

## Annotation

McrBC is a type IV deoxyribonuclease and is one of three restriction systems defending E. coli K-12 against foreign DNA, such as bacteriophages. McrBC is active on many different methylated sites . It recognizes DNA containing two methylated cytosine residues separated by 30-2000 base pairs and cleaves the DNA at multiple sites one to five helical turns away from the methylated sites . A ratio of 3-5 McrB molecules per McrC is optimal for DNA cleavage; McrBS enhances or decreases the DNase activity of McrBC depending on the McrB/McrC ratio . In the presence of GTP, McrBC forms high molecular mass complexes both in the absence and presence of DNA . Cryo-EM shows hexameric ring structures formed by McrB ; crystal structures of the McrBC complex show a dumbbell-shaped structure formed by two hexameric McrB rings that are connected via two McrC molecules . McrBC complex formation appears to precede GTP hydrolysis . Exposure to UV light reduces the activity of the McrBC restriction system on introduced phage DNA in a time- and dose-dependent manner . A later publication disputed this finding. Restriction of methylated DNA is responsible for difficulties with cloning methylcytosine-containing DNA from various sources in E. coli . Mcr: "modified cytosine restriction" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2941|reaction.ecocyc.RXN0-2941]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P15005|protein.P15005]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P15006|protein.P15006]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-2661`
- `PDB:6HZ9`
- `PDB:6HZ8`
- `PDB:6HZ7`
- `PDB:6HZ6`
- `PDB:6HZ5`
- `PDB:6HZ4`
- `PDB:6UT6`
- `PDB:7VSR`

## Notes

12*protein.P15005|2*protein.P15006
