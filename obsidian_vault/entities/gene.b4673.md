---
entity_id: "gene.b4673"
entity_type: "gene"
name: "ymjD"
source_database: "NCBI RefSeq"
source_id: "gene-b4673"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4673"
  - "ymjD"
---

# ymjD

`gene.b4673`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4673`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ymjD (gene.b4673) is a gene entity. It encodes ymjD (protein.P0CD93). Encoded protein function: Protein YmjD EcoCyc product frame: MONOMER0-2872. Genomic coordinates: 1390868-1390933. EcoCyc protein note: The YmjD open reading frame was predicted based on the presence of a ribosome binding site in an intergenic region. YmjD shows high sequence similarity to the amino-terminal portion of an amino acid hydrolase; thus, this 21 amino acid protein may be a truncated remnant of a much larger protein. YmjD is highly expressed during stationary phase .

## Biological Role

Repressed by pgrR (protein.P77333).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CD93|protein.P0CD93]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77333|protein.P77333]] `RegulonDB` `S` - regulator=PgrR; target=ymjD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285156,ECOCYC:G0-10645,GeneID:7751617`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1390868-1390933:-; feature_type=gene
