---
entity_id: "gene.b1879"
entity_type: "gene"
name: "flhA"
source_database: "NCBI RefSeq"
source_id: "gene-b1879"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1879"
  - "flhA"
---

# flhA

`gene.b1879`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1879`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flhA (gene.b1879) is a gene entity. It encodes flhA (protein.P76298). Encoded protein function: FUNCTION: Required for formation of the rod structure of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin. EcoCyc product frame: G370-MONOMER. EcoCyc synonyms: flaH. Genomic coordinates: 1962972-1965050. EcoCyc protein note: FlhA is one of six integral membrane components of the flagellar export apparatus. FlhA has two regions: the hydrophobic N-terminal transmembrane region with eight membrane-spanning segments and the C-terminal cytoplasmic domain . The structures of the C-terminal domain of FlhA and a fragment of the domain have been determined by X-ray crystallography to a resolution of 2.9 and 3.2 Å, respectively . Temperature-sensitive mutations in the cytoplasmic region of FlhA can prevent flagellar export . FlhA is osmosensitive and is involved in the stress response at pH 6.5 or lower .

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76298|protein.P76298]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006272,ECOCYC:G370,GeneID:946390`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1962972-1965050:-; feature_type=gene
