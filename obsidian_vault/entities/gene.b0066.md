---
entity_id: "gene.b0066"
entity_type: "gene"
name: "thiQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0066"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0066"
  - "thiQ"
---

# thiQ

`gene.b0066`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0066`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiQ (gene.b0066) is a gene entity. It encodes thiQ (protein.P31548). Encoded protein function: FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}. EcoCyc product frame: SFUC-MONOMER. EcoCyc synonyms: sfuC, yabJ. Genomic coordinates: 72229-72927. EcoCyc protein note: ThiQ is the predicted ATP-binding subunit of a thiamine uptake system; ThiQ contains sequence motifs conserved in ATP-binding cassette (ABC) proteins

## Biological Role

Repressed by sgrR (protein.P33595).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31548|protein.P31548]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=thiQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000244,ECOCYC:EG11572,GeneID:944785`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:72229-72927:-; feature_type=gene
