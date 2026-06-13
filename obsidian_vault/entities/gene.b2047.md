---
entity_id: "gene.b2047"
entity_type: "gene"
name: "wcaJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2047"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2047"
  - "wcaJ"
---

# wcaJ

`gene.b2047`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2047`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wcaJ (gene.b2047) is a gene entity. It encodes wcaJ (protein.P71241). Encoded protein function: FUNCTION: Is the initiating enzyme for colanic acid (CA) synthesis. Catalyzes the transfer of the glucose-1-phosphate moiety from UDP-Glc onto the carrier lipid undecaprenyl phosphate (C55-P), forming a phosphoanhydride bond yielding to glucosyl-pyrophosphoryl-undecaprenol (Glc-PP-C55). Also possesses a weak galactose-1-P transferase activity. {ECO:0000269|PubMed:22408159}. EcoCyc product frame: G7098-MONOMER. Genomic coordinates: 2120160-2121554. EcoCyc protein note: WcaJ belongs to the polyisoprenyl-phosphate hexose-1-phosphate transferase (PHPT) family and catalyzes the transfer of glucose-1-phosphate from UDP-glucose to undecaprenyl-phosphate , which is the initial step of colanic acid biosynthesis in E. coli . WcaJ was predicted to catalyze this reaction based on sequence similarity and its presence in a colanic acid biosynthesis operon . Experimental validation led to a revision of the predicted membrane topology of WcaJ and the PHPT family of enzymes. The enzyme comprises four canonical transmembrane helices followed by a cytoplasmic loop and an additional membrane domain that adopts a helix-break-helix structure that does not span the membrane, thus leading to cytoplasmic localization of the C terminus...

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71241|protein.P71241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006785,ECOCYC:G7098,GeneID:946583`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2120160-2121554:-; feature_type=gene
