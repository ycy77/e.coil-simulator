---
entity_id: "gene.b3032"
entity_type: "gene"
name: "cpdA"
source_database: "NCBI RefSeq"
source_id: "gene-b3032"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3032"
  - "cpdA"
---

# cpdA

`gene.b3032`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3032`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpdA (gene.b3032) is a gene entity. It encodes cpdA (protein.P0AEW4). Encoded protein function: FUNCTION: Hydrolyzes cAMP to 5'-AMP. Plays an important regulatory role in modulating the intracellular concentration of cAMP, thereby influencing cAMP-dependent processes. Specific for cAMP. {ECO:0000255|HAMAP-Rule:MF_00905, ECO:0000269|PubMed:8810311}. EcoCyc product frame: G7579-MONOMER. EcoCyc synonyms: icc. Genomic coordinates: 3176006-3176833. EcoCyc protein note: cAMP phosphodiesterase hydrolyzes the important regulatory molecule cAMP and may thus influence the level of transcription of genes regulated by cAMP-CRP . Usage of the unusual translation start codon UUG has been confirmed by amino-terminal sequencing of the purified protein and may be involved in translational regulation of CpdA expression . CpdA is the founding member of the Class III family of 3',5'-cyclic nucleotide phosphodiesterases . Expression of CpdA appears to be itself catabolite-repressed . A cpdA mutant has slightly increased intracellular levels of cAMP . Overexpression of cpdA leads to increased resistance to hypochlorous acid stress due to derepression of rpoS and to increased persister cell formation due to reduced indole production...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEW4|protein.P0AEW4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009957,ECOCYC:G7579,GeneID:947515`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3176006-3176833:-; feature_type=gene
