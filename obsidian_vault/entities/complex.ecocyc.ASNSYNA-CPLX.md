---
entity_id: "complex.ecocyc.ASNSYNA-CPLX"
entity_type: "complex"
name: "asparagine synthetase A"
source_database: "EcoCyc"
source_id: "ASNSYNA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# asparagine synthetase A

`complex.ecocyc.ASNSYNA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASNSYNA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00963|protein.P00963]]

## Enriched Summary

Asparagine synthetase A (AsnA) is one of two asparagine synthetases in E. coli, catalyzing the ammonia-dependent conversion of aspartate to asparagine. AsnA is the more active of two unrelated asparagine synthetases in E. coli . Various lines of evidence suggest that AsnA evolved from an ancestral aminoacyl-tRNA synthetase. In early biochemical studies of the enzyme, a two-step reaction mechanism involving the formation of an aspartyl enzyme intermediate was proposed . Later, it was shown that any mutation of the R298 residue, which corresponds to an invariant arginine residue in class II aminoacyl-tRNA synthetases, results in loss of enzymatic activity . Crystal structures of AsnA revealed similarity of the overall structure, conserved active site architecture and catalytic residues to the catalytic domain of yeast aspartyl-tRNA synthetase . In addition to its role in metabolism, AsnA was found to be involved in the production of a linear peptide with the amino acid sequence Asn-Asn-Trp-Asn-Asn (NNWNN) that acts as an "extracellular death factor" (EDF) for MazEF-mediated cell death . Deletion of asnA prevents production of active EDF . Amidation of the aspartate residue within the NNWDN peptide derived from GLU6PDEHYDROG-MONOMER appears to occur during the formation of the EDF pentapeptide . Transcription of asnA is positively regulated by AsnC in the absence of asparagine...

## Biological Role

Catalyzes ASNSYNA-RXN (reaction.ecocyc.ASNSYNA-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Asparagine synthetase A (AsnA) is one of two asparagine synthetases in E. coli, catalyzing the ammonia-dependent conversion of aspartate to asparagine. AsnA is the more active of two unrelated asparagine synthetases in E. coli . Various lines of evidence suggest that AsnA evolved from an ancestral aminoacyl-tRNA synthetase. In early biochemical studies of the enzyme, a two-step reaction mechanism involving the formation of an aspartyl enzyme intermediate was proposed . Later, it was shown that any mutation of the R298 residue, which corresponds to an invariant arginine residue in class II aminoacyl-tRNA synthetases, results in loss of enzymatic activity . Crystal structures of AsnA revealed similarity of the overall structure, conserved active site architecture and catalytic residues to the catalytic domain of yeast aspartyl-tRNA synthetase . In addition to its role in metabolism, AsnA was found to be involved in the production of a linear peptide with the amino acid sequence Asn-Asn-Trp-Asn-Asn (NNWNN) that acts as an "extracellular death factor" (EDF) for MazEF-mediated cell death . Deletion of asnA prevents production of active EDF . Amidation of the aspartate residue within the NNWDN peptide derived from GLU6PDEHYDROG-MONOMER appears to occur during the formation of the EDF pentapeptide . Transcription of asnA is positively regulated by AsnC in the absence of asparagine . AsnA: "asparagine synthetase A" Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASNSYNA-RXN|reaction.ecocyc.ASNSYNA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00963|protein.P00963]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASNSYNA-CPLX`
- `QSPROTEOME:QS00182045`

## Notes

2*protein.P00963
