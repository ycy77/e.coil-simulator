---
entity_id: "gene.b1994"
entity_type: "gene"
name: "insH6"
source_database: "NCBI RefSeq"
source_id: "gene-b1994"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1994"
  - "insH6"
---

# insH6

`gene.b1994`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1994`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH6 (gene.b1994) is a gene entity. It encodes insH6 (protein.P0CE53). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. EcoCyc product frame: G7074-MONOMER. EcoCyc synonyms: yi52_6, trs5-6. Genomic coordinates: 2066305-2067285. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CE53|protein.P0CE53]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006619,ECOCYC:G7074,GeneID:946507`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2066305-2067285:-; feature_type=gene
