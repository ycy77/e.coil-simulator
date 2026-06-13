---
entity_id: "gene.b0647"
entity_type: "gene"
name: "ybeT"
source_database: "NCBI RefSeq"
source_id: "gene-b0647"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0647"
  - "ybeT"
---

# ybeT

`gene.b0647`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0647`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybeT (gene.b0647) is a gene entity. It encodes ybeT (protein.P77296). Encoded protein function: Sel1-repeat-containing protein YbeT EcoCyc product frame: G6354-MONOMER. Genomic coordinates: 678852-679406. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 17, 2017.

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77296|protein.P77296]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ybeT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002213,ECOCYC:G6354,GeneID:945243`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:678852-679406:-; feature_type=gene
