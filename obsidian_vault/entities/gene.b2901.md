---
entity_id: "gene.b2901"
entity_type: "gene"
name: "bglA"
source_database: "NCBI RefSeq"
source_id: "gene-b2901"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2901"
  - "bglA"
---

# bglA

`gene.b2901`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2901`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglA (gene.b2901) is a gene entity. It encodes bglA (protein.Q46829). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin), with the exception of phosphorylated salicin, and a low affinity for phosphorylated beta-methyl-glucoside. Apparently, it has only a very limited role in the utilization of external beta-glucosides. {ECO:0000269|PubMed:4576407}. EcoCyc product frame: G495-MONOMER. EcoCyc synonyms: yqfC, bglD. Genomic coordinates: 3043662-3045101. EcoCyc protein note: BglA is a 6-phospho-β-glucosidase with a high affinity for phosphorylated aromatic β-glucosides and a low affinity for phosphorylated β-methyl-glucoside . BglA is one of several 6-phospho-β-glucosidases in E. coli; transporters for these compounds are present, but appear to be not expressed. Because its potential phosphorylated substrates are not commercially available, the true substrate range of BglA is unknown. Mutants that are able to utilize β-methyl-glucoside as the source of carbon and energy have increased levels of 6-phospho-β-glucosidase . A crystal structure of BglA has been solved at 2.3 Å resolution...

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46829|protein.Q46829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009523,ECOCYC:G495,GeneID:947378`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3043662-3045101:+; feature_type=gene
