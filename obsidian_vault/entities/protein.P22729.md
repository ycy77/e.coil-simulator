---
entity_id: "protein.P22729"
entity_type: "protein"
name: "livM"
source_database: "UniProt"
source_id: "P22729"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livM b3456 JW3421"
---

# livM

`protein.P22729`

## Static

- Type: `protein`
- Source: `UniProt:P22729`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for branched-chain amino acids. Probably responsible for the translocation of the substrates across the membrane. LivM is an integral membrane component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . livM encodes a very hydrophobic protein with 9 predicted transmembrane regions . liv: leucine isoleucine valine

## Biological Role

Component of branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX), leucine / L-phenylalanine ABC transporter (complex.ecocyc.ABC-304-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for branched-chain amino acids. Probably responsible for the translocation of the substrates across the membrane.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-304-CPLX|complex.ecocyc.ABC-304-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3456|gene.b3456]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22729`
- `KEGG:ecj:JW3421;eco:b3456;ecoc:C3026_18720;`
- `GeneID:947966;`
- `GO:GO:0005304; GO:0005886; GO:0015188; GO:0015190; GO:0015192; GO:0015658; GO:0015803; GO:0015823; GO:0016020; GO:0055052; GO:1903714; GO:1903785`

## Notes

High-affinity branched-chain amino acid transport system permease protein LivM (LIV-I protein M)
