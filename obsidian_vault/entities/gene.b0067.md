---
entity_id: "gene.b0067"
entity_type: "gene"
name: "thiP"
source_database: "NCBI RefSeq"
source_id: "gene-b0067"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0067"
  - "thiP"
---

# thiP

`gene.b0067`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0067`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiP (gene.b0067) is a gene entity. It encodes thiP (protein.P31549). Encoded protein function: FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:12175925, ECO:0000305}. EcoCyc product frame: SFUB-MONOMER. EcoCyc synonyms: sfuB, yabK. Genomic coordinates: 72911-74521. EcoCyc protein note: ThiP is the predicted inner membrane permease of an ATP-dependent thiamine uptake system

## Biological Role

Repressed by sgrR (protein.P33595).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31549|protein.P31549]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P33595|protein.P33595]] `RegulonDB` `C` - regulator=SgrR; target=thiP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000246,ECOCYC:EG11573,GeneID:944784`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:72911-74521:-; feature_type=gene
