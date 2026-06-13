---
entity_id: "gene.b4325"
entity_type: "gene"
name: "yjiC"
source_database: "NCBI RefSeq"
source_id: "gene-b4325"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4325"
  - "yjiC"
---

# yjiC

`gene.b4325`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4325`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjiC (gene.b4325) is a gene entity. It encodes yjiC (protein.P39374). Encoded protein function: Uncharacterized protein YjiC EcoCyc product frame: G7922-MONOMER. Genomic coordinates: 4555490-4556320. EcoCyc protein note: In an atypical enteropathogenic (aEPEC) E. coli strain, a transposon insertion into a gene with similarity to yjiC eliminates its ability to form biofilms .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39374|protein.P39374]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=yjiC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014181,ECOCYC:G7922,GeneID:948850`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4555490-4556320:-; feature_type=gene
