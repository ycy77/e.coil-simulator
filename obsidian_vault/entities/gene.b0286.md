---
entity_id: "gene.b0286"
entity_type: "gene"
name: "paoA"
source_database: "NCBI RefSeq"
source_id: "gene-b0286"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0286"
  - "paoA"
---

# paoA

`gene.b0286`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0286`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paoA (gene.b0286) is a gene entity. It encodes paoA (protein.P77165). Encoded protein function: FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. EcoCyc product frame: G6157-MONOMER. EcoCyc synonyms: yagT. Genomic coordinates: 301884-302573. EcoCyc protein note: paoA encodes the α subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC; PaoA binds two [2Fe-2S] clusters . A paoA single deletion mutant is unable to grow in the presence of cinnamaldehyde at pH 4.0 . PaoA contains a twin arginine signal peptide for translocation to the periplasm .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77165|protein.P77165]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000992,ECOCYC:G6157,GeneID:945330`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:301884-302573:-; feature_type=gene
