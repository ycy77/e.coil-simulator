---
entity_id: "gene.b4244"
entity_type: "gene"
name: "pyrI"
source_database: "NCBI RefSeq"
source_id: "gene-b4244"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4244"
  - "pyrI"
---

# pyrI

`gene.b4244`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4244`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrI (gene.b4244) is a gene entity. It encodes pyrI (protein.P0A7F3). Encoded protein function: FUNCTION: Involved in allosteric regulation of aspartate carbamoyltransferase. EcoCyc product frame: ASPCARBREG-MONOMER. Genomic coordinates: 4470986-4471447.

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7F3|protein.P0A7F3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013889,ECOCYC:EG10811,GeneID:948763`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4470986-4471447:-; feature_type=gene
