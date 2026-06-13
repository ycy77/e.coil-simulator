---
entity_id: "gene.b3873"
entity_type: "gene"
name: "yihM"
source_database: "NCBI RefSeq"
source_id: "gene-b3873"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3873"
  - "yihM"
---

# yihM

`gene.b3873`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3873`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihM (gene.b3873) is a gene entity. It encodes yihM (protein.P32134). Encoded protein function: Uncharacterized protein YihM EcoCyc product frame: EG11839-MONOMER. Genomic coordinates: 4061165-4062145. EcoCyc protein note: Expression of yihM is upregulated by hexane and is increased in an organic solvent-tolerant strain. Overexpression of yihM does not increase tolerance to hexane or cyclohexane .

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32134|protein.P32134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yihM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012653,ECOCYC:EG11839,GeneID:948367`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4061165-4062145:+; feature_type=gene
