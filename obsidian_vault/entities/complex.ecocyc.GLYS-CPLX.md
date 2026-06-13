---
entity_id: "complex.ecocyc.GLYS-CPLX"
entity_type: "complex"
name: "glycine—tRNA ligase"
source_database: "EcoCyc"
source_id: "GLYS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GlyRS"
---

# glycine—tRNA ligase

`complex.ecocyc.GLYS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00961|protein.P00961]], [[protein.P00960|protein.P00960]]

## Enriched Summary

Glycine-tRNA ligase (GlyRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. GlyRS belongs to the Class IIC aminoacyl tRNA synthetases . GlyRS is a heterotetramer consisting of two α and two β subunits. Both subunits are required for catalytic activity . An enzyme in which the α and β subunits are fused into a single polypeptide chain is catalytically active . A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . The reaction mechanism of GlyRS includes the formation of an aminoacyl adenylate intermediate , which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction. Specificity determinants within tRNAGly that are important for recognition by GlyRS have been identified . The tRNA binding site is located in the β subunit of GlyRS . The synthesis of GlyRS is growth rate-dependent...

## Biological Role

Catalyzes GLYCINE--TRNA-LIGASE-RXN (reaction.ecocyc.GLYCINE--TRNA-LIGASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Glycine-tRNA ligase (GlyRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. GlyRS belongs to the Class IIC aminoacyl tRNA synthetases . GlyRS is a heterotetramer consisting of two α and two β subunits. Both subunits are required for catalytic activity . An enzyme in which the α and β subunits are fused into a single polypeptide chain is catalytically active . A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . The reaction mechanism of GlyRS includes the formation of an aminoacyl adenylate intermediate , which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction. Specificity determinants within tRNAGly that are important for recognition by GlyRS have been identified . The tRNA binding site is located in the β subunit of GlyRS . The synthesis of GlyRS is growth rate-dependent . Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYCINE--TRNA-LIGASE-RXN|reaction.ecocyc.GLYCINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00960|protein.P00960]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P00961|protein.P00961]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYS-CPLX`
- `PDB:7EIV`
- `PDB:7YSE`
- `PDB:7EIV`
- `QSPROTEOME:QS00170495`

## Notes

2*protein.P00961|2*protein.P00960
