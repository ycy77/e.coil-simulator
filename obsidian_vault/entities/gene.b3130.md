---
entity_id: "gene.b3130"
entity_type: "gene"
name: "yhaV"
source_database: "NCBI RefSeq"
source_id: "gene-b3130"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3130"
  - "yhaV"
---

# yhaV

`gene.b3130`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3130`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhaV (gene.b3130) is a gene entity. It encodes yhaV (protein.P64594). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. Has RNase activity in vitro. Overexpression leads to growth arrest after 30 minutes; these effects are overcome by concomitant expression of antitoxin SohA (PrlF). Massive overexpression is toxic. Unlike most other characterized TA systems degrades rRNA, and co-folding of the both TA proteins is necessary in vitro for inhibition of the RNase activity. It is not known if it has any sequence-specificity. Acts as a transcription factor. The YhaV/PrlF complex binds the prlF-yhaV operon, probably negatively regulating its expression. {ECO:0000269|PubMed:17706670}. EcoCyc product frame: G7629-MONOMER. Genomic coordinates: 3277337-3277801. EcoCyc protein note: YhaV is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems and the ribonuclease toxin component of the YhaV-PrlF toxin-antitoxin system . The ribonuclease activity of YhaV is dependent on the presence of the ribosome . YhaV associates with the 70S ribosome and the 50S ribosomal subunit in a ribosomal profiling assay . Residues 131-145 at the C terminus of YhaV are involved in its mRNA interferase activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64594|protein.P64594]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010289,ECOCYC:G7629,GeneID:947638`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3277337-3277801:+; feature_type=gene
