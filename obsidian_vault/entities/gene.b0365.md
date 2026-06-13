---
entity_id: "gene.b0365"
entity_type: "gene"
name: "tauA"
source_database: "NCBI RefSeq"
source_id: "gene-b0365"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0365"
  - "tauA"
---

# tauA

`gene.b0365`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0365`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tauA (gene.b0365) is a gene entity. It encodes tauA (protein.Q47537). Encoded protein function: FUNCTION: Part of a binding-protein-dependent transport system for taurine. EcoCyc product frame: TAUA-MONOMER. EcoCyc synonyms: yaiR, ssiA. Genomic coordinates: 385232-386194. EcoCyc protein note: TauA is the predicted periplasmic binding protein of an ATP-dependent taurine uptake system . tauA in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Repressed by nac (protein.Q47005). Activated by cysB (protein.P0A9F3), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47537|protein.Q47537]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=tauA; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=tauA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=tauA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001256,ECOCYC:G6217,GeneID:945030`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:385232-386194:+; feature_type=gene
