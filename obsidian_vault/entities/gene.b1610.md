---
entity_id: "gene.b1610"
entity_type: "gene"
name: "tus"
source_database: "NCBI RefSeq"
source_id: "gene-b1610"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1610"
  - "tus"
---

# tus

`gene.b1610`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1610`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tus (gene.b1610) is a gene entity. It encodes tus (protein.P16525). Encoded protein function: FUNCTION: Trans-acting protein required for termination of DNA replication. Binds to DNA replication terminator sequences (terA to terF) to prevent the passage of replication forks. The termination efficiency will be affected by the affinity of this protein for the terminator sequence. EcoCyc product frame: EG11038-MONOMER. EcoCyc synonyms: tau. Genomic coordinates: 1684259-1685188. EcoCyc protein note: Tus, also known as ter-binding protein (TBP), binds to ter sites, blocking the progress of DNA replication in a polar fashion, thus terminating replication . Leading-strand synthesis arrests immediately on contact with Tus, whereas the lagging strand arrests 50-70 nucleotides upstream from the site of Tus binding . Tus halts advancing replication forks by blocking the progress of the replicative helicase DnaB . ter-bound Tus has also demonstrated directional blocking of the helicases PriA, Rep and UvrD . Conversely, UvrD in combination with RecA appears to be able to restore viability in strains that have ectopic ter sites . It has been suggested that the effectivenes of Tus in blocking depends on the amount of adjacent duplex DNA present, though there are conflicting results in this area...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16525|protein.P16525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005378,ECOCYC:EG11038,GeneID:945135`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1684259-1685188:+; feature_type=gene
