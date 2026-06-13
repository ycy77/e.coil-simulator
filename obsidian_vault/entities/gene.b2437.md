---
entity_id: "gene.b2437"
entity_type: "gene"
name: "eutR"
source_database: "NCBI RefSeq"
source_id: "gene-b2437"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2437"
  - "eutR"
---

# eutR

`gene.b2437`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2437`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutR (gene.b2437) is a gene entity. It encodes eutR (protein.P36547). Encoded protein function: FUNCTION: Activates the transcription of the eut operon. Also positively regulates its own transcription. Probably binds ethanolamine and vitamin B12 as effectors. Competes with ethanolamine ammonia-lysase (EAL, the first enzyme in the EA degradation pathway) for adenosylcobalamin. {ECO:0000250|UniProtKB:Q9ZFU7}. EcoCyc product frame: EG12190-MONOMER. EcoCyc synonyms: yfeG. Genomic coordinates: 2554130-2555182. EcoCyc protein note: By making use of microarray analysis it was concluded that anaerobiosis does not affect the expression of eutR, although FNR appears to repress it. A putative FNR binding site, which is not shown in the paper, was identified upstream of this gene .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36547|protein.P36547]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008036,ECOCYC:EG12190,GeneID:946911`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2554130-2555182:-; feature_type=gene
