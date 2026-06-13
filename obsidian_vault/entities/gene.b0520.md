---
entity_id: "gene.b0520"
entity_type: "gene"
name: "ylbF"
source_database: "NCBI RefSeq"
source_id: "gene-b0520"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0520"
  - "ylbF"
---

# ylbF

`gene.b0520`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0520`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ylbF (gene.b0520) is a gene entity. It encodes allH (protein.P0AAS5). Encoded protein function: FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:38888336}. EcoCyc product frame: G6289-MONOMER. EcoCyc synonyms: ylbF. Genomic coordinates: 549627-550442. EcoCyc protein note: Using genome and metabolic context methods, ylbF is predicted to encode an oxamate carbamoyltransferase that is active in the PWY0-41 "anaerobic allantoin degradation pathway" . Using mutational analyses and purified proteins, this gene product, renamed AllH, was shown to be required for oxamate carbamoyltransferase (OXTCase) activity along with AllF and AllG subunits . The complex of three distinct subunits has not been observed for other enzymes of the transcarbamylase family in other organisms; also, the protein sequences for all three enzymes lack similarity to others in the transcarbamylase family .

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAS5|protein.P0AAS5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001789,ECOCYC:G6289,GeneID:945195`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:549627-550442:+; feature_type=gene
