---
entity_id: "gene.b0239"
entity_type: "gene"
name: "frsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0239"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0239"
  - "frsA"
---

# frsA

`gene.b0239`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0239`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frsA (gene.b0239) is a gene entity. It encodes frsA (protein.P04335). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of esters (PubMed:15808744). Displays esterase activity toward pNP-butyrate (PubMed:15808744). May stimulate mixed-acid fermentation by acting as a fermentation/respiration switch that down-regulates respiration and up-regulates fermentation rates (PubMed:15169777). {ECO:0000269|PubMed:15169777, ECO:0000269|PubMed:15808744}. EcoCyc product frame: EG11091-MONOMER. EcoCyc synonyms: yafA. Genomic coordinates: 256527-257771. EcoCyc protein note: The FrsA protein was found to bind specifically to the unphosphorylated form of enzyme IIAGlc of the PEP-sugar phosphotransferase system and is suggested to aid IIAGlc in regulating the flux between respiration and fermentation pathways . Esterase activity of FrsA was discovered in a high-throughput screen of purified proteins . FrsA from Vibrio vulnificus is a pyruvate decarboxylase . Mutation of the frsA gene results in increased respiration on sugars including glucose. Overexpression of FrsA, on the other hand, results in increased fermentation of these sugars, leading to the accumulation of mixed-acid fermentation products . Orthologs of the frsA gene have so far only been found in facultative anaerobes belonging to the γ proteobacteria . FrsA: "fermentation/respiration switch protein"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04335|protein.P04335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000817,ECOCYC:EG11091,GeneID:946039`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:256527-257771:+; feature_type=gene
