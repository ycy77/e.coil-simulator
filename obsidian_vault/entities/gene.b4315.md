---
entity_id: "gene.b4315"
entity_type: "gene"
name: "fimI"
source_database: "NCBI RefSeq"
source_id: "gene-b4315"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4315"
  - "fimI"
---

# fimI

`gene.b4315`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4315`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimI (gene.b4315) is a gene entity. It encodes fimI (protein.P39264). Encoded protein function: Fimbrin-like protein FimI EcoCyc product frame: EG11974-MONOMER. Genomic coordinates: 4543728-4544267. EcoCyc protein note: The fimI gene is located in the fim gene cluster of Escherichia coli and has been shown to encode a 16.4 kDa noncytoplasmic protein product. Deletion mutations in fimI produced a piliation-negative phenotype, however the function of the FimI protein in pilus biosynthesis has not been determined . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including fimAICDFGH; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39264|protein.P39264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimI; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimI; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimI; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014147,ECOCYC:EG11974,GeneID:948841`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4543728-4544267:+; feature_type=gene
