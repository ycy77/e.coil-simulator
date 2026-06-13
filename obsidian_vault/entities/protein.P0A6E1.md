---
entity_id: "protein.P0A6E1"
entity_type: "protein"
name: "aroL"
source_database: "UniProt"
source_id: "P0A6E1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroL b0388 JW0379"
---

# aroL

`protein.P0A6E1`

## Static

- Type: `protein`
- Source: `UniProt:P0A6E1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:3001029, ECO:0000269|PubMed:3026317}. Shikimate kinase is involved in the fifth step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. Shikimate kinase catalyzes the formation of shikimate 3-phosphate from shikimate and ATP. There are two shikimate kinase enzymes, I (AroK) and II (AroL). The isoenzymes are separable and presumably monofunctional . The amino acid sequences of shikimate kinase I and II shows 30% homology over the entire length of both proteins . Shikimate kinase I is encoded by aroK and shikimate kinase II is encoded by aroL. The expression of aroK unlike that of aroL, which is controlled by the TyrR and TrpR repressors, appears to be constitutive . Expression of aroL is regulated by the tyrR gene product protein with tyrosine or tryptophan as a co-repressor . Shikimate kinase I has a much lower affinity (approximately 100-fold) for shikimate than shikimate kinase II. Shikimate II seems to be the dominant enzyme of the pathway with shikimate I playing a secondary role. The enzyme activity is dependent on the presence of a divalent cation as a cofactor...

## Biological Role

Catalyzes SHIKIMATE-KINASE-RXN (reaction.ecocyc.SHIKIMATE-KINASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:3001029, ECO:0000269|PubMed:3026317}.

## Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SHIKIMATE-KINASE-RXN|reaction.ecocyc.SHIKIMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0388|gene.b0388]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6E1`
- `KEGG:ecj:JW0379;eco:b0388;ecoc:C3026_01880;`
- `GeneID:93777073;945031;`
- `GO:GO:0000287; GO:0004765; GO:0005524; GO:0005829; GO:0008652; GO:0009073; GO:0009423; GO:0046872`
- `EC:2.7.1.71`

## Notes

Shikimate kinase 2 (SK 2) (EC 2.7.1.71) (Shikimate kinase II) (SKII)
