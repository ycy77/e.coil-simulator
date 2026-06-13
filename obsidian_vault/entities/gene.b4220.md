---
entity_id: "gene.b4220"
entity_type: "gene"
name: "tamA"
source_database: "NCBI RefSeq"
source_id: "gene-b4220"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4220"
  - "tamA"
---

# tamA

`gene.b4220`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4220`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tamA (gene.b4220) is a gene entity. It encodes tamA (protein.P0ADE4). Encoded protein function: FUNCTION: Component of the translocation and assembly module (TAM), which facilitates the insertion and assembly of specific beta-barrel proteins into the outer membrane (PubMed:22466966, PubMed:25341963, PubMed:28752534, PubMed:39174534). Promotes the assembly and secretion across the outer membrane of a subset of autotransporters, such as Ag43 (PubMed:22466966, PubMed:25341963). Involved in the assembly of the outer membrane usher protein FimD (PubMed:28752534). In vitro, when TAM is reconstituted into preformed liposomes, it can promote the assembly of several outer membrane proteins, including OmpA, EspP, Ag43 and FadL (PubMed:39174534). TamA is sufficient to catalyze a low level of outer membrane protein (OMP) assembly, but both TamA and TamB are required for efficient OMP assembly (PubMed:39174534). TamA must bind to the beta signal of client proteins to promote their assembly (PubMed:39174534). Has anion selective channel-forming ability, but the physiological relevance of this activity is unclear (PubMed:17214547). {ECO:0000269|PubMed:17214547, ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:25341963, ECO:0000269|PubMed:28752534, ECO:0000269|PubMed:39174534}. EcoCyc product frame: G7874-MONOMER. EcoCyc synonyms: ytfM. Genomic coordinates: 4442382-4444115...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADE4|protein.P0ADE4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013809,ECOCYC:G7874,GeneID:948733`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4442382-4444115:+; feature_type=gene
