---
entity_id: "gene.b1119"
entity_type: "gene"
name: "nagK"
source_database: "NCBI RefSeq"
source_id: "gene-b1119"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1119"
  - "nagK"
---

# nagK

`gene.b1119`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1119`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagK (gene.b1119) is a gene entity. It encodes nagK (protein.P75959). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of N-acetyl-D-glucosamine (GlcNAc) derived from cell-wall degradation, yielding GlcNAc-6-P. Has also low level glucokinase activity in vitro. {ECO:0000269|PubMed:15489439}. EcoCyc product frame: G6576-MONOMER. EcoCyc synonyms: ycfX. Genomic coordinates: 1178593-1179504. EcoCyc protein note: N-acetyl-D-glucosamine (GlcNAc) is released in the cytoplasm during murein recycling. NagK is the only known cytoplasmic GlcNAc kinase in E. coli . The enzyme was originally purified and studied by Asensio and Ruiz-Amil who reported a high affinity and specificity for GlcNAc, marginal activity on D-glucose and no detectable activity on D-glucosamine, N-methyl D-glucosamine, N-acetyl-D-mannosamine nor N-acetyl-D-galactosamine . Overexpression of nagK rescues the glucose auxotrophy of a glucokinase mutant, and the NagK protein functions as a rudimentary glucokinase in vitro . The Km of NagK for glucose is 100-fold higher than its Km for GlcNAc . Contrary to expectations, a nagK mutant does not accumulate GlcNAc in the cytoplasm, suggesting the presence of an additional pathway for GlcNAc utilization . The PTS transporter NagE was found to contribute to this pathway . nagK is expressed constitutively . NagK: "N-acetylglucosamine kinase" Review:

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75959|protein.P75959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003778,ECOCYC:G6576,GeneID:945664`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1178593-1179504:+; feature_type=gene
