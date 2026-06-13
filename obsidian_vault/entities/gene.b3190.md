---
entity_id: "gene.b3190"
entity_type: "gene"
name: "ibaG"
source_database: "NCBI RefSeq"
source_id: "gene-b3190"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3190"
  - "ibaG"
---

# ibaG

`gene.b3190`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3190`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ibaG (gene.b3190) is a gene entity. It encodes ibaG (protein.P0A9W6). Encoded protein function: FUNCTION: Involved in cell resistance against acid stress. {ECO:0000269|PubMed:22534295}. EcoCyc product frame: G7657-MONOMER. EcoCyc synonyms: yrbA. Genomic coordinates: 3336549-3336803. EcoCyc protein note: When IbaG is co-expressed with Grx4, it can form a [2Fe-2S] cluster-bridged Grx4-IbaG heterodimer, within which it destabilizes the interaction of Grx4 with the iron-sulfur cluster. Within the Grx4-IbaG complex, His63 of IbaG is involved in coordinating the [2Fe-2S] cluster. In the absence of Grx4, IbaG appears to be unable to bind an Fe-S cluster. Heterodimerization with Grx4 is independent of the [2Fe-2S] cluster . IbaG may play a role in the assembly or stability of NADH-DHI-CPLX . Expression of ibaG is increased by acid stress. An ibaG deletion mutant is slightly more sensitive to acid stress than wild type . IbaG: "influenced by acid gene"

## Biological Role

Activated by mlrA (protein.P33358).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9W6|protein.P0A9W6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=ibaG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010481,ECOCYC:G7657,GeneID:947958`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3336549-3336803:-; feature_type=gene
