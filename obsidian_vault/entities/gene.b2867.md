---
entity_id: "gene.b2867"
entity_type: "gene"
name: "xdhB"
source_database: "NCBI RefSeq"
source_id: "gene-b2867"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2867"
  - "xdhB"
---

# xdhB

`gene.b2867`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2867`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xdhB (gene.b2867) is a gene entity. It encodes xdhB (protein.Q46800). Encoded protein function: FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism). EcoCyc product frame: G7486-MONOMER. EcoCyc synonyms: ygeT. Genomic coordinates: 3002614-3003492. EcoCyc protein note: XdhB has similarity to YagS . XdhB has sequence similarity to the FAD-binding domain of Drosophila melanogaster xanthine dehydrogenase .

## Biological Role

Activated by rpoN (protein.P24255).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46800|protein.Q46800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=xdhB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009416,ECOCYC:G7486,GeneID:947205`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3002614-3003492:+; feature_type=gene
