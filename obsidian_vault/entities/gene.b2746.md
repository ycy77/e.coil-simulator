---
entity_id: "gene.b2746"
entity_type: "gene"
name: "ispF"
source_database: "NCBI RefSeq"
source_id: "gene-b2746"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2746"
  - "ispF"
---

# ispF

`gene.b2746`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2746`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispF (gene.b2746) is a gene entity. It encodes ispF (protein.P62617). Encoded protein function: FUNCTION: Involved in the biosynthesis of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP), two major building blocks of isoprenoid compounds. Catalyzes the conversion of 4-diphosphocytidyl-2-C-methyl-D-erythritol 2-phosphate (CDP-ME2P) to 2-C-methyl-D-erythritol 2,4-cyclodiphosphate (ME-CPP) with a corresponding release of cytidine 5-monophosphate (CMP). Also converts 4-diphosphocytidyl-2-C-methyl-D-erythritol into 2-C-methyl-D-erythritol 3,4-cyclophosphate and CMP. {ECO:0000269|PubMed:10694574, ECO:0000269|PubMed:22839733}. EcoCyc product frame: EG11816-MONOMER. EcoCyc synonyms: ygbB. Genomic coordinates: 2871301-2871780.

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62617|protein.P62617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009013,ECOCYC:EG11816,GeneID:945057`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2871301-2871780:-; feature_type=gene
