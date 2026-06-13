---
entity_id: "gene.b3392"
entity_type: "gene"
name: "hofP"
source_database: "NCBI RefSeq"
source_id: "gene-b3392"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3392"
  - "hofP"
---

# hofP

`gene.b3392`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3392`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofP (gene.b3392) is a gene entity. It encodes hofP (protein.P45750). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient. {ECO:0000269|PubMed:16707682}. EcoCyc product frame: G7736-MONOMER. EcoCyc synonyms: yrfA. Genomic coordinates: 3520615-3521019. EcoCyc protein note: The yrfA gene product is required for utilization of DNA as the sole source of carbon and energy; yrfA is homologous to genes involved in natural competence and genetic transformation in other bacteria . YrfA is predicted to be located in the inner membrane . A yrfA null mutant has a normal growth phenotype in complex media, but has a stationary phase competition-defective (SPCD) phenotype in co-culture with the wild-type strain. A yrfA null mutant can not utilize DNA as the sole source of carbon and energy . yrfA is poorly expressed .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45750|protein.P45750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011073,ECOCYC:G7736,GeneID:947900`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3520615-3521019:-; feature_type=gene
