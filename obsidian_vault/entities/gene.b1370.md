---
entity_id: "gene.b1370"
entity_type: "gene"
name: "insH5"
source_database: "NCBI RefSeq"
source_id: "gene-b1370"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1370"
  - "insH5"
---

# insH5

`gene.b1370`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1370`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

insH5 (gene.b1370) is a gene entity. It encodes insH5 (protein.P76071). Encoded protein function: FUNCTION: Involved in the transposition of the insertion sequence IS5. EcoCyc product frame: G6693-MONOMER. EcoCyc synonyms: yi52_5, trs5-5. Genomic coordinates: 1427746-1428726. EcoCyc protein note: InsH is believed to be the transposase for the insertion sequence element IS5. insH spans the length of IS5 . IS5 can enhance gene transcription when it is placed on either side of the promoter for a target gene. This enhancement depends specifically on InsH and its interaction with the termini of the IS5 sequence . The consensus target for IS5 insertion is C(T/A)A(G/A) . Many copies of IS5, and thus InsH, are present in typical E. coli strains .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76071|protein.P76071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004586,ECOCYC:G6693,GeneID:945944`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1427746-1428726:-; feature_type=gene
