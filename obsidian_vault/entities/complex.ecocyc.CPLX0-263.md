---
entity_id: "complex.ecocyc.CPLX0-263"
entity_type: "complex"
name: "isoaspartyl dipeptidase / asparaginase 3"
source_database: "EcoCyc"
source_id: "CPLX0-263"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "asparaginase III"
  - "AIII"
---

# isoaspartyl dipeptidase / asparaginase 3

`complex.ecocyc.CPLX0-263`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-263`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37595|protein.P37595]], [[protein.P37595|protein.P37595]]

## Enriched Summary

E. coli encodes three enzymes with asparaginase activity . The IaaA protein is a prototypic class 2-type asparaginase, also called asparaginase III (AIII), that belongs to the family of N-terminal nucleophile (Ntn)-hydrolases. However, IaaA is referred to as an isoaspartyl dipeptidase because its isoaspartyl dipeptidase activity predominates compared to the relatively weak asparaginase activity of IaaA . Like other Ntn-hydrolases, IaaA is first synthesized as a proenzyme which undergoes autocatalytic cleavage, producing two smaller subunits that combine to form an αβ-heterodimer . There is evidence for further processing of the α and β peptides . Autocatalytic cleavage generates the freed N-terminal nucleophilic threonine residue of the β subunit, T179. A T179A mutant folds correctly, but is not processed. A mechanism for autocatalytic cleavage has been proposed and additional structural requirements for autoprocessing have been identified . L-asparaginase activity of variants derived from random mutagenesis identified several amino acid residues important for active site stability and enzymatic activity; Arg207 and Asp211 are involved in substrate binding and necessary for L-asparaginase activity . Crystal structures of wild-type IaaA alone and in complex with L-aspartate, an active site mutant, and random mutagenesis-derived variants have been determined...

## Biological Role

Catalyzes ASPARAGHYD-RXN (reaction.ecocyc.ASPARAGHYD-RXN), RXN0-3241 (reaction.ecocyc.RXN0-3241).

## Annotation

E. coli encodes three enzymes with asparaginase activity . The IaaA protein is a prototypic class 2-type asparaginase, also called asparaginase III (AIII), that belongs to the family of N-terminal nucleophile (Ntn)-hydrolases. However, IaaA is referred to as an isoaspartyl dipeptidase because its isoaspartyl dipeptidase activity predominates compared to the relatively weak asparaginase activity of IaaA . Like other Ntn-hydrolases, IaaA is first synthesized as a proenzyme which undergoes autocatalytic cleavage, producing two smaller subunits that combine to form an αβ-heterodimer . There is evidence for further processing of the α and β peptides . Autocatalytic cleavage generates the freed N-terminal nucleophilic threonine residue of the β subunit, T179. A T179A mutant folds correctly, but is not processed. A mechanism for autocatalytic cleavage has been proposed and additional structural requirements for autoprocessing have been identified . L-asparaginase activity of variants derived from random mutagenesis identified several amino acid residues important for active site stability and enzymatic activity; Arg207 and Asp211 are involved in substrate binding and necessary for L-asparaginase activity . Crystal structures of wild-type IaaA alone and in complex with L-aspartate, an active site mutant, and random mutagenesis-derived variants have been determined. The two subunits have distinct structural changes and may be intrinsically non-equivalent . A structure of a M200W mutant allowed a high-resolution observation of an acyl-enzyme intermediate, revealing H-bonds between the substrate and the guanidinium group of Arg207 . Results reported in may have been due to a polar effect on downstream genes encoding a glutationine transporter . Spt: "sulfur peptide transport" IaaA

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ASPARAGHYD-RXN|reaction.ecocyc.ASPARAGHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3241|reaction.ecocyc.RXN0-3241]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37595|protein.P37595]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-263`
- `QSPROTEOME:QS00188641`
- `PDB:3C17`
- `PDB:2ZAK`
- `PDB:1T3M`
- `PDB:1K2X`
- `PDB:1JN9`
- `PDB:2ZAL`

## Notes

2*protein.P37595|2*protein.P37595
