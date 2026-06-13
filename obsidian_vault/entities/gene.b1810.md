---
entity_id: "gene.b1810"
entity_type: "gene"
name: "yoaC"
source_database: "NCBI RefSeq"
source_id: "gene-b1810"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1810"
  - "yoaC"
---

# yoaC

`gene.b1810`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1810`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaC (gene.b1810) is a gene entity. It encodes yoaC (protein.P64490). Encoded protein function: Uncharacterized protein YoaC EcoCyc product frame: G6994-MONOMER. Genomic coordinates: 1894133-1894432. EcoCyc protein note: A knockout mutant of this gene was hypersensitive to boric acid exposure compared to other gene knockouts; a complementation assay restored its intrinsic boric acid resistance. Double and triple knockout mutants (ΔyoaCΔG7261, ΔG6253ΔEG12760ΔyoaC and ΔyfeSΔyoaCΔgarP) exhibited increasing sensitivity, respectively .

## Biological Role

Activated by yeiE (protein.P0ACR4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64490|protein.P64490]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006024,ECOCYC:G6994,GeneID:946308`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1894133-1894432:+; feature_type=gene
