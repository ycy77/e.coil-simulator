---
entity_id: "gene.b3552"
entity_type: "gene"
name: "yiaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3552"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3552"
  - "yiaD"
---

# yiaD

`gene.b3552`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3552`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaD (gene.b3552) is a gene entity. It encodes yiaD (protein.P37665). Encoded protein function: FUNCTION: Suppresses temperature-sensitive mutations in BamB when overexpressed. {ECO:0000269|PubMed:21228468}. EcoCyc product frame: EG12271-MONOMER. Genomic coordinates: 3716547-3717206. EcoCyc protein note: Sequence similarity suggests that YiaD is a member of the OmpA-OmpF Porin (OOP) Family . YiaD is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). yiaD is a multicopy suppressor of a temperature sensitive bamD mutant . Outer membrane protein profiles of bamD mutants with or without the yiaD multicopy plasmid suggest that YiaD is involved in the function of BamB .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37665|protein.P37665]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yiaD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011601,ECOCYC:EG12271,GeneID:948075`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3716547-3717206:+; feature_type=gene
