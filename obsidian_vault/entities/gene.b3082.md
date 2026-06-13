---
entity_id: "gene.b3082"
entity_type: "gene"
name: "higA"
source_database: "NCBI RefSeq"
source_id: "gene-b3082"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3082"
  - "higA"
---

# higA

`gene.b3082`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3082`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

higA (gene.b3082) is a gene entity. It encodes higA (protein.P67701). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents HigB-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19943910}. EcoCyc product frame: G7601-MONOMER. EcoCyc synonyms: ygjM. Genomic coordinates: 3233728-3234144.

## Biological Role

Repressed by higA (protein.P67701). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P67701|protein.P67701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=higA; function=+
- `represses` <-- [[protein.P67701|protein.P67701]] `RegulonDB` `S` - regulator=HigA; target=higA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010126,ECOCYC:G7601,GeneID:947593`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3233728-3234144:-; feature_type=gene
