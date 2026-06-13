---
entity_id: "complex.ecocyc.CPLX0-8593"
entity_type: "complex"
name: "DNA-binding transcriptional dual regulator NanR"
source_database: "EcoCyc"
source_id: "CPLX0-8593"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional dual regulator NanR

`complex.ecocyc.CPLX0-8593`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8593`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8W0|protein.P0A8W0]]

## Enriched Summary

The genes regulated by NanR, "N-acetyl-neuraminic acid regulator," are involved in N-acetyl-neuraminic acid (or sialic acid) transport and metabolism and in OFF/ON switching of type 1 fimbriation. N-acetylneuraminate (Neu5Ac), which is the most common sialic acid, induces the catabolism of sialic acids operons by directly inactivating NanR , converting the predominantly dimeric form of the repressor to an inactive monomer . NanR is a member of the FadR/GntR family. Members of this family have two domains, an N-terminal domain with a helix-turn-helix DNA-binding motif and a C-terminal domain with dimerization and effector-binding motifs. Three-dimensional models of the N terminus of FadR and NanR show topological similarities and a ~26% sequence identity between them . The NanR dimer regulates transcription when it binds, in an asymmetric manner, to a region of ~30 bp that contains a set of conserved operators with two or three exact, or nearly exact, repeats of the hexanucleotide sequence GGTATA; this binding occurs in a cooperative way and is mediated by an N-terminal extension of 32 residues in NanR . However, this protein can be displaced from this region byN-acetyl-neuraminic acid (Neu5Ac), which causes a conformational change in the protein...

## Biological Role

Component of NanR-N-acetylneuraminate (complex.ecocyc.MONOMER0-2341).

## Annotation

The genes regulated by NanR, "N-acetyl-neuraminic acid regulator," are involved in N-acetyl-neuraminic acid (or sialic acid) transport and metabolism and in OFF/ON switching of type 1 fimbriation. N-acetylneuraminate (Neu5Ac), which is the most common sialic acid, induces the catabolism of sialic acids operons by directly inactivating NanR , converting the predominantly dimeric form of the repressor to an inactive monomer . NanR is a member of the FadR/GntR family. Members of this family have two domains, an N-terminal domain with a helix-turn-helix DNA-binding motif and a C-terminal domain with dimerization and effector-binding motifs. Three-dimensional models of the N terminus of FadR and NanR show topological similarities and a ~26% sequence identity between them . The NanR dimer regulates transcription when it binds, in an asymmetric manner, to a region of ~30 bp that contains a set of conserved operators with two or three exact, or nearly exact, repeats of the hexanucleotide sequence GGTATA; this binding occurs in a cooperative way and is mediated by an N-terminal extension of 32 residues in NanR . However, this protein can be displaced from this region byN-acetyl-neuraminic acid (Neu5Ac), which causes a conformational change in the protein . One dimer of NarR binding to a molecule of Neu5Ac causes alteration of the DNA binding activity of the protein but not its oligomeric state . When this protein is repressing transcription, it overlaps the whole promoter region . The region of 30 bp that NanR binds to is close to a Dam methylation site (GATC) that appears to be necessary for induction of some genes of the NanR regulon . Methylation in these sites is prevented by NanR binding . NarR is also able to bind zinc . Kalivoda et. al. (2013) have suggested that the term

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2341|complex.ecocyc.MONOMER0-2341]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8W0|protein.P0A8W0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8593`
- `QSPROTEOME:QS00188485`

## Notes

2*protein.P0A8W0
