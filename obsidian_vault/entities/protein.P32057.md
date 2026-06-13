---
entity_id: "protein.P32057"
entity_type: "protein"
name: "wcaI"
source_database: "UniProt"
source_id: "P32057"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wcaI yefD b2050 JW2035"
---

# wcaI

`protein.P32057`

## Static

- Type: `protein`
- Source: `UniProt:P32057`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative colanic acid biosynthesis glycosyl transferase WcaI WcaI is the fucosyltransferase that catalyzes the transfer of unmodified fucose to CPD-12773 UPP-Glc in the biosynthesis of the extracellular polysaccharide CPD-21504 colanic acid (CA) . wcaI is located within a cluster of genes that are responsible for production of CA; wcaI was predicted to encode a glycosyl transferase involved in the process . Expression of wcaI is higher in wild-type biofilms than in biofilms formed by an rpoS mutant . The Keio collection wcaI mutant is sensitive to lithium (<90% growth at 200mM Li) . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Catalyzes RXN0-7341 (reaction.ecocyc.RXN0-7341).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

Putative colanic acid biosynthesis glycosyl transferase WcaI

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7341|reaction.ecocyc.RXN0-7341]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2050|gene.b2050]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32057`
- `KEGG:ecj:JW2035;eco:b2050;ecoc:C3026_11540;`
- `GeneID:946588;`
- `GO:GO:0009103; GO:0009242; GO:0045228; GO:0046920`

## Notes

Putative colanic acid biosynthesis glycosyl transferase WcaI
