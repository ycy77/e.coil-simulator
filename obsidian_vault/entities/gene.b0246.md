---
entity_id: "gene.b0246"
entity_type: "gene"
name: "yafW"
source_database: "NCBI RefSeq"
source_id: "gene-b0246"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0246"
  - "yafW"
---

# yafW

`gene.b0246`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0246`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafW (gene.b0246) is a gene entity. It encodes yafW (protein.Q47684). Encoded protein function: FUNCTION: Antitoxin component of a type IV toxin-antitoxin (TA) system. Antitoxin that counteracts the effect of cognate toxin YkfI (PubMed:14594833, PubMed:28257056). It does not seem to bind to the cognate toxin but instead induces toxin loss by an unknown mechanism (PubMed:14594833). Co-overexpression of toxin YkfI and antitoxin YafW leads to formation of elongated cells (PubMed:28257056). {ECO:0000269|PubMed:14594833, ECO:0000269|PubMed:28257056}. EcoCyc product frame: G6121-MONOMER. Genomic coordinates: 263690-264007. EcoCyc protein note: Episomal expression of ykfI causes inhibition of cell growth and decreased viability, compared to wild type , and this phenotype is suppressed by coexpression of yafW . Antitoxin production reduces toxin abundance, probably by a post-transcriptional mechanism . The YafW and YeeU antitoxins are partially interchangeable with respect to inhibition of toxicity caused by YkfI or YeeV production . YeeV, YkfI, and YpjF have similarity to each other and define a protein family of cellular toxins .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47684|protein.Q47684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000838,ECOCYC:G6121,GeneID:944929`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:263690-264007:-; feature_type=gene
