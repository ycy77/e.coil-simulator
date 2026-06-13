---
entity_id: "protein.P0AEX7"
entity_type: "protein"
name: "livH"
source_database: "UniProt"
source_id: "P0AEX7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livH b3457 JW3422"
---

# livH

`protein.P0AEX7`

## Static

- Type: `protein`
- Source: `UniProt:P0AEX7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for branched-chain amino acids. Probably responsible for the translocation of the substrates across the membrane. LivH is an integral membrane component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . livH encodes a very hydrophobic protein with 7 or 9 predicted transmembrane regions . livH mutant strains (livR livH::Mu) show significantly reduced uptake of L-valine, L-isoleucine and L-leucine . liv: leucine isoleucine valine

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

- `encodes` <-- [[gene.b3457|gene.b3457]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEX7`
- `KEGG:ecj:JW3422;eco:b3457;ecoc:C3026_18725;`
- `GeneID:86862149;93778534;947965;`
- `GO:GO:0005304; GO:0005886; GO:0015188; GO:0015190; GO:0015192; GO:0015658; GO:0015803; GO:0015808; GO:0015823; GO:0016020; GO:0042941; GO:0055052; GO:1903714; GO:1903785; GO:1903801; GO:1903806`

## Notes

High-affinity branched-chain amino acid transport system permease protein LivH (LIV-I protein H)
