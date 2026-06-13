---
entity_id: "gene.b3267"
entity_type: "gene"
name: "yhdV"
source_database: "NCBI RefSeq"
source_id: "gene-b3267"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3267"
  - "yhdV"
---

# yhdV

`gene.b3267`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3267`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhdV (gene.b3267) is a gene entity. It encodes yhdV (protein.P64622). Encoded protein function: Uncharacterized protein YhdV EcoCyc product frame: G7695-MONOMER. Genomic coordinates: 3418390-3418611. EcoCyc protein note: YhdV is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). yhdV was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 compared to pH 7.6) as measured by ribosome coverage of its transcripts using RNA-Seq .

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64622|protein.P64622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhdV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010728,ECOCYC:G7695,GeneID:947767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3418390-3418611:+; feature_type=gene
