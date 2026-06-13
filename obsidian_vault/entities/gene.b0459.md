---
entity_id: "gene.b0459"
entity_type: "gene"
name: "maa"
source_database: "NCBI RefSeq"
source_id: "gene-b0459"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0459"
  - "maa"
---

# maa

`gene.b0459`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0459`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

maa (gene.b0459) is a gene entity. It encodes maa (protein.P77791). Encoded protein function: FUNCTION: Catalyzes the CoA-dependent transfer of an acetyl group to maltose and other sugars (PubMed:1856235). Acetylates glucose exclusively at the C6 position and maltose at the C6 position of the non-reducing end glucosyl moiety. Is able to acetylate maltooligosaccharides (PubMed:12731863). {ECO:0000269|PubMed:12731863, ECO:0000269|PubMed:1856235}. EcoCyc product frame: MALTACETYLTRAN-MONOMER. EcoCyc synonyms: ylaD. Genomic coordinates: 479367-479918. EcoCyc protein note: Maltose O-acetyltransferase has broad substrate specificity, and is capable of acetylating many sugars. The enzyme is not part of the maltose system. Its specific physiological role is not known, but it is thought that the enzyme prevents the accumulation of free sugars to high levels through acetylation, playing a detoxifying role in the cell . Acetylmaltose is excreted into the culture medium in malB+ malQ strains, which accumulate maltose, but cannot metabolize it . The enzyme belongs to the hexapeptide repeat family of proteins. A crystal structure has been solved at 2.15 Å resolution . The most effective substrate is glucose, which is acetylated at the C6 position; maltose is acetylated at C6 of the nonreducing glucose moiety . Mac: "maltose transacetylase"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77791|protein.P77791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001591,ECOCYC:G58,GeneID:945096`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:479367-479918:-; feature_type=gene
