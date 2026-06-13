---
entity_id: "gene.b0552"
entity_type: "gene"
name: "insH2"
source_database: "NCBI RefSeq"
source_id: "gene-b0552"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0552"
  - "insH2"
---

# insH2

`gene.b0552`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0552`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH2 (gene.b0552) is a gene entity. It encodes insH2 (protein.P0CE50). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. EcoCyc product frame: MONOMER0-4234. EcoCyc synonyms: trs5-2, yi52_2. Genomic coordinates: 574737-575717. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE50|protein.P0CE50]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001886,ECOCYC:G6308,GeneID:946163`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:574737-575717:-; feature_type=gene
