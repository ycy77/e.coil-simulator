---
entity_id: "gene.b2779"
entity_type: "gene"
name: "eno"
source_database: "NCBI RefSeq"
source_id: "gene-b2779"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2779"
  - "eno"
---

# eno

`gene.b2779`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2779`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eno (gene.b2779) is a gene entity. It encodes eno (protein.P0A6P9). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of 2-phosphoglycerate (2-PG) into phosphoenolpyruvate (PEP) (PubMed:2513001, PubMed:4942326). It is essential for the degradation of carbohydrates via glycolysis. {ECO:0000255|HAMAP-Rule:MF_00318, ECO:0000269|PubMed:2513001, ECO:0000269|PubMed:4942326}.; FUNCTION: Part of the RNA degradosome, a multi-enzyme complex involved in RNA processing and messenger RNA degradation (PubMed:8610017, PubMed:9732274). Its interaction with RNase E is important for the turnover of mRNA, in particular on transcripts encoding enzymes of energy-generating metabolic routes (PubMed:14981237). Its presence in the degradosome is required for the response to excess phosphosugar (PubMed:15522087). May play a regulatory role in the degradation of specific RNAs, such as ptsG mRNA, therefore linking cellular metabolic status with post-translational gene regulation (PubMed:15522087). {ECO:0000269|PubMed:14981237, ECO:0000269|PubMed:15522087, ECO:0000269|PubMed:17242352, ECO:0000269|PubMed:18337249, ECO:0000269|PubMed:8610017, ECO:0000269|PubMed:9732274}. EcoCyc product frame: ENOLASE-MONOMER. Genomic coordinates: 2906643-2907941.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6P9|protein.P0A6P9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=eno; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009110,ECOCYC:EG10258,GeneID:945032`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2906643-2907941:-; feature_type=gene
