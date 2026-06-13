---
entity_id: "gene.b3705"
entity_type: "gene"
name: "yidC"
source_database: "NCBI RefSeq"
source_id: "gene-b3705"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3705"
  - "yidC"
---

# yidC

`gene.b3705`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3705`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yidC (gene.b3705) is a gene entity. It encodes yidC (protein.P25714). Encoded protein function: FUNCTION: Inner membrane protein required for the insertion and/or proper folding and/or complex formation of integral inner membrane proteins. Involved in integration of membrane proteins that insert dependently and independently of the Sec translocase complex, as well as at least 2 lipoproteins. Its own insertion requires SRP and is Sec translocase-dependent. Essential for the integration of Sec-dependent subunit a of the F(0)ATP synthase, FtsQ and SecE proteins and for Sec-independent subunit c of the F(0)ATP synthase, M13 phage procoat and the N-terminus of leader peptidase Lep. Probably interacts directly with Sec-independent substrates. Sec-dependent protein FtsQ interacts first with SecY then subsequently with YidC. Sec-dependent LacY and MalF require YidC to acquire tertiary structure and stability, a chaperone-like function, but not for membrane insertion. Stable maltose transport copmplex formation (MalFGK(2)) also requires YidC. Partially complements a Streptococcus mutans yidC2 disruption mutant. {ECO:0000269|PubMed:10675323, ECO:0000269|PubMed:10949305, ECO:0000269|PubMed:12724529, ECO:0000269|PubMed:12950181, ECO:0000269|PubMed:15067017, ECO:0000269|PubMed:15140892, ECO:0000269|PubMed:17073462, ECO:0000269|PubMed:18456666}. EcoCyc product frame: YIDC...

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25714|protein.P25714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012120,ECOCYC:EG11197,GeneID:948214`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3885076-3886722:+; feature_type=gene
