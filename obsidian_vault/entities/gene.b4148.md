---
entity_id: "gene.b4148"
entity_type: "gene"
name: "gdx"
source_database: "NCBI RefSeq"
source_id: "gene-b4148"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4148"
  - "gdx"
---

# gdx

`gene.b4148`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4148`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gdx (gene.b4148) is a gene entity. It encodes gdx (protein.P69937). Encoded protein function: FUNCTION: Guanidinium ion exporter. Couples guanidinium export to the proton motive force, exchanging one guanidinium ion for two protons (PubMed:29507227). Overexpression leads to resistance to a subset of toxic quaternary ammonium compounds such as cetylpyridinium, cetyldimethylethyl ammonium and cetrimide cations (PubMed:11948170). {ECO:0000269|PubMed:11948170, ECO:0000269|PubMed:29507227}. EcoCyc product frame: SUGE-MONOMER. EcoCyc synonyms: sugE. Genomic coordinates: 4376875-4377192.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69937|protein.P69937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013588,ECOCYC:EG11616,GeneID:948671`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4376875-4377192:+; feature_type=gene
