---
entity_id: "gene.b2239"
entity_type: "gene"
name: "glpQ"
source_database: "NCBI RefSeq"
source_id: "gene-b2239"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2239"
  - "glpQ"
---

# glpQ

`gene.b2239`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2239`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpQ (gene.b2239) is a gene entity. It encodes glpQ (protein.P09394). Encoded protein function: FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:2829735}. EcoCyc product frame: GLYCPDIESTER-PERI-MONOMER. Genomic coordinates: 2349935-2351011. EcoCyc protein note: Glycerophosphoryl diester phosphodiesterase (GlpQ) is involved in the utilization of the glycerol moiety of phospholipids and triglycerides after their breakdown into usable forms such as glycerophosphodiesters, sn-glycerol-3-phosphate (G3P) or glycerol. GlpQ catalyzes the hydrolysis of glycerophosphodiesters into sn-glycerol 3-phosphate (glycerol-P) and an alcohol. The glycerol-P is then transported into the cell by the glycerol-P transporter, GlpT Periplasmic GlpQ is specific for the glycerophospho- moiety of the substrate, but the alcohol can be any one of several alcohols. This provides the cell with the capability of channeling a wide variety of glycerophosphodiesters into the glp-encoded dissimilatory system glpQ, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . glpQ is part of the glpTQ operon where glpT encodes the glycerol-P transporter...

## Biological Role

Repressed by glpR (protein.P0ACL0). Activated by fis (protein.P0A6R3), crp (protein.P0ACJ8), rpoN (protein.P24255).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09394|protein.P09394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=glpQ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpQ; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=glpQ; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `C` - regulator=GlpR; target=glpQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007399,ECOCYC:EG10399,GeneID:946725`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2349935-2351011:-; feature_type=gene
