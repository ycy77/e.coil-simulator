---
entity_id: "gene.b3395"
entity_type: "gene"
name: "hofM"
source_database: "NCBI RefSeq"
source_id: "gene-b3395"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3395"
  - "hofM"
---

# hofM

`gene.b3395`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3395`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofM (gene.b3395) is a gene entity. It encodes hofM (protein.P45753). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient. {ECO:0000269|PubMed:16707682}. EcoCyc product frame: G7739-MONOMER. EcoCyc synonyms: yrfD. Genomic coordinates: 3521972-3522751. EcoCyc protein note: The yrfD gene product is required for utilization of DNA as the sole source of carbon and energy; yrfD is homologous to genes involved in natural competence and genetic transformation in other bacteria . YrfD is predicted to be located in the periplasm . A yrfD null mutant has a normal growth phenotype in complex media and in co-culture with the wild-type strain. A yrfD null mutant can not utilize DNA as the sole source of carbon and energy . yrfD is poorly expressed .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45753|protein.P45753]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011079,ECOCYC:G7739,GeneID:947908`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3521972-3522751:-; feature_type=gene
