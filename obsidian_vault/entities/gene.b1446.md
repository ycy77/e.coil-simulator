---
entity_id: "gene.b1446"
entity_type: "gene"
name: "ydcY"
source_database: "NCBI RefSeq"
source_id: "gene-b1446"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1446"
  - "ydcY"
---

# ydcY

`gene.b1446`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1446`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcY (gene.b1446) is a gene entity. It encodes ydcY (protein.P64455). Encoded protein function: Uncharacterized protein YdcY EcoCyc product frame: G6757-MONOMER. Genomic coordinates: 1517648-1517881. EcoCyc protein note: YdcY, when expressed from a plasmid, does not inactivate the orphan toxin G6756-MONOMER "OrtT" . The YdcY protein can be expressed as a His-tagged fusion protein .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64455|protein.P64455]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydcY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004821,ECOCYC:G6757,GeneID:945916`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1517648-1517881:+; feature_type=gene
