---
entity_id: "gene.b0865"
entity_type: "gene"
name: "ybjP"
source_database: "NCBI RefSeq"
source_id: "gene-b0865"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0865"
  - "ybjP"
---

# ybjP

`gene.b0865`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0865`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjP (gene.b0865) is a gene entity. It encodes ybjP (protein.P75818). Encoded protein function: Uncharacterized lipoprotein YbjP EcoCyc product frame: G6450-MONOMER. Genomic coordinates: 903952-904467. EcoCyc protein note: YbjP is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Deletion of ybjP is associated with significant changes in the distribution of carbon fluxes in central metabolism .

## Biological Role

Activated by rpoS (protein.P13445), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75818|protein.P75818]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ybjP; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybjP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002941,ECOCYC:G6450,GeneID:945491`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:903952-904467:-; feature_type=gene
