---
entity_id: "protein.P27828"
entity_type: "protein"
name: "wecB"
source_database: "UniProt"
source_id: "P27828"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02028, ECO:0000269|PubMed:8226648}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecB nfrC rffE yifF b3786 JW5600"
---

# wecB

`protein.P27828`

## Static

- Type: `protein`
- Source: `UniProt:P27828`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02028, ECO:0000269|PubMed:8226648}.

## Enriched Summary

FUNCTION: Catalyzes the reversible epimerization at C-2 of UDP-N-acetylglucosamine (UDP-GlcNAc) and thereby provides bacteria with UDP-N-acetylmannosamine (UDP-ManNAc), the activated donor of ManNAc residues. Also involved in bacteriophage N4 adsorption. {ECO:0000269|PubMed:15210128, ECO:0000269|PubMed:7559340, ECO:0000269|PubMed:8170390, ECO:0000269|PubMed:8226648, ECO:0000269|Ref.9}. UDP-N-acetylmannosaminuronate (UDP-ManNAcUA) is one of the building blocks for the cell surface polysaccharide enterobacterial common antigen (ECA). UDP-N-acetylglucosamine 2-epimerase catalyzes the first step in UDP-ManNAcUA biosynthesis, the reversible epimerization at the C-2 position between UDP-N-acetylglucosamine (UDP-GlcNAc) and UDP-N-acetylmannosamine (UDP-ManNAc) . Enzymatic activity requires the presence of UDP-GlcNAc as an activator . UDP-ManNAc synthesized by WecB is proposed to be the precursor for biosynthesis of a novel surface glycan that is required for bacteriophage N4 infection . Experiments with the BASEL collection of bacteriophages that infect E. coli showed that certain families of phages depend on the presence of WecB for infectivity . The reaction mechanism in the UDP-GlcNAc to UDP-ManNAc direction involves the anti-elimination of UDP from UDP-GlcNAc, generating the intermediate 2-acetamidoglucal, and followed by a syn-addition of UDP...

## Biological Role

Catalyzes UDP-N-acetyl-D-glucosamine 2-epimerase (reaction.R00414), UDP-N-acetyl-D-glucosamine 2-epimerase (reaction.R00420). Component of UDP-N-acetylglucosamine 2-epimerase (complex.ecocyc.CPLX0-8008).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible epimerization at C-2 of UDP-N-acetylglucosamine (UDP-GlcNAc) and thereby provides bacteria with UDP-N-acetylmannosamine (UDP-ManNAc), the activated donor of ManNAc residues. Also involved in bacteriophage N4 adsorption. {ECO:0000269|PubMed:15210128, ECO:0000269|PubMed:7559340, ECO:0000269|PubMed:8170390, ECO:0000269|PubMed:8226648, ECO:0000269|Ref.9}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00414|reaction.R00414]] `KEGG` `database` - via EC:5.1.3.14
- `catalyzes` --> [[reaction.R00420|reaction.R00420]] `KEGG` `database` - via EC:5.1.3.14
- `is_component_of` --> [[complex.ecocyc.CPLX0-8008|complex.ecocyc.CPLX0-8008]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3786|gene.b3786]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27828`
- `KEGG:ecj:JW5600;eco:b3786;`
- `GeneID:944789;`
- `GO:GO:0000271; GO:0005829; GO:0008761; GO:0009246; GO:0042803`
- `EC:5.1.3.14`

## Notes

UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) (Bacteriophage N4 adsorption protein C) (UDP-GlcNAc-2-epimerase)
