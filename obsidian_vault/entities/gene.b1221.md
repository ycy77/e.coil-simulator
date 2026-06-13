---
entity_id: "gene.b1221"
entity_type: "gene"
name: "narL"
source_database: "NCBI RefSeq"
source_id: "gene-b1221"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1221"
  - "narL"
---

# narL

`gene.b1221`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1221`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narL (gene.b1221) is a gene entity. It encodes narL (protein.P0AF28). Encoded protein function: FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins. EcoCyc product frame: PHOSPHO-NARL. EcoCyc synonyms: frdR, narR. Genomic coordinates: 1275179-1275829. EcoCyc protein note: NarL, "nitrate/nitrite response regulator NarL," is a transcriptional dual regulator of many anaerobic electron transport and fermentation-related genes in the response to the availability of high concentrations of nitrate or nitrite . NarL activates expression of 51 operons in response to nitrate, mostly genes needed for nitrate respiration. NarL represses 41 operons involved in alternative respiratory pathways, such as fumarate reduction or fermentation of simple sugars . The response regulator NarL belongs to the LuxR/UhpA family and is part of the two-component system NarX-NarL. There is intensive cross-regulation with the paralogous two-component system NarQ-NarP . Each of the sensors, NarX and NarQ, is able to phosphorylate NarL and NarP, leading to the activation of both proteins...

## Biological Role

Activated by modE (protein.P0A9G8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF28|protein.P0AF28]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=narL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004097,ECOCYC:EG10643,GeneID:945795`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1275179-1275829:-; feature_type=gene
