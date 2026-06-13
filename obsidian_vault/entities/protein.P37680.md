---
entity_id: "protein.P37680"
entity_type: "protein"
name: "sgbE"
source_database: "UniProt"
source_id: "P37680"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgbE yiaS b3583 JW3555"
---

# sgbE

`protein.P37680`

## Static

- Type: `protein`
- Source: `UniProt:P37680`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:10913097, ECO:0000269|PubMed:11741871}. The sgbE gene encodes a second L-ribulose-5-phosphate 4-epimerase that functions in metabolism of L-lyxose and L-xylulose . The operon encoding SgbE is not required for fermentation of L-ascorbate . Review:

## Biological Role

Catalyzes L-ribulose-5-phosphate 4-epimerase (reaction.R05850), RIBULPEPIM-RXN (reaction.ecocyc.RIBULPEPIM-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:10913097, ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05850|reaction.R05850]] `KEGG` `database` - via EC:5.1.3.4
- `catalyzes` --> [[reaction.ecocyc.RIBULPEPIM-RXN|reaction.ecocyc.RIBULPEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3583|gene.b3583]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37680`
- `KEGG:ecj:JW3555;eco:b3583;ecoc:C3026_19425;`
- `GeneID:948099;`
- `GO:GO:0005829; GO:0008270; GO:0008742; GO:0016832; GO:0019323; GO:0019324; GO:0019572`
- `EC:5.1.3.4`

## Notes

L-ribulose-5-phosphate 4-epimerase SgbE (EC 5.1.3.4) (Phosphoribulose isomerase)
