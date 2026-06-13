---
entity_id: "gene.b1931"
entity_type: "gene"
name: "yedK"
source_database: "NCBI RefSeq"
source_id: "gene-b1931"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1931"
  - "yedK"
---

# yedK

`gene.b1931`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1931`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedK (gene.b1931) is a gene entity. It encodes yedK (protein.P76318). Encoded protein function: FUNCTION: Sensor of abasic sites in single-stranded DNA (ssDNA) required to preserve genome integrity by promoting error-free repair of abasic sites (PubMed:30554877). Recognizes and binds abasic sites in ssDNA at replication forks and chemically modifies the lesion by forming a covalent cross-link with DNA: forms a stable thiazolidine linkage between a ring-opened abasic site and the alpha-amino and sulfhydryl substituents of its N-terminal catalytic cysteine residue (PubMed:30554877, PubMed:31235915, PubMed:31504793). The DNA-protein cross-link is then reversed: able to catalyze the reversal of the thiazolidine cross-link and cycle between a cross-link and a non-cross-linked state depending on DNA context: mediates self-reversal of the thiazolidine cross-link in double stranded DNA (PubMed:35934051, PubMed:37519246). May act as a protease: mediates autocatalytic processing of its N-terminal methionine in order to expose the catalytic cysteine (By similarity). {ECO:0000250|UniProtKB:Q8R1M0, ECO:0000269|PubMed:30554877, ECO:0000269|PubMed:31235915, ECO:0000269|PubMed:31504793, ECO:0000269|PubMed:35934051, ECO:0000269|PubMed:37519246}. EcoCyc product frame: EG11662-MONOMER. EcoCyc synonyms: yedG. Genomic coordinates: 2009821-2010489...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76318|protein.P76318]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006428,ECOCYC:EG11662,GeneID:946435`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2009821-2010489:+; feature_type=gene
