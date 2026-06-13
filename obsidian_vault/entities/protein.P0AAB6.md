---
entity_id: "protein.P0AAB6"
entity_type: "protein"
name: "galF"
source_database: "UniProt"
source_id: "P0AAB6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galF wcaN b2042 JW2027"
---

# galF

`protein.P0AAB6`

## Static

- Type: `protein`
- Source: `UniProt:P0AAB6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (Alpha-D-glucosyl-1-phosphate uridylyltransferase) (UDP-glucose pyrophosphorylase) (UDPGP) (Uridine diphosphoglucose pyrophosphorylase) GalF is a protein with 58% sequence identity to GLUC1PURIDYLTRANS-MONOMER GalU. The potential biochemical activity and in vivo role of GalF has long been unclear. Recent biochemical and mutagenesis data showed that GalF has vestigial UTP:glucose-1-phosphate uridylyltransferase activity, with a specific activity 10000-fold lower than GalU. Mutagenesis of predicted active site residues towards the GalU sequence increases activity, and overexpression of GalF allows delayed growth on galactose as the source of carbon in a galU mutant . GalF was initially suggested to be a subunit of a GalU/GalF protein complex involved in COLANSYN-PWY. In the uropathogenic E. coli strain VW187 (O7:K1), GalF has been shown to interact physically with GalU, as well as enhancing its thermal stability and increasing its enzymatic activity . Based on these results, it was thought to be part of a GalU/GalF complex in that strain, and was predicted to be involved in a similar complex in E. coli K-12. GalF overproduction leads to increased levels of capsular polysaccharide production in E. coli B44 (O9:K30) . Overexpression of GalF enables increased production of hyaluronic acid in an engineered E. coli strain...

## Biological Role

Catalyzes UTP:alpha-D-glucose-1-phosphate uridylyltransferase (reaction.R00289).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (Alpha-D-glucosyl-1-phosphate uridylyltransferase) (UDP-glucose pyrophosphorylase) (UDPGP) (Uridine diphosphoglucose pyrophosphorylase)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R00289|reaction.R00289]] `KEGG` `database` - via EC:2.7.7.9

## Incoming Edges (1)

- `encodes` <-- [[gene.b2042|gene.b2042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAB6`
- `KEGG:ecj:JW2027;eco:b2042;ecoc:C3026_11500;`
- `GeneID:86946998;946560;`
- `GO:GO:0003983; GO:0005829; GO:0006011; GO:0009244; GO:0030234`
- `EC:2.7.7.9`

## Notes

UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (Alpha-D-glucosyl-1-phosphate uridylyltransferase) (UDP-glucose pyrophosphorylase) (UDPGP) (Uridine diphosphoglucose pyrophosphorylase)
