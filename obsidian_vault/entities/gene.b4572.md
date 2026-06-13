---
entity_id: "gene.b4572"
entity_type: "gene"
name: "ylbE"
source_database: "NCBI RefSeq"
source_id: "gene-b4572"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4572"
  - "ylbE"
---

# ylbE

`gene.b4572`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4572`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ylbE (gene.b4572) is a gene entity. It encodes allG (protein.P77129). Encoded protein function: FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:38888336}. EcoCyc product frame: G6288-MONOMER. EcoCyc synonyms: b0519, G0-10554, b4507, ylbE. Genomic coordinates: 548357-549616. EcoCyc protein note: Resequencing of multiple isolates of the MG1655 strain has identified several genetic variations, including a single-nucleotide polymorphism and a single-nucleotide insertion in the former ylbE_1 pseudogene fragment in strain ATCC700926 , which is the source of the genome sequence within EcoCyc (U00096.3). This insertion repairs the frameshift and results in an intact ylbE gene . Using mutational analyses and purified proteins, this gene product, renamed AllG, was shown to be required for oxamate carbamoyltransferase (OXTCase) activity along with AllF and AllH subunits . The complex of three distinct subunits has not been observed for other enzymes of the transcarbamylase family in other organisms; also, the protein sequences for all three enzymes lack similarity to others in the transcarbamylase family...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77129|protein.P77129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0285105,ECOCYC:G6288,GeneID:4056025`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:548357-549616:+; feature_type=gene
