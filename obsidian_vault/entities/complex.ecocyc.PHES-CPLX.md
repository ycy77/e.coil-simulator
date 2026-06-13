---
entity_id: "complex.ecocyc.PHES-CPLX"
entity_type: "complex"
name: "phenylalanine—tRNA ligase"
source_database: "EcoCyc"
source_id: "PHES-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PheRS"
---

# phenylalanine—tRNA ligase

`complex.ecocyc.PHES-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PHES-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08312|protein.P08312]], [[protein.P07395|protein.P07395]]

## Enriched Summary

Phenylalanine-tRNA ligase (PheRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. PheRS belongs to the Class IIC aminoacyl tRNA synthetases . PheRS is a tetramer consisting of two α and two β subunits. Both subunits are required for catalytic activity . Two molecules of tRNAPhe bind to one PheRS complex , and both binding sites are active sites . Binding is not dependent on Mg2+ . A crystal structure of PheRS in a complex with phenylalanine and AMP has been solved at 3.05 Å resolution, revealing structural differences between the E. coli and T. thermophilus enzymes . The reaction mechanism of PheRS includes the formation of an aminoacyl adenylate intermediate, which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction . Binding of tRNAPhe to PheRS induces a conformational change in the tRNA as well as in PheRS . Aminoacylation is limited by the kinetics of a conformational change of the PheRS-Phe-tRNAPhe complex . PheRS can aminoacylate a synthetic substrate with a deoxyribose backbone (tDNA) . Specificity determinants within tRNAPhe that are important for recognition by PheRS, for attenuation, and for editing have been identified...

## Biological Role

Catalyzes PHENYLALANINE--TRNA-LIGASE-RXN (reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN), RXN-23957 (reaction.ecocyc.RXN-23957), RXN-23958 (reaction.ecocyc.RXN-23958). Bound by Magnesium cation (molecule.C00305).

## Annotation

Phenylalanine-tRNA ligase (PheRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. PheRS belongs to the Class IIC aminoacyl tRNA synthetases . PheRS is a tetramer consisting of two α and two β subunits. Both subunits are required for catalytic activity . Two molecules of tRNAPhe bind to one PheRS complex , and both binding sites are active sites . Binding is not dependent on Mg2+ . A crystal structure of PheRS in a complex with phenylalanine and AMP has been solved at 3.05 Å resolution, revealing structural differences between the E. coli and T. thermophilus enzymes . The reaction mechanism of PheRS includes the formation of an aminoacyl adenylate intermediate, which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction . Binding of tRNAPhe to PheRS induces a conformational change in the tRNA as well as in PheRS . Aminoacylation is limited by the kinetics of a conformational change of the PheRS-Phe-tRNAPhe complex . PheRS can aminoacylate a synthetic substrate with a deoxyribose backbone (tDNA) . Specificity determinants within tRNAPhe that are important for recognition by PheRS, for attenuation, and for editing have been identified . A synthetically constructed tRNAPhe(AAA) is not a good substrate for PheRS . Specificity determinants and residues within PheRS that are important for catalytic activity have been investigated . The Ala294 residue of the α subunit is involved in binding phenylalanine and influences amino acid specificity by determining of the size of the binding pocket . A proofreading mechanism hydrolyzes a PheRS-tyrosine adenylate complex and Tyr-tRNAPhe . The editing site localizes

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN|reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23957|reaction.ecocyc.RXN-23957]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23958|reaction.ecocyc.RXN-23958]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P07395|protein.P07395]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P08312|protein.P08312]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHES-CPLX`
- `PDB:3PCO`
- `PDB:6P24`
- `PDB:6P26`
- `PDB:6OZ5`
- `QSPROTEOME:QS00173837`

## Notes

2*protein.P08312|2*protein.P07395
