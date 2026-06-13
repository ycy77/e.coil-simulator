---
entity_id: "gene.b0682"
entity_type: "gene"
name: "chiQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0682"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0682"
  - "chiQ"
---

# chiQ

`gene.b0682`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0682`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chiQ (gene.b0682) is a gene entity. It encodes chiQ (protein.P75734). Encoded protein function: Uncharacterized lipoprotein ChiQ EcoCyc product frame: G6371-MONOMER. EcoCyc synonyms: ybfN. Genomic coordinates: 709790-710116. EcoCyc protein note: ChiQ is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). In a large genetic interaction screen, chiQ showed genetic interactions with a number of proteins involved in translation and ribosome biogenesis. A ΔchiQ mutant shows increased levels of stop codon readthrough . Hfq appears to repress expression of chiP and chiQ .

## Biological Role

Repressed by chiX (gene.b4585), nagC (protein.P0AF20).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75734|protein.P75734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[gene.b4585|gene.b4585]] `RegulonDB` `S` - regulator=ChiX; target=chiQ; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=chiQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002325,ECOCYC:G6371,GeneID:945713`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:709790-710116:+; feature_type=gene
