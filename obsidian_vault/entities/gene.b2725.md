---
entity_id: "gene.b2725"
entity_type: "gene"
name: "hycA"
source_database: "NCBI RefSeq"
source_id: "gene-b2725"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2725"
  - "hycA"
---

# hycA

`gene.b2725`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2725`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycA (gene.b2725) is a gene entity. It encodes hycA (protein.P0AEV4). Encoded protein function: FUNCTION: Regulatory protein for the formate hydrogenlyase system. Could act by directly interacting with FhlA or by preventing the binding of FhlA to the upstream activatory sequence (PubMed:1625581). Also down-regulates expression of the hyf operon (PubMed:12426353). {ECO:0000269|PubMed:12426353, ECO:0000269|PubMed:1625581}. EcoCyc product frame: EG10474-MONOMER. EcoCyc synonyms: hevA. Genomic coordinates: 2849974-2850435. EcoCyc protein note: This regulator participates in controlling several genes involved in the formate hydrogenlyase system . The mechanism of regulation by HycA is unknown. HycA may interact directly with the FhlA protein or prevent the binding of FhlA to activator sequences. Expression of hycA is activated by formate and hypophosphite (a formate analog) .

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEV4|protein.P0AEV4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycA; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008952,ECOCYC:EG10474,GeneID:947193`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2849974-2850435:-; feature_type=gene
