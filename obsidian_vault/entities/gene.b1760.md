---
entity_id: "gene.b1760"
entity_type: "gene"
name: "ynjH"
source_database: "NCBI RefSeq"
source_id: "gene-b1760"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1760"
  - "ynjH"
---

# ynjH

`gene.b1760`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1760`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynjH (gene.b1760) is a gene entity. It encodes ynjH (protein.P76227). Encoded protein function: Uncharacterized protein YnjH EcoCyc product frame: G6955-MONOMER. Genomic coordinates: 1841863-1842135. EcoCyc protein note: The promoter of ynjH is predicted to be σ28-dependent and can be transcribed by CPLX0-222 in vitro .

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76227|protein.P76227]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ynjH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynjH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005858,ECOCYC:G6955,GeneID:946279`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1841863-1842135:-; feature_type=gene
