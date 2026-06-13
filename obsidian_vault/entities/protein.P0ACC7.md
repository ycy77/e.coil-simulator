---
entity_id: "protein.P0ACC7"
entity_type: "protein"
name: "glmU"
source_database: "UniProt"
source_id: "P0ACC7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01631, ECO:0000269|PubMed:10428949}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glmU yieA b3730 JW3708"
---

# glmU

`protein.P0ACC7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACC7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01631, ECO:0000269|PubMed:10428949}.

## Enriched Summary

FUNCTION: Catalyzes the last two sequential reactions in the de novo biosynthetic pathway for UDP-N-acetylglucosamine (UDP-GlcNAc). The C-terminal domain catalyzes the transfer of acetyl group from acetyl coenzyme A to glucosamine-1-phosphate (GlcN-1-P) to produce N-acetylglucosamine-1-phosphate (GlcNAc-1-P), which is converted into UDP-GlcNAc by the transfer of uridine 5-monophosphate (from uridine 5-triphosphate), a reaction catalyzed by the N-terminal domain. {ECO:0000255|HAMAP-Rule:MF_01631, ECO:0000269|PubMed:10428949, ECO:0000269|PubMed:21984832, ECO:0000269|PubMed:22297115, ECO:0000269|PubMed:8083170, ECO:0000269|PubMed:8555230}. glmU encodes a fused enzyme with two enzymatic activities that catalyze sequential steps in the biosynthesis of UDP-N-acetyl-D-glucosamine (UDP-GlcNAc), an essential precursor of cell wall peptidoglycan, lipopolysaccharide and enterobacterial common antigen . The enzymatic activities of GlmU are present in two independently folding and functional domains . The uridylyltransferase activity, which catalyzes the formation of UDP-GlcNAc, localizes to the N-terminal domain, and the acetyltransferase activity, which catalyzes the formation of N-acetylglucosamine-1-phosphate (GlcNAc-1-P), is located in the C-terminal domain. Kinetic data shows that the acetyl transfer precedes the uridylyl transfer...

## Biological Role

Catalyzes UTP:N-acetyl-alpha-D-glucosamine-1-phosphate uridylyltransferase (reaction.R00416), acetyl-CoA:D-glucosamine-1-phosphate N-acetyltransferase (reaction.R05332). Component of fused N-acetylglucosamine-1-phosphate uridyltransferase and glucosamine-1-phosphate acetyltransferase (complex.ecocyc.NAG1P-URIDYLTRANS-CPLX).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Catalyzes the last two sequential reactions in the de novo biosynthetic pathway for UDP-N-acetylglucosamine (UDP-GlcNAc). The C-terminal domain catalyzes the transfer of acetyl group from acetyl coenzyme A to glucosamine-1-phosphate (GlcN-1-P) to produce N-acetylglucosamine-1-phosphate (GlcNAc-1-P), which is converted into UDP-GlcNAc by the transfer of uridine 5-monophosphate (from uridine 5-triphosphate), a reaction catalyzed by the N-terminal domain. {ECO:0000255|HAMAP-Rule:MF_01631, ECO:0000269|PubMed:10428949, ECO:0000269|PubMed:21984832, ECO:0000269|PubMed:22297115, ECO:0000269|PubMed:8083170, ECO:0000269|PubMed:8555230}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00416|reaction.R00416]] `KEGG` `database` - via EC:2.7.7.23
- `catalyzes` --> [[reaction.R05332|reaction.R05332]] `KEGG` `database` - via EC:2.3.1.157
- `is_component_of` --> [[complex.ecocyc.NAG1P-URIDYLTRANS-CPLX|complex.ecocyc.NAG1P-URIDYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3730|gene.b3730]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACC7`
- `KEGG:ecj:JW3708;eco:b3730;ecoc:C3026_20215;`
- `GeneID:75173964;75205448;948246;`
- `GO:GO:0000287; GO:0000902; GO:0003977; GO:0005829; GO:0006048; GO:0008360; GO:0009245; GO:0009252; GO:0016020; GO:0019134; GO:0042802; GO:0071555`
- `EC:2.3.1.157; 2.7.7.23`

## Notes

Bifunctional protein GlmU [Includes: UDP-N-acetylglucosamine pyrophosphorylase (EC 2.7.7.23) (N-acetylglucosamine-1-phosphate uridyltransferase); Glucosamine-1-phosphate N-acetyltransferase (EC 2.3.1.157)]
