---
entity_id: "gene.b2976"
entity_type: "gene"
name: "glcB"
source_database: "NCBI RefSeq"
source_id: "gene-b2976"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2976"
  - "glcB"
---

# glcB

`gene.b2976`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2976`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glcB (gene.b2976) is a gene entity. It encodes glcB (protein.P37330). Encoded protein function: FUNCTION: Involved in the glycolate utilization. Catalyzes the condensation and subsequent hydrolysis of acetyl-coenzyme A (acetyl-CoA) and glyoxylate to form malate and CoA. {ECO:0000255|HAMAP-Rule:MF_00641, ECO:0000269|PubMed:14336062, ECO:0000269|PubMed:4892366, ECO:0000269|PubMed:7925370}. EcoCyc product frame: MALSYNG-MONOMER. EcoCyc synonyms: glc. Genomic coordinates: 3121634-3123805. EcoCyc protein note: Malate synthase catalyzes the Claisen condensation of glyoxylate and acetyl-CoA, initially forming a malyl-CoA intermediate that is hydrolyzed to the products malate and CoA. There are two isozymes of malate synthase in E. coli . Malate synthase G (the "glycolate form" of malate synthase described here) is responsible for almost all of the malate synthase activity in cells metabolizing glyoxylate that is formed during growth on glycolate . MALATE-SYNTHASE Malate synthase A is involved in the GLYOXYLATE-BYPASS "glyoxylate bypass", metabolizing glyoxylate formed in the dissimilation of acetate . Crystal and solution structures (as well as a cryo-EM structure) of malate synthase G in various conformations have been determined, and a reaction mechanism has been proposed . Active site residues were confirmed by site-directed mutagenesis...

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by glcC (protein.P0ACL5).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37330|protein.P37330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACL5|protein.P0ACL5]] `RegulonDB` `S` - regulator=GlcC; target=glcB; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=glcB; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=glcB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009767,ECOCYC:EG20080,GeneID:948857`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3121634-3123805:-; feature_type=gene
