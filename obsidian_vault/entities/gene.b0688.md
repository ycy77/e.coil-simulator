---
entity_id: "gene.b0688"
entity_type: "gene"
name: "pgm"
source_database: "NCBI RefSeq"
source_id: "gene-b0688"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0688"
  - "pgm"
---

# pgm

`gene.b0688`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0688`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgm (gene.b0688) is a gene entity. It encodes pgm (protein.P36938). Encoded protein function: FUNCTION: This enzyme participates in both the breakdown and synthesis of glucose. {ECO:0000269|PubMed:14216423}. EcoCyc product frame: PHOSPHOGLUCMUT-MONOMER. EcoCyc synonyms: blu. Genomic coordinates: 713558-715198. EcoCyc protein note: Phosphoglucomutase is involved in the breakdown of glycogen and metabolism of galactose and maltose. Pgm forms a complex with GLU6PDEHYDROG-MONOMER, which uses the product of Pgm, GLC-1-P, to produce D-6-P-GLUCONO-DELTA-LACTONE . Phosphoglucomutase was found to be a modulator of chromosomal supercoiling. Its role in mediating chromosome topology may be indirect . pgm mutants are thought to accumulate maltodextrin due to reversal of the reaction catalyzed by MALDEXPHOSPHORYL-CPLX, leading to the Blu phenotype (blue color when stained with iodine) . Amylose begins to accumulate when the pgm expression level is below 10% of wild type levels . In a genome-wide screen of single-gene knockout mutants of E. coli K-12 (the Keio collection), a pgm mutant was shown to be defective in swarming and swimming ability, as expected for the role of this enzyme in energy production...

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36938|protein.P36938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002345,ECOCYC:EG12144,GeneID:945271`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:713558-715198:+; feature_type=gene
