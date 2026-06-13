---
entity_id: "protein.P75919"
entity_type: "protein"
name: "clsC"
source_database: "UniProt"
source_id: "P75919"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clsC ymdC b1046 JW5150"
---

# clsC

`protein.P75919`

## Static

- Type: `protein`
- Source: `UniProt:P75919`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) from phosphatidylglycerol (PG) and phosphatidylethanolamine (PE). {ECO:0000269|PubMed:22988102}. ClsC is a third cardiolipin synthase in E. coli. Synthesis of cardiolipin during exponential growth is due to the activity of CARDIOLIPSYN-MONOMER ClsA, while all three cardiolipin synthases, ClsA, G6406-MONOMER ClsB and ClsC, contribute to cardiolipin synthesis in stationary phase . Full complementation of a clsC mutant requires co-expression with G6550, the gene directly upstream of clsC. However, more recent studies using plasmids with various lengths of nucleotides upstream of the currently annotated TTG start site found that the ATG +9 nucleotides upstream is most likely the true start site for transcription of clsC; the ymdB gene was not required. Additionally, using a thin layer chromatography-based assay with P32 found the ClsC (+9 bp ATG) produced the P32-labelled cardiolipin, and ymdB was not required for phosphatidylethanolamine substrate specificity . Cells with deletions of all three of the genes encoding cardiolipin synthases, ΔclsABC, completely lack cardiolipin . Upon overexpression of AtpF (as well as other membrane proteins), formation of intracellular membranes (ICMs) is observed; the inverted hexagonal phase of ICMs is absent in a ΔclsABC mutant, and thus requires cardiolipin...

## Biological Role

Catalyzes RXN0-7012 (reaction.ecocyc.RXN0-7012).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) from phosphatidylglycerol (PG) and phosphatidylethanolamine (PE). {ECO:0000269|PubMed:22988102}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7012|reaction.ecocyc.RXN0-7012]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1046|gene.b1046]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75919`
- `KEGG:ecj:JW5150;eco:b1046;ecoc:C3026_06365;`
- `GeneID:947321;`
- `GO:GO:0032049; GO:0050685; GO:0090483`
- `EC:2.7.8.-`

## Notes

Cardiolipin synthase C (CL synthase) (EC 2.7.8.-)
