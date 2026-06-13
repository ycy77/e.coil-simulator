---
entity_id: "complex.ecocyc.CPLX0-11240"
entity_type: "complex"
name: "putative RNase adaptor protein YicC"
source_database: "EcoCyc"
source_id: "CPLX0-11240"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative RNase adaptor protein YicC

`complex.ecocyc.CPLX0-11240`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-11240`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23839|protein.P23839]]

## Enriched Summary

YicC is an mRNA degrading RNase. It specifically interferes with the function of SRAI-RNA by enabling its degradation by EG10743-MONOMER PNPase . It is one of three proteins of the Uncharacterized Protein Family, UPF0701, along with the Bacillus subtilis endonuclease YloC to which it shares 30% amino acid identity and exhibits identical cleavage patterns for various RNA oligo substrates . In vitro RNA cleavage assays identified GUG as the consensus motif . A low resolution (~4.0 Å) crystal structure of YicC found three monomers forming a concave boat-shaped trimer, two of which come together to form an inverted funnel-shaped hexamer. Surface potential analysis identified the catalytic residue as E252, active site region residues and RNA-binding groove residues, most of which are conserved and localized in the C-terminus; mutations of key residues substantiated the RNA-binding capabilities . A higher resolution (2.8 Å) structure of the apo-YicC, cryoEM of an RNA bound YicC complex, mutational and biochemical studies confirms the hexameric complex and active site residues, but also reveals additional features including conformational changes upon binding to RNA . A yicC dinD double insertion mutant is heat sensitive and shows a filamentous phenotype in stationary phase . Overproduction of yicC in an otherwise wild type background leads to reduced levels of RyhB and SRAD-RNA...

## Biological Role

Catalyzes 3.1.27.6-RXN (reaction.ecocyc.3.1.27.6-RXN).

## Annotation

YicC is an mRNA degrading RNase. It specifically interferes with the function of SRAI-RNA by enabling its degradation by EG10743-MONOMER PNPase . It is one of three proteins of the Uncharacterized Protein Family, UPF0701, along with the Bacillus subtilis endonuclease YloC to which it shares 30% amino acid identity and exhibits identical cleavage patterns for various RNA oligo substrates . In vitro RNA cleavage assays identified GUG as the consensus motif . A low resolution (~4.0 Å) crystal structure of YicC found three monomers forming a concave boat-shaped trimer, two of which come together to form an inverted funnel-shaped hexamer. Surface potential analysis identified the catalytic residue as E252, active site region residues and RNA-binding groove residues, most of which are conserved and localized in the C-terminus; mutations of key residues substantiated the RNA-binding capabilities . A higher resolution (2.8 Å) structure of the apo-YicC, cryoEM of an RNA bound YicC complex, mutational and biochemical studies confirms the hexameric complex and active site residues, but also reveals additional features including conformational changes upon binding to RNA . A yicC dinD double insertion mutant is heat sensitive and shows a filamentous phenotype in stationary phase . Overproduction of yicC in an otherwise wild type background leads to reduced levels of RyhB and SRAD-RNA . yicC belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.27.6-RXN|reaction.ecocyc.3.1.27.6-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P23839|protein.P23839]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-11240`
- `QSPROTEOME:QS00196199`

## Notes

6*protein.P23839
