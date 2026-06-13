---
entity_id: "protein.P42630"
entity_type: "protein"
name: "tdcG"
source_database: "UniProt"
source_id: "P42630"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcG yhaP yhaQ b4471 JW5520"
---

# tdcG

`protein.P42630`

## Static

- Type: `protein`
- Source: `UniProt:P42630`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

L-serine dehydratase TdcG (SDH) (EC 4.3.1.17) (L-serine deaminase)

## Biological Role

Catalyzes L-serine ammonia-lyase (reaction.R00220), L-serine hydro-lyase (reaction.R00590). Component of L-serine deaminase III (complex.ecocyc.CPLX0-7622).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

L-serine dehydratase TdcG (SDH) (EC 4.3.1.17) (L-serine deaminase)

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00220|reaction.R00220]] `KEGG` `database` - via EC:4.3.1.17
- `catalyzes` --> [[reaction.R00590|reaction.R00590]] `KEGG` `database` - via EC:4.3.1.17
- `is_component_of` --> [[complex.ecocyc.CPLX0-7622|complex.ecocyc.CPLX0-7622]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4471|gene.b4471]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42630`
- `KEGG:ecj:JW5520;eco:b4471;ecoc:C3026_16975;`
- `GeneID:2847724;`
- `GO:GO:0003941; GO:0006094; GO:0009063; GO:0046872; GO:0051539; GO:0070689`
- `EC:4.3.1.17`

## Notes

L-serine dehydratase TdcG (SDH) (EC 4.3.1.17) (L-serine deaminase)
