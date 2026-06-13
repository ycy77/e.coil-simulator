---
entity_id: "gene.b1955"
entity_type: "gene"
name: "yedP"
source_database: "NCBI RefSeq"
source_id: "gene-b1955"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1955"
  - "yedP"
---

# yedP

`gene.b1955`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1955`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yedP (gene.b1955) is a gene entity. It encodes yedP (protein.P76329). Encoded protein function: Mannosyl-3-phosphoglycerate phosphatase (MPGP) (EC 3.1.3.70) EcoCyc product frame: G7048-MONOMER. Genomic coordinates: 2025511-2026326. EcoCyc protein note: YedP is a predicted phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. No phosphatase activity was detected using a variety of possible substrates; thus, the enzyme may be highly substrate-specific . Later, YedP was annotated as a mannosyl-3-phosphoglycerate phosphatase based on its membership in subcluster C2.B.2 of the HAD superfamily .

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76329|protein.P76329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006493,ECOCYC:G7048,GeneID:946472`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2025511-2026326:+; feature_type=gene
