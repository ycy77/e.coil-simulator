---
entity_id: "gene.b0435"
entity_type: "gene"
name: "bolA"
source_database: "NCBI RefSeq"
source_id: "gene-b0435"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0435"
  - "bolA"
---

# bolA

`gene.b0435`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0435`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bolA (gene.b0435) is a gene entity. It encodes bolA (protein.P0ABE2). Encoded protein function: FUNCTION: Transcriptional regulator that plays an important role in general stress response. Has many effects on cell morphology, cell growth and cell division. Acts by regulating the transcription of many genes, including dacA (PBP-5), dacC (PBP-6), ampC and mreB. Probably involved in the coordination of genes that adapt the cell physiology in order to enhance cell adaptation and survival under stress conditions. Essential for normal cell morphology in stationary phase and under conditions of starvation (PubMed:10361282, PubMed:12354237, PubMed:19111750, PubMed:21464593, PubMed:25691594). Also regulates a complex network of genes encoding proteins related to biofilm development, and negatively modulates flagellar biosynthesis and swimming capacity. Could be a motile/adhesive transcriptional switch, specifically involved in the transition between the planktonic and the attachment stage of biofilm formation (PubMed:25691594). Overexpression produces round cell shape, impairs cell growth rate and induces biofilm development (PubMed:15345459, PubMed:21464593, PubMed:305364). {ECO:0000269|PubMed:10361282, ECO:0000269|PubMed:12354237, ECO:0000269|PubMed:15345459, ECO:0000269|PubMed:19111750, ECO:0000269|PubMed:21464593, ECO:0000269|PubMed:25691594, ECO:0000269|PubMed:305364}...

## Biological Role

Repressed by ompR (protein.P0AA16). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABE2|protein.P0ABE2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bolA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=bolA; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=bolA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001508,ECOCYC:EG10125,GeneID:947043`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:454472-454789:+; feature_type=gene
