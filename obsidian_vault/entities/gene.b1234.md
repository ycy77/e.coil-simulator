---
entity_id: "gene.b1234"
entity_type: "gene"
name: "rssA"
source_database: "NCBI RefSeq"
source_id: "gene-b1234"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1234"
  - "rssA"
---

# rssA

`gene.b1234`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1234`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rssA (gene.b1234) is a gene entity. It encodes rssA (protein.P0AFR0). Encoded protein function: NTE family protein RssA EcoCyc product frame: EG12120-MONOMER. EcoCyc synonyms: ychK. Genomic coordinates: 1289245-1290150. EcoCyc protein note: A non-polar rssA mutant does not exhibit a defect in regulation of RssB or RpoS . A point mutation in rssA was one of serveral changes found in a strain evolved for fast growth in glucose. Inactivation of rssA in the parent strain increased its specific growth rate in glucose as the sole source of carbon .

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFR0|protein.P0AFR0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rssA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004144,ECOCYC:EG12120,GeneID:945725`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1289245-1290150:+; feature_type=gene
