---
entity_id: "gene.b0470"
entity_type: "gene"
name: "dnaX"
source_database: "NCBI RefSeq"
source_id: "gene-b0470"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0470"
  - "dnaX"
---

# dnaX

`gene.b0470`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0470`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaX (gene.b0470) is a gene entity. It encodes dnaX (protein.P06710). Encoded protein function: FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3'-5' exonuclease activity. The gamma complex (gamma(3),delta,delta') is thought to load beta dimers onto DNA by binding ATP which alters the complex's conformation so it can bind beta sliding clamp dimers and open them at one interface. Primed DNA is recognized, ATP is hydrolyzed releasing the gamma complex and closing the beta sliding clamp ring around the primed DNA (PubMed:9927437). {ECO:0000269|PubMed:2040637}.; FUNCTION: [Isoform tau]: Serves as a scaffold to trimerize the core complex (PubMed:7037770). {ECO:0000305|PubMed:7037770}.; FUNCTION: [Isoform gamma]: Interacts with the delta and delta' subunits to transfer the beta subunit on the DNA (PubMed:9927437). Interacts with ATP, drives ATP-induced conformational changes in the gamma complex that opens the beta sliding clamp ring. After loading of primed DNA ATP is hydrolyzed and the beta sliding clamp ring closes (PubMed:9927437). {ECO:0000269|PubMed:9927437}. EcoCyc product frame: MONOMER0-2383...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06710|protein.P06710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001633,ECOCYC:EG10245,GeneID:945105`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:492092-494023:+; feature_type=gene
