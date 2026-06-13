---
entity_id: "gene.b0285"
entity_type: "gene"
name: "paoB"
source_database: "NCBI RefSeq"
source_id: "gene-b0285"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0285"
  - "paoB"
---

# paoB

`gene.b0285`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0285`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paoB (gene.b0285) is a gene entity. It encodes paoB (protein.P77324). Encoded protein function: FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. EcoCyc product frame: G6156-MONOMER. EcoCyc synonyms: yagS. Genomic coordinates: 300931-301887. EcoCyc protein note: paoB encodes the β subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC; PaoB binds a [4Fe-4S] cluster and is the FAD-containing subunit .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77324|protein.P77324]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000990,ECOCYC:G6156,GeneID:945710`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:300931-301887:-; feature_type=gene
