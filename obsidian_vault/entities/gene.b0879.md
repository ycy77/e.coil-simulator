---
entity_id: "gene.b0879"
entity_type: "gene"
name: "macB"
source_database: "NCBI RefSeq"
source_id: "gene-b0879"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0879"
  - "macB"
---

# macB

`gene.b0879`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0879`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

macB (gene.b0879) is a gene entity. It encodes macB (protein.P75831). Encoded protein function: FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:28504659, PubMed:29109272, PubMed:40083904, PubMed:40461577). MacB is a non-canonical ABC transporter that contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:17214741, PubMed:18955484, PubMed:29109272). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:28504659, PubMed:29109272). Involved in secretion of enterotoxin STII (PubMed:29109272). In addition, the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:29109272, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}. EcoCyc product frame: MACB. EcoCyc synonyms: ybjZ...

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75831|protein.P75831]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002989,ECOCYC:G6462,GeneID:945164`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:920347-922293:+; feature_type=gene
