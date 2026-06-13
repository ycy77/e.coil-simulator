---
entity_id: "gene.b4485"
entity_type: "gene"
name: "ytfR"
source_database: "NCBI RefSeq"
source_id: "gene-b4485"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4485"
  - "ytfR"
---

# ytfR

`gene.b4485`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4485`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfR (gene.b4485) is a gene entity. It encodes ytfR (protein.Q6BEX0). Encoded protein function: FUNCTION: Part of the ABC transporter complex YtfQRT-YjfF involved in galactofuranose transport (Probable). Responsible for energy coupling to the transport system (Probable). {ECO:0000305, ECO:0000305|PubMed:19744923}. EcoCyc product frame: YTFR-MONOMER. EcoCyc synonyms: ytfS, b4228, b4229. Genomic coordinates: 4451058-4452560. EcoCyc protein note: Sequence analysis suggests that YtfR is tthe ATP binding protein of an ATP-binding cassette (ABC) transporter .

## Biological Role

Repressed by araC (protein.P0A9E0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q6BEX0|protein.Q6BEX0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=ytfR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174118,ECOCYC:EG12518,GeneID:2847725`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4451058-4452560:+; feature_type=gene
