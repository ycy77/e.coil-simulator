---
entity_id: "gene.b2004"
entity_type: "gene"
name: "cbeA"
source_database: "NCBI RefSeq"
source_id: "gene-b2004"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2004"
  - "cbeA"
---

# cbeA

`gene.b2004`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2004`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbeA (gene.b2004) is a gene entity. It encodes cbeA (protein.P76364). Encoded protein function: FUNCTION: Antitoxin component of a type IV toxin-antitoxin (TA) system (PubMed:14594833, PubMed:22515815, PubMed:28257056). Antitoxin that counteracts the effect of its cognate toxin CbtA (YeeV) (PubMed:14594833, PubMed:22515815, PubMed:28257056). It does not bind to the toxin but instead binds to MreB and FtsZ (the toxin targets), enhancing their polymerization by forming higher-order bundles; it is probably retained in the MreB and FtsZ filament bundles (PubMed:22515815). The mechanism has been proposed to require intergenic DNA, in cis, between the cbeA (yeeU) and cbta (yeeV) genes (PubMed:14594833). The intergenic region was not found to be necessary in another study (PubMed:22515815). Also counteracts the morphological defects caused by overexpression of SulA and DicB on cell shape (PubMed:22515815). Also counteracts the effect of non-cognate toxins YfkI and YpjF (PubMed:28257056). {ECO:0000269|PubMed:14594833, ECO:0000269|PubMed:22515815, ECO:0000269|PubMed:28257056}. EcoCyc product frame: G7084-MONOMER. EcoCyc synonyms: yeeU. Genomic coordinates: 2077112-2077480. EcoCyc protein note: CbeA is the antitoxin of the CbtA-CbeA toxin-antitoxin system. Unlike other antitoxins, CbeA does not interact directly with the toxin CbtA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76364|protein.P76364]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006656,ECOCYC:G7084,GeneID:946510`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2077112-2077480:+; feature_type=gene
