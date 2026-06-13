---
entity_id: "gene.b0143"
entity_type: "gene"
name: "pcnB"
source_database: "NCBI RefSeq"
source_id: "gene-b0143"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0143"
  - "pcnB"
---

# pcnB

`gene.b0143`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0143`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pcnB (gene.b0143) is a gene entity. It encodes pcnB (protein.P0ABF1). Encoded protein function: FUNCTION: Adds poly(A) tail to the 3' end of many RNAs, which usually targets these RNAs for decay. Plays a significant role in the global control of gene expression, through influencing the rate of transcript degradation, and in the general RNA quality control. Rho-independent transcription terminators may serve as polyadenylation signals. Seems to be involved in plasmid copy number control. {ECO:0000255|HAMAP-Rule:MF_00957, ECO:0000269|PubMed:10594833, ECO:0000269|PubMed:1438224, ECO:0000269|PubMed:17040898}. EcoCyc product frame: EG10690-MONOMER. Genomic coordinates: 157729-159126. EcoCyc protein note: Poly(A) polymerase I (PAP I) is responsible for the polyadenylation of 3' ends of RNA molecules. PAP I polyadenylates the vast majority of mRNA transcripts . Unlike in eukaryotes, increased polyadenylation of mRNAs leads to decreased mRNA half-life . Rho-independent transcription terminators appear to serve as targeting signals for polyadenylation . The Hfq protein appears to be involved in the recognition of 3' termini of RNA by poly(A) polymerase I . Polyadenylation of tRNA fragment has been demonstrated during tRNA processing of Glu2, Ile1 and Ala1B tRNAs...

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABF1|protein.P0ABF1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pcnB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pcnB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000493,ECOCYC:EG10690,GeneID:947318`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:157729-159126:-; feature_type=gene
