---
entity_id: "gene.b3850"
entity_type: "gene"
name: "hemG"
source_database: "NCBI RefSeq"
source_id: "gene-b3850"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3850"
  - "hemG"
---

# hemG

`gene.b3850`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3850`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemG (gene.b3850) is a gene entity. It encodes hemG (protein.P0ACB4). Encoded protein function: FUNCTION: Catalyzes the 6-electron oxidation of protoporphyrinogen IX to form protoporphyrin IX; under anaerobic conditions uses menaquinone as an electron acceptor, under aerobic condition uses ubiquinone as an electron acceptor. {ECO:0000255|HAMAP-Rule:MF_00853}.; FUNCTION: Anaerobically in vitro transfers electrons to fumarate reductase and nitrate reductase; transfer to nitrate reductase couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis (PubMed:19583219, PubMed:20484676). Neither mesoporphyrinogen nor coproporphyrinogen are substrates (PubMed:19583219). Under aerobic conditions in vitro forms protoporphyrin IX using ubiquinone as an electron acceptor, is able to transfer electrons to cytochrome bd oxidase and cytochrome bo oxidase; transfer to these oxidases couples this reaction to electron transfer across the cell inner membrane and thus ATP synthesis. In cell free extracts deletion of both cytochrome oxidases prevents formation of protoporphyrin IX (PubMed:20484676). {ECO:0000269|PubMed:19583219, ECO:0000269|PubMed:20484676}. EcoCyc product frame: PROTOPORGENOXI-MONOMER. EcoCyc synonyms: yihB. Genomic coordinates: 4034608-4035153.

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACB4|protein.P0ACB4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012577,ECOCYC:EG11485,GeneID:948331`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4034608-4035153:+; feature_type=gene
