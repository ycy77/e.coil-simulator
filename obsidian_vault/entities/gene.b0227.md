---
entity_id: "gene.b0227"
entity_type: "gene"
name: "yafL"
source_database: "NCBI RefSeq"
source_id: "gene-b0227"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0227"
  - "yafL"
---

# yafL

`gene.b0227`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0227`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafL (gene.b0227) is a gene entity. It encodes yafL (protein.Q47151). Encoded protein function: Probable endopeptidase YafL (EC 3.4.-.-) (Uncharacterized lipoprotein YafL) EcoCyc product frame: G6111-MONOMER. Genomic coordinates: 246712-247461. EcoCyc protein note: No information about this protein was found by a literature search conducted on July 31, 2008.

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47151|protein.Q47151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=yafL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000775,ECOCYC:G6111,GeneID:944899`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:246712-247461:+; feature_type=gene
