---
entity_id: "gene.b0228"
entity_type: "gene"
name: "rayT"
source_database: "NCBI RefSeq"
source_id: "gene-b0228"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0228"
  - "rayT"
---

# rayT

`gene.b0228`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0228`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rayT (gene.b0228) is a gene entity. It encodes rayT (protein.Q47152). Encoded protein function: FUNCTION: Transposase that is always flanked by repeated extragenic palindrome (REP) sequences, which are clustered in structures called bacterial interspersed mosaic elements (BIMEs). RayT catalyzes cleavage and recombination of BIMEs. Binds REP sequences and cleaves BIMEs both upstream and downstream of the REP sequence. Could be important in the creation of BIME variability and amplification. {ECO:0000269|PubMed:20085626, ECO:0000269|PubMed:22199259, ECO:0000269|PubMed:22885300}. EcoCyc product frame: G6112-MONOMER. EcoCyc synonyms: yafM. Genomic coordinates: 247637-248134. EcoCyc protein note: TnpAREP (RayT) is closely related to IS200/IS605 transposases and is associated with a repetitive extragenic palindromic (REP) sequence . It catalyzes cleavage and recombination of bacterial interspersed mosaic elements (BIMEs) in vitro . TnpAREP binds single-stranded REP sequences containing the conserved 5' GATG tetranucleotide and catalyzes BIME cleavage both upstream and downstream of the REP sequence . A crystal structure of TnpAREP bound to a REP has been solved at 2.6 Å resolution. Unlike the IS200/IS605 transposases, TnpAREP is momoneric and specifically requires Mn2+ for cleavage and the formation of a covalent intermediate . RayT: "REP-associated tyrosine transposase"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47152|protein.Q47152]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000779,ECOCYC:G6112,GeneID:944913`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:247637-248134:+; feature_type=gene
