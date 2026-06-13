---
entity_id: "gene.b4362"
entity_type: "gene"
name: "dnaT"
source_database: "NCBI RefSeq"
source_id: "gene-b4362"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4362"
  - "dnaT"
---

# dnaT

`gene.b4362`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4362`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaT (gene.b4362) is a gene entity. It encodes dnaT (protein.P0A8J2). Encoded protein function: FUNCTION: Involved in the restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:8663104, PubMed:8663105, PubMed:8663106). Functions in the PriA-PriB and PriA-PriC restart pathways, but probably not in the PriC-Rep pathway (PubMed:15238512). Displaces ssDNA from a PriB-ssDNA complex (PubMed:25265331, PubMed:30659961). Also involved in inducing stable DNA replication during SOS response. It forms, in concert with DnaC protein and other prepriming proteins DnaB, PriA, PriB and PriC a prepriming protein complex on the specific site of the template DNA recognized by PriA (PubMed:8663104, PubMed:8663105). Binds single-stranded (ss)DNA in a cooperative manner; both the N- and C-terminal domains are required for cooperativity (PubMed:15238512, PubMed:25053836). Forms a spiral filament on ssDNA (PubMed:25053836). {ECO:0000269|PubMed:15238512, ECO:0000269|PubMed:25053836, ECO:0000269|PubMed:30659961, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105, ECO:0000269|PubMed:8663106}. EcoCyc product frame: EG10244-MONOMER. Genomic coordinates: 4600978-4601517.

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8J2|protein.P0A8J2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014306,ECOCYC:EG10244,GeneID:948813`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4600978-4601517:-; feature_type=gene
