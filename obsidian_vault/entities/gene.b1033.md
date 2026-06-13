---
entity_id: "gene.b1033"
entity_type: "gene"
name: "ghrA"
source_database: "NCBI RefSeq"
source_id: "gene-b1033"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1033"
  - "ghrA"
---

# ghrA

`gene.b1033`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1033`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ghrA (gene.b1033) is a gene entity. It encodes ghrA (protein.P75913). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of glyoxylate and hydroxypyruvate into glycolate and glycerate, respectively. Inactive towards 2-oxo-D-gluconate, 2-oxoglutarate, oxaloacetate and pyruvate. Only D- and L-glycerate are involved in the oxidative activity with NADP. Activity with NAD is very low. EcoCyc product frame: G6539-MONOMER. EcoCyc synonyms: ycdW. Genomic coordinates: 1097886-1098824. EcoCyc protein note: GhrA is one of two enzymes with glyoxylate reductase activity. GhrA prefers NADPH as the electron donor and also catalyzes reduction of hydroxypyruvate, although at lower catalytic efficiency. In contrast, the ghrB-encoded enzyme prefers hydroxypyruvate as the substrate . Expression of ghrA is slightly increased by growth on medium containing hydroxypyruvate . ghrA was one of only three genes whose expression changed under all stress conditions tested by . Inactivation of ghrA was investigated as a means to improve production of 1,2,4-butanetriol in a metabolically engineered strain .

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75913|protein.P75913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003503,ECOCYC:G6539,GeneID:946431`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1097886-1098824:+; feature_type=gene
