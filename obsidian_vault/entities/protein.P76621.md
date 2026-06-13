---
entity_id: "protein.P76621"
entity_type: "protein"
name: "glaH"
source_database: "UniProt"
source_id: "P76621"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glaH csiD gab ygaT b2659 JW5427"
---

# glaH

`protein.P76621`

## Static

- Type: `protein`
- Source: `UniProt:P76621`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as an alpha-ketoglutarate-dependent dioxygenase catalyzing hydroxylation of glutarate (GA) to L-2-hydroxyglutarate (L2HG) in the stationary phase of E.coli. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. Other dicarboxylic acids (oxalate, malonate, succinate, adipate, and pimelate) are not substrates for this enzyme. {ECO:0000269|PubMed:30498244}.

## Biological Role

Component of glutarate dioxygenase GlaH (complex.ecocyc.CPLX0-8201).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Acts as an alpha-ketoglutarate-dependent dioxygenase catalyzing hydroxylation of glutarate (GA) to L-2-hydroxyglutarate (L2HG) in the stationary phase of E.coli. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. Other dicarboxylic acids (oxalate, malonate, succinate, adipate, and pimelate) are not substrates for this enzyme. {ECO:0000269|PubMed:30498244}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8201|complex.ecocyc.CPLX0-8201]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2659|gene.b2659]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76621`
- `KEGG:ecj:JW5427;eco:b2659;ecoc:C3026_14660;`
- `GeneID:948076;`
- `GO:GO:0005506; GO:0008198; GO:0019477; GO:0032991; GO:0042802; GO:0050498; GO:0090549; GO:0106343`
- `EC:1.14.11.64`

## Notes

Glutarate 2-hydroxylase (G-2-H) (EC 1.14.11.64) (Carbon starvation induced protein D)
