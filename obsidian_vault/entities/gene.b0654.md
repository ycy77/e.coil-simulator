---
entity_id: "gene.b0654"
entity_type: "gene"
name: "gltJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0654"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0654"
  - "gltJ"
---

# gltJ

`gene.b0654`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0654`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltJ (gene.b0654) is a gene entity. It encodes gltJ (protein.P0AER3). Encoded protein function: FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000305|PubMed:9593292}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from P.luminescens strain TTO1 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. EcoCyc product frame: GLTJ-MONOMER. Genomic coordinates: 685929-686669. EcoCyc protein note: GltJ is the predicted integral membrane subunit of a glutamate/aspartate ABC transporter complex (see .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AER3|protein.P0AER3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002239,ECOCYC:EG12661,GeneID:945443`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:685929-686669:-; feature_type=gene
