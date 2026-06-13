---
entity_id: "protein.P0AD96"
entity_type: "protein"
name: "livJ"
source_database: "UniProt"
source_id: "P0AD96"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "livJ b3460 JW3425"
---

# livJ

`protein.P0AD96`

## Static

- Type: `protein`
- Source: `UniProt:P0AD96`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: This protein is a component of the leucine, isoleucine, valine, (threonine) transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids. LivJ is the periplasmic binding protein of the LIV-I (LivJHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12 . Early studies suggested that LIV-I served as the entry point for the branched amino acids L-leucine, L-isoleucine, and L-valine and possibly L-alanine, L-threonine and L-serine . The LIV-I system is also able to transport phenylanine and plays a physiologically relevant role in phenylalanine accumulation . LivJ is synthesized as a precursor; a 23 amino acid signal sequence is cleaved upon export to the periplasm . Purified LivJ* binds L-leucine (KD = 0.4 µM), L-isoleucine KD = 0.4 µM) and L-valine (KD = 0.7 µM) (LivJ* denotes a protein that has been engineered with a StyI restriction site added at codon 124). Crystal structures indicate that the protein consists of two globular domains connected by a 3-stranded hinge .

## Biological Role

Component of branched chain amino acid / phenylalanine ABC transporter (complex.ecocyc.ABC-15-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: This protein is a component of the leucine, isoleucine, valine, (threonine) transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3460|gene.b3460]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD96`
- `KEGG:ecj:JW3425;eco:b3460;`
- `GeneID:93778531;947971;`
- `GO:GO:0015803; GO:0015818; GO:0015820; GO:0015829; GO:0016020; GO:0030288; GO:0055052`

## Notes

Leu/Ile/Val-binding protein (LIV-BP)
