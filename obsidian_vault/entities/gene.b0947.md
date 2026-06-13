---
entity_id: "gene.b0947"
entity_type: "gene"
name: "ycbX"
source_database: "NCBI RefSeq"
source_id: "gene-b0947"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0947"
  - "ycbX"
---

# ycbX

`gene.b0947`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0947`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycbX (gene.b0947) is a gene entity. It encodes ycbX (protein.P75863). Encoded protein function: FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:35640667). In the presence of methyl viologen as reduced electron donor, it is also active toward other N-hydroxy substrates such as 2-amino-6-hydroxylaminopurine (2-AHAP), N-hydroxyadenosine, N-hydroxyacetamidine, N-hydroxyurea and hydroxylamine, but it cannot use N-oxide and sulfoxide substrates, or nitrate and chlorate (PubMed:35640667). The reducing equivalents required for the detoxification reaction may be provided by the sulfite reductase component CysJ, which functions as a partner of YcbX (PubMed:20118259). YcbX is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:20118259, ECO:0000269|PubMed:35640667}. EcoCyc product frame: G6487-MONOMER. Genomic coordinates: 1006491-1007600.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75863|protein.P75863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003206,ECOCYC:G6487,GeneID:945563`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1006491-1007600:-; feature_type=gene
