---
entity_id: "protein.P22731"
entity_type: "protein"
name: "livF"
source_database: "UniProt"
source_id: "P22731"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livF b3454 JW3419"
---

# livF

`protein.P22731`

## Static

- Type: `protein`
- Source: `UniProt:P22731`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the leucine-specific transport system. LivF is an ATP-binding cassette (ABC) protein that is a component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . The LivF predicted protein sequence contains Walker A and Walker B motifs involved in the binding and hydrolysis of ATP, and the ABC signature motif (also called the linker peptide or C-loop) (and see also ). liv: leucine isoleucine valine

## Biological Role

Component of branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX), leucine / L-phenylalanine ABC transporter (complex.ecocyc.ABC-304-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Component of the leucine-specific transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.ABC-304-CPLX|complex.ecocyc.ABC-304-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3454|gene.b3454]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22731`
- `KEGG:ecj:JW3419;eco:b3454;`
- `GeneID:86862152;86948307;947961;`
- `GO:GO:0005304; GO:0005524; GO:0015188; GO:0015190; GO:0015658; GO:0015803; GO:0015807; GO:0015823; GO:0016020; GO:0016887; GO:0055052; GO:1903714; GO:1903785`

## Notes

High-affinity branched-chain amino acid transport ATP-binding protein LivF (LIV-I protein F)
