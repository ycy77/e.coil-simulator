---
entity_id: "gene.b3393"
entity_type: "gene"
name: "hofO"
source_database: "NCBI RefSeq"
source_id: "gene-b3393"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3393"
  - "hofO"
---

# hofO

`gene.b3393`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3393`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofO (gene.b3393) is a gene entity. It encodes hofO (protein.P45751). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient. {ECO:0000269|PubMed:16707682}. EcoCyc product frame: G7737-MONOMER. EcoCyc synonyms: yrfB. Genomic coordinates: 3521009-3521449. EcoCyc protein note: The yrfB gene product is required for utilization of DNA as the sole source of carbon and energy; yrfB is homologous to genes involved in natural competence and genetic transformation in other bacteria . YrfB is predicted to be located in the inner membrane and to be a bitopic inner membrane protein . A yrfB null mutant has a normal growth phenotype in complex media, but has a stationary phase competition-defective (SPCD) phenotype in co-culture with the wild-type strain. A yrfB null mutant can not utilize DNA as the sole source of carbon and energy . yrfB is poorly expressed .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45751|protein.P45751]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hofO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011075,ECOCYC:G7737,GeneID:947899`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3521009-3521449:-; feature_type=gene
