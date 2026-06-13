---
entity_id: "protein.P0A9S7"
entity_type: "protein"
name: "livG"
source_database: "UniProt"
source_id: "P0A9S7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livG b3455 JW3420"
---

# livG

`protein.P0A9S7`

## Static

- Type: `protein`
- Source: `UniProt:P0A9S7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the leucine-specific transport system. LivG is an ATP-binding cassette (ABC) protein that is a component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . The LivG predicted protein sequence contains Walker A and Walker B motifs involved in the binding and hydrolysis of ATP . liv: leucine isoleucine valine

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

- `encodes` <-- [[gene.b3455|gene.b3455]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9S7`
- `KEGG:ecj:JW3420;eco:b3455;ecoc:C3026_18715;`
- `GeneID:86948308;89518287;947967;`
- `GO:GO:0005304; GO:0005524; GO:0005886; GO:0015188; GO:0015190; GO:0015192; GO:0015658; GO:0015803; GO:0015808; GO:0015823; GO:0016020; GO:0016887; GO:0042941; GO:0055052; GO:1903714; GO:1903785; GO:1903805; GO:1903806`

## Notes

High-affinity branched-chain amino acid transport ATP-binding protein LivG (LIV-I protein G)
