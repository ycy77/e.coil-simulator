---
entity_id: "gene.b0993"
entity_type: "gene"
name: "torS"
source_database: "NCBI RefSeq"
source_id: "gene-b0993"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0993"
  - "torS"
---

# torS

`gene.b0993`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0993`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torS (gene.b0993) is a gene entity. It encodes torS (protein.P39453). Encoded protein function: FUNCTION: Member of the two-component regulatory system TorS/TorR involved in the anaerobic utilization of trimethylamine-N-oxide (TMAO). Detects the presence of TMAO in the medium and, in response, activates TorR via a four-step phosphorelay. When TMAO is removed, TorS can dephosphorylate TorR, probably by a reverse phosphorelay involving His-860 and Asp-733. EcoCyc product frame: TORS-MONOMER. EcoCyc synonyms: yccI. Genomic coordinates: 1053434-1056178. EcoCyc protein note: TorS is the histidine kinase of a multi component regulatory system which induces expression of the torCAD operon encoding the trimethylamine-N-oxide (TMAO) respiratory system of E. coli. TorS is required for torCAD operon expression . TorS contains three phosphorylation sites and is an unorthodox sensor kinase; the protein contains two predicted transmembrane regions, an N-terminal detector or sensor region, a transmitter domain with a histidine phosphorylation site (H443) and an ATP binding motif, a receiver domain with an aspartate phosphorylation site (D723), and a C-terminal alternative transmitter domain with a phosphorylation site (H850)...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39453|protein.P39453]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003354,ECOCYC:G6514,GeneID:945595`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1053434-1056178:-; feature_type=gene
