---
entity_id: "gene.b0394"
entity_type: "gene"
name: "mak"
source_database: "NCBI RefSeq"
source_id: "gene-b0394"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0394"
  - "mak"
---

# mak

`gene.b0394`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0394`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mak (gene.b0394) is a gene entity. It encodes mak (protein.P23917). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of fructose to fructose-6-P. Also has low level glucokinase activity in vitro. Is not able to phosphorylate D-ribose, D-mannitol, D-sorbitol, inositol, and L-threonine. {ECO:0000269|PubMed:11742072, ECO:0000269|PubMed:15157072}. EcoCyc product frame: EG11288-MONOMER. EcoCyc synonyms: yajF. Genomic coordinates: 410144-411052. EcoCyc protein note: In the absence of the usual PTS-mediated route of fructose uptake, a selected mutation that causes increased expression of Mak enables phosphorylation of fructose after its facilitated diffusion into the cell via a selected mutant allele of PTSG-MONOMER PtsG . The Mak enzyme appears to be identical to the previously reported mannokinase activity in E. coli. The enzyme was reported to be constitutively expressed and is able to phosphorylate mannose, fructose and to a lesser extent glucosamine, D-glucose and 2-deoxyglucose . Trace Mak activity is present in wild-type cells . Overexpression of mak rescues the glucose auxotrophy of a glucokinase mutant, and the Mak protein functions as a rudimentary glucokinase in vitro...

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23917|protein.P23917]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001372,ECOCYC:EG11288,GeneID:949086`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:410144-411052:+; feature_type=gene
