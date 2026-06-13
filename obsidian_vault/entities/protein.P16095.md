---
entity_id: "protein.P16095"
entity_type: "protein"
name: "sdaA"
source_database: "UniProt"
source_id: "P16095"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sdaA b1814 JW1803"
---

# sdaA

`protein.P16095`

## Static

- Type: `protein`
- Source: `UniProt:P16095`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Also deaminates threonine, particularly when it is present in high concentration. L-serine deaminase I (SdaA) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. SdaA catalyzes the conversion of L-serine into pyruvate and ammonia . SdaA contains a catalytically critical 4Fe-4S cluster that interacts directly with the L-serine substrate . This cluster is only present when the enzyme is synthesized under anaerobic conditions . Oxidatively inactivated serine deaminase can be activated in vitro with a combination of iron sulfate and dithiothreitol . Activation in vivo, presumably involving construction of the 4Fe-4S cluster, appears to require multiple additional gene products .

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
- `encodes` <-- [[gene.b1814|gene.b1814]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16095`
- `KEGG:ecj:JW1803;eco:b1814;ecoc:C3026_10330;`
- `GeneID:93776063;946331;`
- `GO:GO:0003941; GO:0005829; GO:0006094; GO:0006565; GO:0046872; GO:0051539`
- `EC:4.3.1.17`

## Notes

L-serine dehydratase 1 (SDH 1) (EC 4.3.1.17) (L-serine deaminase 1) (L-SD1)
