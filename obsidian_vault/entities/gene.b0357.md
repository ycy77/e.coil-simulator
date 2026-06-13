---
entity_id: "gene.b0357"
entity_type: "gene"
name: "frmR"
source_database: "NCBI RefSeq"
source_id: "gene-b0357"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0357"
  - "frmR"
---

# frmR

`gene.b0357`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0357`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frmR (gene.b0357) is a gene entity. It encodes frmR (protein.P0AAP3). Encoded protein function: FUNCTION: Formaldehyde sensor (PubMed:27934966). In the absence of formaldehyde, mediates repression of the frmRAB operon (PubMed:15466022, PubMed:27934966). Acts by binding directly to the frmRAB promoter region (PubMed:27934966). In the presence of formaldehyde, it dissociates from the frmRAB promoter region and allows expression of the formaldehyde detoxification system encoded by frmA and frmB (PubMed:27934966). It senses the toxic chemical formaldehyde directly, with no metal-dependence (PubMed:27934966). {ECO:0000269|PubMed:15466022, ECO:0000269|PubMed:27934966}. EcoCyc product frame: G6209-MONOMER. EcoCyc synonyms: yaiN. Genomic coordinates: 379606-379881.

## Biological Role

Repressed by frmR (protein.P0AAP3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAP3|protein.P0AAP3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AAP3|protein.P0AAP3]] `RegulonDB` `S` - regulator=FrmR; target=frmR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001226,ECOCYC:G6209,GeneID:944986`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:379606-379881:-; feature_type=gene
