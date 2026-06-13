---
entity_id: "gene.b3060"
entity_type: "gene"
name: "ttdR"
source_database: "NCBI RefSeq"
source_id: "gene-b3060"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3060"
  - "ttdR"
---

# ttdR

`gene.b3060`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3060`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ttdR (gene.b3060) is a gene entity. It encodes ttdR (protein.P45463). Encoded protein function: FUNCTION: Positive regulator required for L-tartrate-dependent anaerobic growth on glycerol. Induces expression of the ttdA-ttdB-ygjE operon. {ECO:0000269|PubMed:16804186}. EcoCyc product frame: MONOMER0-4119. EcoCyc synonyms: dan, ygiP. Genomic coordinates: 3205324-3206256.

## Biological Role

Repressed by hns (protein.P0ACF8), glaR (protein.P37338). Activated by ttdR (protein.P45463).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45463|protein.P45463]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P45463|protein.P45463]] `RegulonDB` `S` - regulator=Dan; target=ttdR; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ttdR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010045,ECOCYC:EG12694,GeneID:947562`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3205324-3206256:-; feature_type=gene
