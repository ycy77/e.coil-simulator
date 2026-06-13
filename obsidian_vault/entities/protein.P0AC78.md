---
entity_id: "protein.P0AC78"
entity_type: "protein"
name: "wecA"
source_database: "UniProt"
source_id: "P0AC78"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02030, ECO:0000269|PubMed:11700352, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17237164}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02030}. Note=Localizes to discrete regions in the plasma membrane. {ECO:0000269|PubMed:17237164}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wecA rfe b3784 JW3758"
---

# wecA

`protein.P0AC78`

## Static

- Type: `protein`
- Source: `UniProt:P0AC78`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02030, ECO:0000269|PubMed:11700352, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:17237164}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02030}. Note=Localizes to discrete regions in the plasma membrane. {ECO:0000269|PubMed:17237164}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of the GlcNAc-1-phosphate moiety from UDP-GlcNAc onto the carrier lipid undecaprenyl phosphate (C55-P), yielding GlcNAc-pyrophosphoryl-undecaprenyl (GlcNAc-PP-C55). It is the first lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis, and an acceptor for the addition of subsequent sugars to complete the biosynthesis of O-antigen lipopolysaccharide (LPS) in many E.coli O types. The apparent affinity of WecA for the polyisoprenyl phosphate substrates increases with the polyisoprenyl chain length. WecA is unable to utilize dolichyl phosphate (Dol-P). {ECO:0000269|PubMed:11700352, ECO:0000269|PubMed:17237164, ECO:0000269|PubMed:1730666, ECO:0000269|PubMed:9134438}.

## Biological Role

Catalyzes UDP-N-acetyl-D-glucosamine:undecaprenyl-phosphate N-acetyl-D-glucosamine phosphotransferase (reaction.R08856), UDP-N-acetyl-alpha-D-glucosamine:trans,octacis-decaprenyl-phosphate N-acetylglucosaminephosphotransferase (reaction.R12075). Component of UDP-N-acetylglucosamine—undecaprenyl-phosphate N-acetylglucosaminephosphotransferase (complex.ecocyc.CPLX0-8011).

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the GlcNAc-1-phosphate moiety from UDP-GlcNAc onto the carrier lipid undecaprenyl phosphate (C55-P), yielding GlcNAc-pyrophosphoryl-undecaprenyl (GlcNAc-PP-C55). It is the first lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis, and an acceptor for the addition of subsequent sugars to complete the biosynthesis of O-antigen lipopolysaccharide (LPS) in many E.coli O types. The apparent affinity of WecA for the polyisoprenyl phosphate substrates increases with the polyisoprenyl chain length. WecA is unable to utilize dolichyl phosphate (Dol-P). {ECO:0000269|PubMed:11700352, ECO:0000269|PubMed:17237164, ECO:0000269|PubMed:1730666, ECO:0000269|PubMed:9134438}.

## Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R08856|reaction.R08856]] `KEGG` `database` - via EC:2.7.8.33
- `catalyzes` --> [[reaction.R12075|reaction.R12075]] `KEGG` `database` - via EC:2.7.8.35
- `is_component_of` --> [[complex.ecocyc.CPLX0-8011|complex.ecocyc.CPLX0-8011]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3784|gene.b3784]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC78`
- `KEGG:ecj:JW3758;eco:b3784;ecoc:C3026_20490;`
- `GeneID:93778160;948789;`
- `GO:GO:0000287; GO:0005886; GO:0008963; GO:0009103; GO:0009243; GO:0009246; GO:0009276; GO:0016020; GO:0016757; GO:0016780; GO:0030145; GO:0036380; GO:0042802; GO:0044038; GO:0071555`
- `EC:2.7.8.33`

## Notes

Undecaprenyl-phosphate alpha-N-acetylglucosaminyl 1-phosphate transferase (EC 2.7.8.33) (UDP-GlcNAc:undecaprenyl-phosphate GlcNAc-1-phosphate transferase) (Undecaprenyl-phosphate GlcNAc-1-phosphate transferase)
