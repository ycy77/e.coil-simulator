---
entity_id: "gene.b3505"
entity_type: "gene"
name: "insH11"
source_database: "NCBI RefSeq"
source_id: "gene-b3505"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3505"
  - "insH11"
---

# insH11

`gene.b3505`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3505`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH11 (gene.b3505) is a gene entity. It encodes insH11 (protein.P0CE58). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. EcoCyc product frame: MONOMER0-4241. EcoCyc synonyms: yi52_11, trs5-11. Genomic coordinates: 3652182-3653162. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE58|protein.P0CE58]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011446,ECOCYC:G7769,GeneID:948015`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3652182-3653162:-; feature_type=gene
