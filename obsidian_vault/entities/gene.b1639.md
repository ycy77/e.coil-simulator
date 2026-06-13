---
entity_id: "gene.b1639"
entity_type: "gene"
name: "mliC"
source_database: "NCBI RefSeq"
source_id: "gene-b1639"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1639"
  - "mliC"
---

# mliC

`gene.b1639`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1639`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mliC (gene.b1639) is a gene entity. It encodes mliC (protein.P28224). Encoded protein function: FUNCTION: Specifically inhibits C-type lysozymes. {ECO:0000269|PubMed:18369469}. EcoCyc product frame: EG11488-MONOMER. EcoCyc synonyms: ydhA. Genomic coordinates: 1718066-1718395. EcoCyc protein note: The MliC protein inhibits activity of c-type lysozyme in vitro. In cells that are sensitized to hen egg white lysozyme (HEWL), overexpression of MliC suppresses growth inhibition by HEWL. MliC is predicted to be a lipoprotein that is anchored to the periplasmic side of the outer membrane; activity is found in the membrane fraction . A solution structure of MliC has been determined, showing an eight-stranded β-barrel . An mliC (ORF1) insertion mutation has no detectable phenotype, and no expression was detected in exponentially growing cells . Overexpression of mliC suppresses the essentiality of EG12691-MONOMER "lapB", which encodes a protein involved in lipopolysaccharide (LPS) assembly . MliC: "membrane-bound lysozyme inhibitor of c-type lysozyme"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28224|protein.P28224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005485,ECOCYC:EG11488,GeneID:946811`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1718066-1718395:-; feature_type=gene
