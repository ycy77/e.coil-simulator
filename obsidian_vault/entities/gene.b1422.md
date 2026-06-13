---
entity_id: "gene.b1422"
entity_type: "gene"
name: "ydcI"
source_database: "NCBI RefSeq"
source_id: "gene-b1422"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1422"
  - "ydcI"
---

# ydcI

`gene.b1422`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1422`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcI (gene.b1422) is a gene entity. It encodes ydcI (protein.P77171). Encoded protein function: FUNCTION: Transcription factor involved in pH homeostasis and acetate metabolism (PubMed:30137486). It is required to maintain physiological activity at acidic/alkaline conditions (PubMed:30137486). It is also involved in regulating the carbon flux in the TCA cycle (PubMed:30137486). It affects, direct or indirectly, the expression of about 60 genes (PubMed:32419108). The vast majority (almost all) of the genes of the YdcI regulon in both log and stationary are small genes (less than 800 bp) encoding small proteins, sRNA or pseudogenes (PubMed:32419108). The transcriptional factor binding sites (TFBS) of YdcI enclose AT-rich inverted repeats separated by 7-nt (PubMed:30137486). {ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:32419108}. EcoCyc product frame: G6737-MONOMER. Genomic coordinates: 1494148-1495071. EcoCyc protein note: Based on results with purified YdcI protein with a DNA probe in a gel shift assay, YdcI was shown to be a DNA-binding transcriptional repressor which negatively regulates its own expression in Salmonella enterica serovar Typhimurium . YdcI was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77171|protein.P77171]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydcI; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004746,ECOCYC:G6737,GeneID:948865`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1494148-1495071:-; feature_type=gene
