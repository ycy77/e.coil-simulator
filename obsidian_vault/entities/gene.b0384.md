---
entity_id: "gene.b0384"
entity_type: "gene"
name: "psiF"
source_database: "NCBI RefSeq"
source_id: "gene-b0384"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0384"
  - "psiF"
---

# psiF

`gene.b0384`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0384`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psiF (gene.b0384) is a gene entity. It encodes psiF (protein.P0AFM4). Encoded protein function: Phosphate starvation-inducible protein PsiF EcoCyc product frame: EG11401-MONOMER. Genomic coordinates: 403281-403601. EcoCyc protein note: Expression of psiF is induced during phosphate starvation .

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFM4|protein.P0AFM4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=psiF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001330,ECOCYC:EG11401,GeneID:945040`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:403281-403601:+; feature_type=gene
