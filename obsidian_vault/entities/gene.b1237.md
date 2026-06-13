---
entity_id: "gene.b1237"
entity_type: "gene"
name: "hns"
source_database: "NCBI RefSeq"
source_id: "gene-b1237"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1237"
  - "hns"
---

# hns

`gene.b1237`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1237`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hns (gene.b1237) is a gene entity. It encodes hns (protein.P0ACF8). Encoded protein function: FUNCTION: A DNA-binding protein implicated in transcriptional repression (silencing) (PubMed:16963779, PubMed:17046956, PubMed:2128918, PubMed:23543115, PubMed:333393, PubMed:8890170, PubMed:8913298, PubMed:9398522). Also involved in bacterial chromosome organization and compaction (PubMed:10982869, PubMed:21903814, PubMed:6379600). H-NS binds tightly to AT-rich dsDNA and inhibits transcription (PubMed:16963779, PubMed:17435766, PubMed:17881364, PubMed:23543115, PubMed:2512122). Binds upstream and downstream of initiating RNA polymerase, trapping it in a loop and preventing transcription (PubMed:11714691). Binds to hundreds of sites, approximately half its binding sites are in non-coding DNA, which only accounts for about 10% of the genome (PubMed:16963779, PubMed:17046956, PubMed:23543115). Many of these loci were horizontally transferred (HTG); this offers the selective advantage of silencing foreign DNA while keeping it in the genome in case of need (PubMed:17046956, PubMed:17881364, PubMed:26789284). Suppresses transcription at many intragenic sites as well as transcription of spurious, non-coding RNAs genome-wide (PubMed:24449106)...

## Biological Role

Repressed by dsrA (gene.b1954), hns (protein.P0ACF8). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cspA (protein.P0A9X9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACF8|protein.P0ACF8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hns; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=hns; function=+
- `activates` <-- [[protein.P0A9X9|protein.P0A9X9]] `RegulonDB` `S` - regulator=CspA; target=hns; function=+
- `represses` <-- [[gene.b1954|gene.b1954]] `RegulonDB` `S` - regulator=DsrA; target=hns; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=hns; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004152,ECOCYC:EG10457,GeneID:945829`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1292509-1292922:-; feature_type=gene
