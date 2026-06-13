---
entity_id: "gene.b1985"
entity_type: "gene"
name: "yeeO"
source_database: "NCBI RefSeq"
source_id: "gene-b1985"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1985"
  - "yeeO"
---

# yeeO

`gene.b1985`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1985`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeeO (gene.b1985) is a gene entity. It encodes yeeO (protein.P76352). Encoded protein function: FUNCTION: A transporter able to export peptides and flavins. When overexpressed allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide, overproduction of this protein increases its export (PubMed:20067529). When overexpressed increases secretion of FMN and FAD but not riboflavin; intracellular concentrations of FMN and riboflavin rise, possibly to compensate for increased secretion (PubMed:25482085). Increased overexpression causes slight cell elongation (PubMed:25482085). {ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:25482085}. EcoCyc product frame: YEEO-MONOMER. Genomic coordinates: 2058203-2059846. EcoCyc protein note: YeeO belongs to the MATE (multi antimicrobial extrusion family or multidrug and toxic compound extrusion) family of transporters . E. coli K-12 (strain BW25113) naturally secretes flavins including riboflavin, flavin mononucleotide (FMN) and flavin adenine dinucleotide (FAD); overexpression of yeeO from a plasmid shifts the flavin secretion profile towards FMN and FAD...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76352|protein.P76352]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006586,ECOCYC:G7070,GeneID:946506`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2058203-2059846:-; feature_type=gene
