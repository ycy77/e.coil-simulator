---
entity_id: "gene.b0450"
entity_type: "gene"
name: "glnK"
source_database: "NCBI RefSeq"
source_id: "gene-b0450"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0450"
  - "glnK"
---

# glnK

`gene.b0450`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0450`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnK (gene.b0450) is a gene entity. It encodes glnK (protein.P0AC55). Encoded protein function: FUNCTION: Involved in the regulation of nitrogen metabolism (PubMed:10760266, PubMed:11847102, PubMed:12366843, PubMed:14668330, PubMed:28538158, PubMed:8843440). Regulates the activity of its targets by protein-protein interaction in response to the nitrogen status of the cell (PubMed:10760266, PubMed:11847102, PubMed:14668330, PubMed:8843440). Involved in the regulation of the ammonium transporter AmtB so as to optimize ammonium uptake under all growth conditions (PubMed:11847102, PubMed:14668330, PubMed:16864585). In nitrogen-limited conditions, GlnK does not interact with AmtB, which remains active and imports ammonium. When extracellular ammonium increases, GlnK associates tightly with AmtB in the inner membrane, thereby inhibiting the transporter activity (PubMed:11847102, PubMed:14668330, PubMed:16864585). Also involved in the regulation of the glutamine synthetase adenylyltransferase/adenylyl-removing (AT/AR) enzyme GlnE and the glutamine synthetase GlnA (PubMed:10760266, PubMed:28538158, PubMed:8843440)...

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC55|protein.P0AC55]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001562,ECOCYC:EG12191,GeneID:945087`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:472598-472936:+; feature_type=gene
