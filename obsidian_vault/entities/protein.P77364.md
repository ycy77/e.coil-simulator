---
entity_id: "protein.P77364"
entity_type: "protein"
name: "glxK"
source_database: "UniProt"
source_id: "P77364"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glxK glxB5 ybbZ b0514 JW0502"
---

# glxK

`protein.P77364`

## Static

- Type: `protein`
- Source: `UniProt:P77364`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glycerate 3-kinase (EC 2.7.1.31) (D-Glycerate-3-kinase) (Glycerate kinase 2) (GK2) Glycerate kinase II (GKII), encoded by glxK, catalyzes the phosphorylation of D-glycerate. The product of the reaction (with the enzyme from E. coli Crooke's strain) was initially identified as 3-phosphoglycerate . More recent biochemical and in vivo metabolic assays showed that the product is in fact 2-phosphoglycerate . There are two glycerate kinases, known as GKI and GKII, in E. coli. GKII is less thermostable and has a narrower pH optimum than GKI . Glycerate kinase II is induced by growth on glycolate as the carbon source . A glxK mutant is unable to utilize glyoxylate . In contrast, state that deletion of glxK does not result in a growth defect with glycolate, glyoxylate or glycerate as sole carbon sources, although the data are not shown. GlxK was shown to allosterically activate CPLX-64, an enzyme that otherwise has low affinity for its substrate, in the presence of GLYOX. Activation by GlxK leads to increased affinity for allantoin . Glyoxylate is a product of allanotin degradation (see PWY-5705), and is converted to 2-PG in a pathway that involves GlxK (see GLYCOLATEMET-PWY).

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

Glycerate 3-kinase (EC 2.7.1.31) (D-Glycerate-3-kinase) (Glycerate kinase 2) (GK2)

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

- `encodes` <-- [[gene.b0514|gene.b0514]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77364`
- `KEGG:ecj:JW0502;eco:b0514;ecoc:C3026_02520;`
- `GeneID:945129;`
- `GO:GO:0005524; GO:0008887; GO:0009436; GO:0031388; GO:0043798; GO:0046296`
- `EC:2.7.1.31`

## Notes

Glycerate 3-kinase (EC 2.7.1.31) (D-Glycerate-3-kinase) (Glycerate kinase 2) (GK2)
