---
entity_id: "protein.P0A6V1"
entity_type: "protein"
name: "glgC"
source_database: "UniProt"
source_id: "P0A6V1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glgC b3430 JW3393"
---

# glgC

`protein.P0A6V1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6V1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of ADP-glucose, a building block required for the elongation reactions to produce glycogen. Catalyzes the reaction between ATP and alpha-D-glucose 1-phosphate (G1P) to produce pyrophosphate and ADP-Glc. {ECO:0000269|PubMed:1648099}. Glucose-1-phosphate adenylyltransferase (GlgC) catalyzes the rate-limiting first step in the biosynthesis of glycogen. The enzyme is allosterically activated by the glycolytic intermediate fructose-1,6-bisphosphate (FBP) and inhibited by AMP and pyrophosphate, thus responding to the energy state of the cell. GlgC consists of an N-terminal glycosyltransferase A-like domain and a C-terminal regulatory domain . Various mutants and truncated forms of the enzyme have been studied . Co-expression of separately encoded N- and C-terminal domain polypeptides yields an active enzyme. The two domains interact strongly . The Asp142 residue is important for catalytic activity . Homology modelling and site-directed mutagenesis allowed the identification of residues that play a role in binding of glucose-1-phosphate . The N-terminal region is required for allosteric regulation of the enzyme , while the C-terminal domain contributes to regulator selectivity . Residues Trp113 and Gln74 have been shown to be required for activation by fructose-1,6-bisphosphate...

## Biological Role

Component of glucose-1-phosphate adenylyltransferase (complex.ecocyc.GLUC1PADENYLTRANS-CPLX).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of ADP-glucose, a building block required for the elongation reactions to produce glycogen. Catalyzes the reaction between ATP and alpha-D-glucose 1-phosphate (G1P) to produce pyrophosphate and ADP-Glc. {ECO:0000269|PubMed:1648099}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLUC1PADENYLTRANS-CPLX|complex.ecocyc.GLUC1PADENYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3430|gene.b3430]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6V1`
- `KEGG:ecj:JW3393;eco:b3430;ecoc:C3026_18595;`
- `GeneID:93778559;947942;`
- `GO:GO:0000287; GO:0005524; GO:0005978; GO:0008878; GO:0009250; GO:0010170; GO:0016208; GO:0042802; GO:0051289`
- `EC:2.7.7.27`

## Notes

Glucose-1-phosphate adenylyltransferase (EC 2.7.7.27) (ADP-glucose pyrophosphorylase) (ADPGlc PPase) (ADP-glucose synthase)
