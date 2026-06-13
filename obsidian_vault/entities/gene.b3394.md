---
entity_id: "gene.b3394"
entity_type: "gene"
name: "hofN"
source_database: "NCBI RefSeq"
source_id: "gene-b3394"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3394"
  - "hofN"
---

# hofN

`gene.b3394`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3394`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofN (gene.b3394) is a gene entity. It encodes hofN (protein.P64634). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient. {ECO:0000269|PubMed:16707682}. EcoCyc product frame: G7738-MONOMER. EcoCyc synonyms: yrfC. Genomic coordinates: 3521433-3521972. EcoCyc protein note: The yrfC gene product is required for utilization of DNA as the sole source of carbon and energy; yrfC is homologous to genes involved in natural competence and genetic transformation in other bacteria . YrfC is predicted to be located in the inner membrane . YrfC is predicted to be a bitopic inner membrane protein . A yrfC null mutant has a normal growth phenotype in complex media, but has a stationary phase competition-defective (SPCD) phenotype in co-culture with the wild-type strain. A yrfC null mutant can not utilize DNA as the sole source of carbon and energy . yrfC is poorly expressed .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64634|protein.P64634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011077,ECOCYC:G7738,GeneID:947898`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3521433-3521972:-; feature_type=gene
