---
entity_id: "protein.P23524"
entity_type: "protein"
name: "garK"
source_database: "UniProt"
source_id: "P23524"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "garK yhaD b3124 JW3093"
---

# garK

`protein.P23524`

## Static

- Type: `protein`
- Source: `UniProt:P23524`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of the phosphate group from adenosine triphosphate (ATP) to (R)-glycerate to form (2R)-2-phosphoglycerate, an enzymatic step in (L)-glucarate/galactarate catabolic pathway. {ECO:0000269|PubMed:9772162}. Glycerate kinase I (GKI), encoded by garK, catalyzes the formation of 2-phosphoglycerate from D-glycerate . Recent in vivo metabolic assays also showed that the product is 2-phosphoglycerate . There are two glycerate kinases, known as GKI and GKII, in E. coli. GKI is more thermostable and has a broader pH optimum than GKII, and GKII activity is only induced by growth on glycolate . Glycerate kinase I is induced by growth on glycolate, glucarate, glycerate, and galactarate as the carbon source and is not sensitive to catabolite repression .

## Biological Role

Catalyzes GKI-RXN (reaction.ecocyc.GKI-RXN).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of the phosphate group from adenosine triphosphate (ATP) to (R)-glycerate to form (2R)-2-phosphoglycerate, an enzymatic step in (L)-glucarate/galactarate catabolic pathway. {ECO:0000269|PubMed:9772162}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GKI-RXN|reaction.ecocyc.GKI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3124|gene.b3124]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23524`
- `KEGG:ecj:JW3093;eco:b3124;ecoc:C3026_17030;`
- `GeneID:947632;`
- `GO:GO:0005524; GO:0008887; GO:0031388; GO:0042838; GO:0043798; GO:0046392`
- `EC:2.7.1.165`

## Notes

Glycerate 2-kinase (EC 2.7.1.165) (Glycerate kinase 1) (GK1)
