---
entity_id: "gene.b1120"
entity_type: "gene"
name: "cobB"
source_database: "NCBI RefSeq"
source_id: "gene-b1120"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1120"
  - "cobB"
---

# cobB

`gene.b1120`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1120`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cobB (gene.b1120) is a gene entity. It encodes cobB (protein.P75960). Encoded protein function: FUNCTION: NAD-dependent lysine deacetylase that specifically removes acetyl groups on target proteins. Also acts as a protein-lysine deacylase by mediating protein desuccinylation and de-2-hydroxyisobutyrylation. Modulates the activities of several proteins which are inactive in their acylated form. Activates the enzyme acetyl-CoA synthetase (acs) by deacetylating 'Lys-609' in the inactive, acetylated form of the enzyme. May also modulate the activity of other propionyl-adenosine monophosphate (AMP)-forming enzymes. {ECO:0000255|HAMAP-Rule:MF_01121, ECO:0000269|PubMed:10811920, ECO:0000269|PubMed:15019790, ECO:0000269|PubMed:24176774, ECO:0000269|PubMed:30274179, ECO:0000269|PubMed:31328167}. EcoCyc product frame: MONOMER0-4534. EcoCyc synonyms: ycfY. Genomic coordinates: 1179520-1180359. EcoCyc protein note: The shorter CobB-S isoform is produced by translation initiation at an alternative start codon in a transcript that is apparently created by use of an alternative promoter . The N-terminal domain which is only present in the G6577-MONOMER CobB-L isoform appears to be required for dimerization .

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75960|protein.P75960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003781,ECOCYC:G6577,GeneID:945687`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1179520-1180359:+; feature_type=gene
