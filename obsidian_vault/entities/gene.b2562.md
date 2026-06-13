---
entity_id: "gene.b2562"
entity_type: "gene"
name: "yfhL"
source_database: "NCBI RefSeq"
source_id: "gene-b2562"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2562"
  - "yfhL"
---

# yfhL

`gene.b2562`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2562`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfhL (gene.b2562) is a gene entity. It encodes yfhL (protein.P52102). Encoded protein function: FUNCTION: Ferredoxins are iron-sulfur proteins that transfer electrons in a wide variety of metabolic reactions. {ECO:0000305}. EcoCyc product frame: G7346-MONOMER. Genomic coordinates: 2699663-2699923. EcoCyc protein note: A ΔyfhL mutant contains reduced levels of the modified wobble base cmo5U34 in tRNAs .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52102|protein.P52102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfhL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008431,ECOCYC:G7346,GeneID:947031`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2699663-2699923:+; feature_type=gene
