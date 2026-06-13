---
entity_id: "gene.b3438"
entity_type: "gene"
name: "gntR"
source_database: "NCBI RefSeq"
source_id: "gene-b3438"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3438"
  - "gntR"
---

# gntR

`gene.b3438`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3438`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gntR (gene.b3438) is a gene entity. It encodes gntR (protein.P0ACP5). Encoded protein function: FUNCTION: Negative regulator for the gluconate utilization system GNT-I, the gntUKR operon. EcoCyc product frame: PD03585. Genomic coordinates: 3577731-3578726. EcoCyc protein note: The Gluconate repressor," GntR, is a transcription factor that negatively regulates the operon involved in the catabolism of D-gluconate via the Entner-Doudoroff pathway and also represses genes involved in two different systems related to D-gluconate uptake: gluconate I and gluconate II . This regulator is part of the gntRKU operon, yet it can also be constitutively expressed as an independent (gntR) transcription unit . In addition, the genes regulated by GntR are induced when Escherichia coli is grown in the presence of the inducer, D-gluconate, and in the absence of glucose. In the absence of inducer, this repressor binds in tandem to inverted repeat sequences that consist of 20-nucleotide-long DNA target sites . Binding of GntR to DNA is diminished in the presence of the inducer D-gluconate. By using synthetic gene circuits, it was demonstrated that GntR represses transcription through stabilization of RNA polymerase (RNAP) at both positions upstream and downstream from the promoter . GntR is closely homologous to IdnR (53% identity) and belongs to the LacI/GalR family of transcriptional regulators...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACP5|protein.P0ACP5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gntR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011226,ECOCYC:EG12630,GeneID:947946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3577731-3578726:-; feature_type=gene
