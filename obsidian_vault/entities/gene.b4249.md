---
entity_id: "gene.b4249"
entity_type: "gene"
name: "bdcA"
source_database: "NCBI RefSeq"
source_id: "gene-b4249"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4249"
  - "bdcA"
---

# bdcA

`gene.b4249`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4249`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bdcA (gene.b4249) is a gene entity. It encodes bdcA (protein.P39333). Encoded protein function: FUNCTION: Increases biofilm dispersal. Acts by binding directly to the signaling molecule cyclic-di-GMP, which decreases the intracellular concentration of cyclic-di-GMP and leads to biofilm dispersal. Also controls other biofilm-related phenotypes such as cell motility, cell size, cell aggregation and production of extracellular DNA and extracellular polysaccharides (EPS). Does not act as a phosphodiesterase. {ECO:0000269|PubMed:21059164}. EcoCyc product frame: G7880-MONOMER. EcoCyc synonyms: yjgI. Genomic coordinates: 4473340-4474053.

## Biological Role

Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39333|protein.P39333]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=bdcA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013909,ECOCYC:G7880,GeneID:948765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4473340-4474053:-; feature_type=gene
