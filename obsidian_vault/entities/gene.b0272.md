---
entity_id: "gene.b0272"
entity_type: "gene"
name: "xynR"
source_database: "NCBI RefSeq"
source_id: "gene-b0272"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0272"
  - "xynR"
---

# xynR

`gene.b0272`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0272`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xynR (gene.b0272) is a gene entity. It encodes xynR (protein.P77300). Encoded protein function: FUNCTION: Involved in regulation of xylonate catabolism. Represses the expression of both yagA and yagEF operons. Binds mainly at a single site within the spacer of the bidirectional transcription units yagA and yagEF. {ECO:0000269|PubMed:29087459}. EcoCyc product frame: G6144-MONOMER. EcoCyc synonyms: yagI. Genomic coordinates: 288404-289162. EcoCyc protein note: XynR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the IclR family of transcription factors (TFs) . Based on SELEX screening of Escherichia coli K-12 W3110, XynR, formerly known as YagI, was identified as a regulator of xylonate catabolism; it is a rare single-target TF, and its regulation network is still fixed within the CR4-6 prophage without significant cross-talk with the host. It regulates the bidirectional transcripts yagA(b) and yagEF(GH) . A single peak of XynR binding was identified within the spacer of bidirectional transcription units of the yagA and yagEF operons. However, by decreasing the cutoff of detection, approximately 30 low-level peaks were detected, which are all located inside open reading frames (ORFs)...

## Biological Role

Activated by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77300|protein.P77300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=xynR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000933,ECOCYC:G6144,GeneID:945016`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:288404-289162:-; feature_type=gene
