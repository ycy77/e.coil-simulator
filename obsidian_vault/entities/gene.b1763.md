---
entity_id: "gene.b1763"
entity_type: "gene"
name: "topB"
source_database: "NCBI RefSeq"
source_id: "gene-b1763"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1763"
  - "topB"
---

# topB

`gene.b1763`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1763`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

topB (gene.b1763) is a gene entity. It encodes topB (protein.P14294). Encoded protein function: FUNCTION: Releases the supercoiling and torsional tension of DNA, which is introduced during the DNA replication and transcription, by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then undergoes passage around the unbroken strand, thus removing DNA supercoils. Finally, in the religation step, the DNA 3'-OH attacks the covalent intermediate to expel the active-site tyrosine and restore the DNA phosphodiester backbone. TOP3 is a potent decatenase. {ECO:0000255|HAMAP-Rule:MF_00953, ECO:0000269|PubMed:2553698, ECO:0000269|PubMed:6326814}. EcoCyc product frame: EG11014-MONOMER. EcoCyc synonyms: mutR. Genomic coordinates: 1844999-1846960. EcoCyc protein note: E. coli possess multiple DNA topoisomerases which coordinate, as well as compete, in order to maintain chromosomes in the appropriate topological state commensurate with their need for replication and transcription...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14294|protein.P14294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005869,ECOCYC:EG11014,GeneID:946141`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1844999-1846960:-; feature_type=gene
