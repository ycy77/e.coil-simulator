---
entity_id: "gene.b2888"
entity_type: "gene"
name: "uacT"
source_database: "NCBI RefSeq"
source_id: "gene-b2888"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2888"
  - "uacT"
---

# uacT

`gene.b2888`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2888`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uacT (gene.b2888) is a gene entity. It encodes uacT (protein.Q46821). Encoded protein function: FUNCTION: Proton-dependent high-capacity transporter for uric acid. Also shows a low capacity for transport of xanthine at 37 degrees Celsius but not at 25 degrees Celsius. {ECO:0000269|PubMed:22437829}. EcoCyc product frame: YGFU-MONOMER. EcoCyc synonyms: ygfU. Genomic coordinates: 3031367-3032815. EcoCyc protein note: UacT is low affinity, high capacity urate transporter in E.coli K-12. Over-expression of uacT from a plasmid results in uptake of labelled urate to high levels. Uptake is abolished by the addition of the protonophore, carbonyl cyanide m-chlorophenyl hydrazaone . UacT also transports xanthine but with low affinity and low capacity . UacT contains 10 transmembrane helices plus 4 smaller helical segments within the membrane; the amino and carboxy termini are located in the cytoplasm . Amino acid residues critical for function have been identified; threonine at position 100 is essential for uric acid specificity . The physiological significance of urate uptake is uncertain since no enzyme for the further catabolism of urate has been identified in E. coli . UacT is a member of the NCS2 family of nucleobase transporters. UacT: uric acid transporter

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46821|protein.Q46821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009478,ECOCYC:G7507,GeneID:949017`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3031367-3032815:+; feature_type=gene
