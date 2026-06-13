---
entity_id: "gene.b0306"
entity_type: "gene"
name: "ykgE"
source_database: "NCBI RefSeq"
source_id: "gene-b0306"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0306"
  - "ykgE"
---

# ykgE

`gene.b0306`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0306`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ykgE (gene.b0306) is a gene entity. It encodes ykgE (protein.P77252). Encoded protein function: Uncharacterized protein YkgE EcoCyc product frame: G6176-MONOMER. Genomic coordinates: 321608-322327. EcoCyc protein note: While their physiological role in E. coli remains unknown, the ykgEFG genes are homologous to newly identified lactate utilization genes in Shewanella oneidensis. Low-copy expression of E. coli ykgEFG in S. oneidensis complements the ability of the Δdld-II ΔlldF double mutant for growth on L-lactate, but not D-lactate . Overexpression of ykgEFG in E. coli restores the ability of a EG10231 dld mutant to grow on D-lactate; crude extracts of an overexpressing strain contain elevated levels of both L- and D-lactate dehydrogenase activity .

## Biological Role

Repressed by yieP (protein.P31475), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77252|protein.P77252]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ykgE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001058,ECOCYC:G6176,GeneID:948438`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:321608-322327:+; feature_type=gene
