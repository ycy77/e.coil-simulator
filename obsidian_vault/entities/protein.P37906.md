---
entity_id: "protein.P37906"
entity_type: "protein"
name: "puuB"
source_database: "UniProt"
source_id: "P37906"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuB ordL ycjA b1301 JW1294"
---

# puuB

`protein.P37906`

## Static

- Type: `protein`
- Source: `UniProt:P37906`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the breakdown of putrescine via the oxidation of L-glutamylputrescine. {ECO:0000269|PubMed:15590624}. PuuB is probably the γ-glutamylputrescine oxidase in a putrescine utilization pathway; together with PuuC, γ-glutamyl-γ-aminobutyrate is produced from γ-glutamylputrescine . The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . Loss of PuuB in a strain without PatA prevents putrescine utilization . The puuC, puuB, and puuE genes may form an operon .

## Biological Role

Catalyzes RXN0-3921 (reaction.ecocyc.RXN0-3921).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the breakdown of putrescine via the oxidation of L-glutamylputrescine. {ECO:0000269|PubMed:15590624}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3921|reaction.ecocyc.RXN0-3921]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1301|gene.b1301]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37906`
- `KEGG:ecj:JW1294;eco:b1301;ecoc:C3026_07635;`
- `GeneID:75203416;945072;`
- `GO:GO:0005737; GO:0009447; GO:0016491`
- `EC:1.4.3.-`

## Notes

Gamma-glutamylputrescine oxidoreductase (Gamma-Glu-Put oxidase) (Gamma-glutamylputrescine oxidase) (EC 1.4.3.-)
