---
entity_id: "protein.P11553"
entity_type: "protein"
name: "fucK"
source_database: "UniProt"
source_id: "P11553"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucK b2803 JW2774"
---

# fucK

`protein.P11553`

## Static

- Type: `protein`
- Source: `UniProt:P11553`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of L-fuculose. Can also phosphorylate, with lower efficiency, D-ribulose, D-xylulose and D-fructose. {ECO:0000255|HAMAP-Rule:MF_00986, ECO:0000269|PubMed:13905785}. FucK can function as both an L-fuculokinase and a D-ribulokinase, the second enzyme of the L-fucose and D-arabinose degradation pathways, respectively. However, production of FucK is only induced by L-fucose . An fucK deletion mutant colonizes the mouse intestine as well as wild type, but is defective in maintenance of the population .

## Biological Role

Catalyzes DARABKIN-RXN (reaction.ecocyc.DARABKIN-RXN), FUCULOKIN-RXN (reaction.ecocyc.FUCULOKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of L-fuculose. Can also phosphorylate, with lower efficiency, D-ribulose, D-xylulose and D-fructose. {ECO:0000255|HAMAP-Rule:MF_00986, ECO:0000269|PubMed:13905785}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DARABKIN-RXN|reaction.ecocyc.DARABKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FUCULOKIN-RXN|reaction.ecocyc.FUCULOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2803|gene.b2803]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11553`
- `KEGG:ecj:JW2774;eco:b2803;ecoc:C3026_15410;`
- `GeneID:75172887;946022;`
- `GO:GO:0005524; GO:0005829; GO:0008737; GO:0019301; GO:0019571; GO:0042355`
- `EC:2.7.1.51`

## Notes

L-fuculokinase (EC 2.7.1.51) (L-fuculose kinase)
