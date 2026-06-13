---
entity_id: "protein.P26612"
entity_type: "protein"
name: "amyA"
source_database: "UniProt"
source_id: "P26612"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1400215}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "amyA yedC b1927 JW1912"
---

# amyA

`protein.P26612`

## Static

- Type: `protein`
- Source: `UniProt:P26612`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1400215}.

## Enriched Summary

Cytoplasmic alpha-amylase (EC 3.2.1.1) (1,4-alpha-D-glucan glucanohydrolase) AmyA is a cytoplasmic α-amylase. Alpha-Amyloses α-Amylose, a linear α-glucan, is the most effective substrate in vitro; Starch starch and CPD-7043 amylopectin, a lightly branched α-glucan, can serve as good substrates, while the highly branched α-glucan Glycogens glycogen is a poor substrate. Linear oligomeric α-glucans of six or more glucose moieties are good substrates of AmyA . The physiological role of AmyA is uncertain. Although under experimental conditions glycogen is a poor substrate for the enzyme, it is the most likely natural substrate since it is the only polysaccharide present in appreciable amounts in the cytoplasm. It has been hypothesized that in the absence of exogenous oligosaccharides that could act as primers for glycogen synthesis, the cytoplasmic amylase might provide oligosaccharides through catabolism of existing cellular glycogen, which would then act as the source of primers for the synthesis of more molecules of glycogen . AmyA is one of two α-amylases present in E. coli. The second enzyme, ALPHA-AMYL-PERI-MONOMER "MalS", is periplasmic.

## Biological Role

Catalyzes 1,4-alpha-D-glucan glucanohydrolase (reaction.R02108), 1,4-alpha-D-glucan maltohydrolase (reaction.R02112), ALPHA-AMYL-RXN (reaction.ecocyc.ALPHA-AMYL-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Cytoplasmic alpha-amylase (EC 3.2.1.1) (1,4-alpha-D-glucan glucanohydrolase)

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02108|reaction.R02108]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` --> [[reaction.R02112|reaction.R02112]] `KEGG` `database` - via EC:3.2.1.1
- `catalyzes` --> [[reaction.ecocyc.ALPHA-AMYL-RXN|reaction.ecocyc.ALPHA-AMYL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1927|gene.b1927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26612`
- `KEGG:ecj:JW1912;eco:b1927;ecoc:C3026_10930;`
- `GeneID:946434;`
- `GO:GO:0004556; GO:0005509; GO:0005737; GO:0005975`
- `EC:3.2.1.1`

## Notes

Cytoplasmic alpha-amylase (EC 3.2.1.1) (1,4-alpha-D-glucan glucanohydrolase)
