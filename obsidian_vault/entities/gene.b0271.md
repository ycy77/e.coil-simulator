---
entity_id: "gene.b0271"
entity_type: "gene"
name: "yagH"
source_database: "NCBI RefSeq"
source_id: "gene-b0271"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0271"
  - "yagH"
---

# yagH

`gene.b0271`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0271`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yagH (gene.b0271) is a gene entity. It encodes yagH (protein.P77713). Encoded protein function: Putative beta-xylosidase (EC 3.2.1.37) (1,4-beta-D-xylan xylohydrolase) (Xylan 1,4-beta-xylosidase) EcoCyc product frame: G6143-MONOMER. Genomic coordinates: 286789-288399. EcoCyc protein note: YagH is a member of the glycosyl hydrolase family 43 with predicted β-xylosidase activity . yagGH is predicted to be a member of the EG20253-MONOMER "XylR" regulon; its products may mediate transport (YagG) and hydrolysis (YagH) of xylooligosaccharides; putative XylR and CRP binding sites are identified upstream of yagGH Based on the anomalous codon usage pattern and GC content, the yagH gene originates from a horizontal gene transfer event; the gene lies within the CP4-6 prophage .

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77713|protein.P77713]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000931,ECOCYC:G6143,GeneID:944949`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:286789-288399:+; feature_type=gene
