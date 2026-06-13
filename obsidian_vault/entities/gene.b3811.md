---
entity_id: "gene.b3811"
entity_type: "gene"
name: "xerC"
source_database: "NCBI RefSeq"
source_id: "gene-b3811"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3811"
  - "xerC"
---

# xerC

`gene.b3811`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3811`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xerC (gene.b3811) is a gene entity. It encodes xerC (protein.P0A8P6). Encoded protein function: FUNCTION: Site-specific tyrosine recombinase, which acts by catalyzing the cutting and rejoining of the recombining DNA molecules. Binds cooperatively to specific DNA consensus sequences that are separated from XerD binding sites by a short central region, forming the heterotetrameric XerC-XerD complex that recombines DNA substrates. The complex is essential to convert dimers of the bacterial chromosome into monomers to permit their segregation at cell division. It also contributes to the segregational stability of plasmids at ColE1 xer (or cer) and pSC101 (or psi) sites. In the complex XerC specifically exchanges the top DNA strands (By similarity). {ECO:0000250, ECO:0000269|PubMed:10037776, ECO:0000269|PubMed:7744017, ECO:0000269|PubMed:9268326}. EcoCyc product frame: EG11069-MONOMER. Genomic coordinates: 3996287-3997183. EcoCyc protein note: XerC is part of the Xer site-specific recombination system .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8P6|protein.P0A8P6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=xerC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012448,ECOCYC:EG11069,GeneID:948355`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3996287-3997183:+; feature_type=gene
