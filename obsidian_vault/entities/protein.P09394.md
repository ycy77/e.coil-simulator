---
entity_id: "protein.P09394"
entity_type: "protein"
name: "glpQ"
source_database: "UniProt"
source_id: "P09394"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2829735}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpQ b2239 JW2233"
---

# glpQ

`protein.P09394`

## Static

- Type: `protein`
- Source: `UniProt:P09394`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2829735}.

## Enriched Summary

FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:2829735}. Glycerophosphoryl diester phosphodiesterase (GlpQ) is involved in the utilization of the glycerol moiety of phospholipids and triglycerides after their breakdown into usable forms such as glycerophosphodiesters, sn-glycerol-3-phosphate (G3P) or glycerol. GlpQ catalyzes the hydrolysis of glycerophosphodiesters into sn-glycerol 3-phosphate (glycerol-P) and an alcohol. The glycerol-P is then transported into the cell by the glycerol-P transporter, GlpT Periplasmic GlpQ is specific for the glycerophospho- moiety of the substrate, but the alcohol can be any one of several alcohols. This provides the cell with the capability of channeling a wide variety of glycerophosphodiesters into the glp-encoded dissimilatory system glpQ, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . glpQ is part of the glpTQ operon where glpT encodes the glycerol-P transporter . Regulatory elements of the glpTQ operon have been identified . Comparison of the nucleotide sequences of glpQ with ugpQ, which codes for another phosphodiesterase, showed significant similarity in primary structure...

## Biological Role

Component of glycerophosphoryl diester phosphodiesterase, periplasmic (complex.ecocyc.GLYCPDIESTER-PERI-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:2829735}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLYCPDIESTER-PERI-CPLX|complex.ecocyc.GLYCPDIESTER-PERI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2239|gene.b2239]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09394`
- `KEGG:ecj:JW2233;eco:b2239;ecoc:C3026_12510;`
- `GeneID:946725;`
- `GO:GO:0005509; GO:0006071; GO:0008889; GO:0042597; GO:0046475; GO:0046872`
- `EC:3.1.4.46`

## Notes

Glycerophosphodiester phosphodiesterase, periplasmic (Glycerophosphoryl diester phosphodiesterase, periplasmic) (EC 3.1.4.46)
