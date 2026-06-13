---
entity_id: "gene.b3952"
entity_type: "gene"
name: "pflC"
source_database: "NCBI RefSeq"
source_id: "gene-b3952"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3952"
  - "pflC"
---

# pflC

`gene.b3952`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3952`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pflC (gene.b3952) is a gene entity. It encodes pflC (protein.P32675). Encoded protein function: FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}. EcoCyc product frame: EG11911-MONOMER. EcoCyc synonyms: yijM. Genomic coordinates: 4146258-4147136. EcoCyc protein note: PflC was identified by sequence similarity as a homolog of pyruvate formate-lyase activating enzyme . The protein belongs to the radical SAM superfamily. Effects of a pflC knockout have been studied; the fermentation pattern under microaerobic conditions is similar to wild type .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32675|protein.P32675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012937,ECOCYC:EG11911,GeneID:948453`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4146258-4147136:+; feature_type=gene
