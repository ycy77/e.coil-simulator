---
entity_id: "protein.P05042"
entity_type: "protein"
name: "fumC"
source_database: "UniProt"
source_id: "P05042"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00743, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fumC b1611 JW1603"
---

# fumC

`protein.P05042`

## Static

- Type: `protein`
- Source: `UniProt:P05042`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00743, ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the TCA cycle. FumC seems to be a backup enzyme for FumA under conditions of iron limitation and oxidative stress (PubMed:7592392). Catalyzes the stereospecific interconversion of fumarate to L-malate (PubMed:1917897, PubMed:3282546). {ECO:0000269|PubMed:1917897, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:7592392, ECO:0000305|PubMed:8496960}. Fumarase C (FumC) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumC is a tetrameric protein and belongs to the class II, iron-independent fumarases . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity . In contrast, FumC is an iron-independent enzyme and is insensitive to oxidative damage . FumC is made by the cells primarily as a backup enzyme if the FumA or FumB enzymes are damaged by reactive oxygen species. Crystal structures of fumarase C have been solved, allowing identification of the active site . What was thought to be an activator binding site was later determined to be part of the active site, providing a path for transfer of substrate and product between the active site and the bulk solvent...

## Biological Role

Component of fumarase C (complex.ecocyc.FUMARASE-C).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the TCA cycle. FumC seems to be a backup enzyme for FumA under conditions of iron limitation and oxidative stress (PubMed:7592392). Catalyzes the stereospecific interconversion of fumarate to L-malate (PubMed:1917897, PubMed:3282546). {ECO:0000269|PubMed:1917897, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:7592392, ECO:0000305|PubMed:8496960}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FUMARASE-C|complex.ecocyc.FUMARASE-C]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1611|gene.b1611]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05042`
- `KEGG:ecj:JW1603;eco:b1611;ecoc:C3026_09270;`
- `GeneID:946147;`
- `GO:GO:0004333; GO:0005737; GO:0006099; GO:0006106; GO:0006108; GO:0006979; GO:0042802`
- `EC:4.2.1.2`

## Notes

Fumarate hydratase class II (Fumarase C) (EC 4.2.1.2) (Aerobic fumarase) (Iron-independent fumarase)
