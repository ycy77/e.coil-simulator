---
entity_id: "gene.b0452"
entity_type: "gene"
name: "tesB"
source_database: "NCBI RefSeq"
source_id: "gene-b0452"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0452"
  - "tesB"
---

# tesB

`gene.b0452`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0452`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tesB (gene.b0452) is a gene entity. It encodes tesB (protein.P0AGG2). Encoded protein function: FUNCTION: Thioesterase that has relatively broad substrate specificity, hydrolyzing primarily medium- and long-chain acyl-CoA substrates to free fatty acids and CoA (PubMed:1645722, PubMed:20547355, PubMed:24271180). Functions in the thioesterase-dependent pathway of beta-oxidation of oleate and conjugated linoleate ((9Z,11E)-octadecadienoate or CLA), which provides all energy and carbon precursors required for the growth of E.coli. Thus, supports growth on oleate or conjugated linoleate as the sole source of carbon by hydrolyzing 3,5-tetradecadienoyl-CoA, the terminal metabolite of oleate beta-oxidation via the alternative thioesterase-dependent pathway, and 3,5-dodecadienoyl-CoA, the end product of CLA beta-oxidation, respectively (PubMed:14707139, PubMed:18702504). Seems to be involved in 3-hydroxyalkanoate production in E.coli (PubMed:20547355). {ECO:0000269|PubMed:14707139, ECO:0000269|PubMed:1645722, ECO:0000269|PubMed:18702504, ECO:0000269|PubMed:20547355, ECO:0000269|PubMed:24271180}. EcoCyc product frame: THIOESTERII-MONOMER. Genomic coordinates: 474301-475161. EcoCyc protein note: Thioesterase II (TesB) is one of a number of thioesterases present in E. coli. The enzyme has relatively broad substrate specificity, cleaving medium- and long-chain acyl-CoA substrates...

## Enriched Pathways

- `eco01040` Biosynthesis of unsaturated fatty acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGG2|protein.P0AGG2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001566,ECOCYC:EG10995,GeneID:945074`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:474301-475161:-; feature_type=gene
