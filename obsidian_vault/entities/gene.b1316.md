---
entity_id: "gene.b1316"
entity_type: "gene"
name: "ycjT"
source_database: "NCBI RefSeq"
source_id: "gene-b1316"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1316"
  - "ycjT"
---

# ycjT

`gene.b1316`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1316`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycjT (gene.b1316) is a gene entity. It encodes ycjT (protein.P77154). Encoded protein function: FUNCTION: In vitro catalyzes the phosphorolysis of D-kojibiose into beta-D-glucose 1-phosphate and D-glucose. No other disaccharides tested substitute for D-kojibiose. In the reverse direction disaccharides can be formed from beta-D-glucose 1-phosphate plus D-glucose, L-sorbose, D-sorbitol, L-iditol or 1,5-anhydro-D-glucitol, but with low efficiency. The beta-D-glucose 1-phosphate product is the substrate for YcjU (AC P77366), the next apparent enzyme in the putative biochemical pathway encoded in this locus (yjcM to ycjW). {ECO:0000269|PubMed:29684280}. EcoCyc product frame: G6654-MONOMER. Genomic coordinates: 1377884-1380151. EcoCyc protein note: YcjT was shown to have kojibiose phosphorylase activity in vitro. However, neither the E. coli K-12 strain BW25113 nor the B strain BL21(DE3) is able to grow on D-kojibiose as the sole source of carbon and energy . YcjT shows sequence similarity to maltose phosphorylase from Lactobacillus sanfranciscensis. A ycjT null mutant does not affect growth on maltose .

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77154|protein.P77154]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ycjT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004418,ECOCYC:G6654,GeneID:945895`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1377884-1380151:+; feature_type=gene
