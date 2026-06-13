---
entity_id: "gene.b0454"
entity_type: "gene"
name: "ybaZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0454"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0454"
  - "ybaZ"
---

# ybaZ

`gene.b0454`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0454`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaZ (gene.b0454) is a gene entity. It encodes atl (protein.P0AFP2). Encoded protein function: FUNCTION: Involved in DNA damage recognition. Binds DNA containing O(6)-methylguanine and larger O(6)-alkylguanine adducts, and to double-stranded DNA that contains an AP (apurinic/apyrimidinic) site (PubMed:16027108, PubMed:18084297, PubMed:19269902, PubMed:20921378). Binds to the damaged base and flips the base out of the DNA duplex into an extrahelical conformation, which allows processing by repair proteins (PubMed:18084297). Works in partnership with the nucleotide excision repair (NER) pathway to enhance the repair of the O(6)-alkylguanine adducts larger than the methyl adduct (PubMed:19269902, PubMed:20921378). Also prevents methyl-directed mismatch repair (MMR)-mediated attack of the O(6)-alkylguanine:T mispairs for the larger alkyl groups (PubMed:20921378). {ECO:0000269|PubMed:16027108, ECO:0000269|PubMed:18084297, ECO:0000269|PubMed:19269902, ECO:0000269|PubMed:20921378}. EcoCyc product frame: G6251-MONOMER. EcoCyc synonyms: atl. Genomic coordinates: 475982-476371...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFP2|protein.P0AFP2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001576,ECOCYC:G6251,GeneID:945094`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:475982-476371:-; feature_type=gene
