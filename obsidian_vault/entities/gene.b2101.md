---
entity_id: "gene.b2101"
entity_type: "gene"
name: "yegW"
source_database: "NCBI RefSeq"
source_id: "gene-b2101"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2101"
  - "yegW"
---

# yegW

`gene.b2101`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2101`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yegW (gene.b2101) is a gene entity. It encodes ggaR (protein.P0ACM5). Encoded protein function: FUNCTION: Transcriptional regulator that regulates glycogen accumulation in response to the amount of glucose available to the cell (PubMed:38257942). Acts as a repressor of the yegTUV operon, which may be involved in glycogen accumulation (PubMed:38257942). Binds at two adjacent sites within the yegTUV upstream region (PubMed:38257942). {ECO:0000269|PubMed:38257942}. EcoCyc product frame: G7133-MONOMER. Genomic coordinates: 2182035-2182781. EcoCyc protein note: GgaR (repressor of glycogen accumulation) negatively regulates genes involved in glycogen accumulation in response to increased glucose concentration . This regulator is found in a constant concentration of approximately 10 molecules in the cell and appears to have just one target, the operon yegTUV, which it regulates by binding to two sites around the regulatory region of the operon. The molecule ADP-glucose, derived from the metabolism of glucose and a precursor of glycogen, appears to bind to GgaR to inactivate it, thus preventing the repression of the yegTUV operon . GgaR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the GntR family of transcription factors...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACM5|protein.P0ACM5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006952,ECOCYC:G7133,GeneID:946639`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2182035-2182781:-; feature_type=gene
