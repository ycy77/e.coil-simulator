---
entity_id: "gene.b1188"
entity_type: "gene"
name: "ycgB"
source_database: "NCBI RefSeq"
source_id: "gene-b1188"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1188"
  - "ycgB"
---

# ycgB

`gene.b1188`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1188`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgB (gene.b1188) is a gene entity. It encodes ycgB (protein.P29013). Encoded protein function: Uncharacterized protein YcgB EcoCyc product frame: EG11516-MONOMER. Genomic coordinates: 1235709-1237241. EcoCyc protein note: The ycgB ortholog of Salmonella enterica serovar Typhimurium belongs to the RpoS regulon .

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29013|protein.P29013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ycgB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003990,ECOCYC:EG11516,GeneID:946365`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1235709-1237241:-; feature_type=gene
