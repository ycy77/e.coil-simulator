---
entity_id: "gene.b1689"
entity_type: "gene"
name: "ydiL"
source_database: "NCBI RefSeq"
source_id: "gene-b1689"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1689"
  - "ydiL"
---

# ydiL

`gene.b1689`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1689`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiL (gene.b1689) is a gene entity. It encodes ydiL (protein.P76196). Encoded protein function: Uncharacterized protein YdiL EcoCyc product frame: G6915-MONOMER. Genomic coordinates: 1770615-1770971. EcoCyc protein note: This uncharacterized enzyme was found to interact with the ENOLASE-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76196|protein.P76196]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydiL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005641,ECOCYC:G6915,GeneID:946181`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1770615-1770971:+; feature_type=gene
