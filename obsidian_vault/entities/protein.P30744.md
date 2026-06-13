---
entity_id: "protein.P30744"
entity_type: "protein"
name: "sdaB"
source_database: "UniProt"
source_id: "P30744"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdaB b2797 JW2768"
---

# sdaB

`protein.P30744`

## Static

- Type: `protein`
- Source: `UniProt:P30744`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Also deaminates threonine, particularly when it is present in high concentration. L-serine deaminase II (SdaB) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. SdaB catalyzes the conversion of L-serine into pyruvate and ammonia . Much like its companion enzyme LSERINEDEAM1-MONOMER, purified SdaB requires activation in vitro with iron and dithiothrietol, suggesting that it, too, has a catalytically important iron-sulfur cluster . Like fellow serine deaminase gene G7624, sdaB is transcribed under glucose-limited conditions in complex medium .

## Biological Role

Catalyzes L-serine ammonia-lyase (reaction.R00220), L-serine hydro-lyase (reaction.R00590), 4.3.1.17-RXN (reaction.ecocyc.4.3.1.17-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Also deaminates threonine, particularly when it is present in high concentration.

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
- `catalyzes` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2797|gene.b2797]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30744`
- `KEGG:ecj:JW2768;eco:b2797;ecoc:C3026_15380;`
- `GeneID:947262;`
- `GO:GO:0003941; GO:0006094; GO:0006565; GO:0046872; GO:0051539`
- `EC:4.3.1.17`

## Notes

L-serine dehydratase 2 (SDH 2) (EC 4.3.1.17) (L-serine deaminase 2) (L-SD2)
