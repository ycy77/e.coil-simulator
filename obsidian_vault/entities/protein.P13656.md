---
entity_id: "protein.P13656"
entity_type: "protein"
name: "chiA"
source_database: "UniProt"
source_id: "P13656"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10760150}. Note=Secreted via the Gsp type II secretion machinery under conditions of derepressed gsp gene expression."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chiA yheB b3338 JW3300"
---

# chiA

`protein.P13656`

## Static

- Type: `protein`
- Source: `UniProt:P13656`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:10760150}. Note=Secreted via the Gsp type II secretion machinery under conditions of derepressed gsp gene expression.

## Enriched Summary

FUNCTION: Bifunctional enzyme with lysozyme/chitinase activity. {ECO:0000269|PubMed:10760150}. ChiA is a large soluble protein with five predicted chitin-binding domains and a C-terminal catalytic domain that is similar to the family 18 glycohydrolases . The purified N-terminal chitin-binding domain binds to chitin with high affinity, but binds only poorly to cellulose . Purified ChiA exhibits endochitinase activity, releasing diacetyl-chitobiose and triacetyl-chitotriose from colloidal chitin . Under standard growth conditions, chiA expression is low and is negatively controlled by H-NS . In mutants lacking H-NS, expression of the gsp locus is derepressed, and a type II secretion machinery can be produced. This allows secretion of ChiA into the culture medium . Expression of chiA is activated by BglJ-RcsB, which may function as an H-NS antagonist . Artificially induced expression of chiA enables growth on pentaacetyl-chitopentaose . ChiA: "chitinase" Review:

## Biological Role

Catalyzes [1,4-(N-acetyl-beta-D-glucosaminyl)]n glycanohydrolase (reaction.R02334), 3.2.1.14-RXN (reaction.ecocyc.3.2.1.14-RXN).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Bifunctional enzyme with lysozyme/chitinase activity. {ECO:0000269|PubMed:10760150}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02334|reaction.R02334]] `KEGG` `database` - via EC:3.2.1.14
- `catalyzes` --> [[reaction.ecocyc.3.2.1.14-RXN|reaction.ecocyc.3.2.1.14-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3338|gene.b3338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13656`
- `KEGG:ecj:JW3300;eco:b3338;`
- `GeneID:947837;`
- `GO:GO:0000272; GO:0003796; GO:0005576; GO:0006032; GO:0008061; GO:0008843; GO:0030246; GO:0030288`
- `EC:3.2.1.14; 3.2.1.17`

## Notes

Probable bifunctional chitinase/lysozyme [Includes: Chitinase (EC 3.2.1.14); Lysozyme (EC 3.2.1.17)]
