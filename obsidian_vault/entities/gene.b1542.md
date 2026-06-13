---
entity_id: "gene.b1542"
entity_type: "gene"
name: "ydfI"
source_database: "NCBI RefSeq"
source_id: "gene-b1542"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1542"
  - "ydfI"
---

# ydfI

`gene.b1542`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1542`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydfI (gene.b1542) is a gene entity. It encodes ydfI (protein.P77260). Encoded protein function: Uncharacterized oxidoreductase YdfI (EC 1.-.-.-) EcoCyc product frame: G6816-MONOMER. Genomic coordinates: 1629453-1630913. EcoCyc protein note: A ΔydfI mutant has a defect in tosufloxacin-tolerant persister cell formation .

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77260|protein.P77260]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ydfI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005149,ECOCYC:G6816,GeneID:945861`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1629453-1630913:-; feature_type=gene
