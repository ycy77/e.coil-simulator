---
entity_id: "gene.b1872"
entity_type: "gene"
name: "torZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1872"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1872"
  - "torZ"
---

# torZ

`gene.b1872`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1872`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torZ (gene.b1872) is a gene entity. It encodes torZ (protein.P46923). Encoded protein function: FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. Can also reduce other N- and S-oxide compounds such as 4-methylmorpholine-N-oxide and biotin sulfoxide (BSO), but with a lower catalytic efficiency. {ECO:0000269|PubMed:11004177}. EcoCyc product frame: G7022-MONOMER. EcoCyc synonyms: bisZ. Genomic coordinates: 1954578-1957007. EcoCyc protein note: The periplasmic oxidoreductase TorZ and pentaheme c-type cytochrome G7023-MONOMER "TorY" constitute an anaerobic respiratory system that can use several N and S-oxides, including trimethylamine n--oxide (TMAO) and biotin sulfoxide (BSO) as terminal electron acceptors . TorZ (formerly BisZ) is responsible for the small amount of biotin-d-sulfoxide (BDS) reductase activity that is present in a strain lacking EG10124-MONOMER; torZ encodes a putative molybdoenzyme . Overexpression of torYZ allows anaerobic TMAO respiration in a strain (torC2::ΩSpcrΔdms Kmr) that otherwise grows extremely slowly with TMAO as terminal oxidant . TMAO and 4-methylmorpholine are good substrates in vitro; BSO, tetramethylene sulfoxide and DL-methionine sulfoxide are reduced less efficiently and DMSO acts as a competitive inhibitor . TorZ is exported to the periplasm via the Tat pathway...

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46923|protein.P46923]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006244,ECOCYC:G7022,GeneID:946389`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1954578-1957007:-; feature_type=gene
