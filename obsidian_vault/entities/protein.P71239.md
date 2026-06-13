---
entity_id: "protein.P71239"
entity_type: "protein"
name: "wcaE"
source_database: "UniProt"
source_id: "P71239"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wcaE b2055 JW2040"
---

# wcaE

`protein.P71239`

## Static

- Type: `protein`
- Source: `UniProt:P71239`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative colanic acid biosynthesis glycosyl transferase WcaE wcaE is located within a cluster of genes that are responsible for production of CPD-21504 "colanic acid" (CA); wcaE was predicted to encode a glycosyltransferase involved in CA biosynthesis . WcaE was later shown to be a fucosyltransferase that catalyzes transfer of a fucosyl residue to the UPP-linked acetylated disaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" . The Keio collection wcaE mutant is sensitive to lithium (<90% growth at 100mM Li) . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Catalyzes RXN0-7343 (reaction.ecocyc.RXN0-7343).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

Putative colanic acid biosynthesis glycosyl transferase WcaE

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7343|reaction.ecocyc.RXN0-7343]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2055|gene.b2055]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P71239`
- `KEGG:ecj:JW2040;eco:b2055;ecoc:C3026_11565;`
- `GeneID:946543;`
- `GO:GO:0008417; GO:0009103; GO:0009242; GO:0045228`

## Notes

Putative colanic acid biosynthesis glycosyl transferase WcaE
