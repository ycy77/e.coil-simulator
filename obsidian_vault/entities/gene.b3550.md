---
entity_id: "gene.b3550"
entity_type: "gene"
name: "yiaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3550"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3550"
  - "yiaC"
---

# yiaC

`gene.b3550`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3550`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaC (gene.b3550) is a gene entity. It encodes yiaC (protein.P37664). Encoded protein function: FUNCTION: N-epsilon-lysine acetyltransferase that catalyzes acetylation of a large number of proteins. Overexpression inhibits motility. {ECO:0000269|PubMed:30352934}. EcoCyc product frame: EG12270-MONOMER. Genomic coordinates: 3713652-3714092. EcoCyc protein note: YiaC is an Nε-lysine acetyltransferase that targets 391 unique lysine residues in 251 proteins . Overexpression of YiaC in an acetylation-gutted strain (ΔEG20173 G7350 EG11448 G6577) leads to the appearance of acetylated proteins in an anti-acetyllysine Western blot. Mutagenesis of a predicted catalytic residue in YiaC, Y115A, eliminates the acetylation signal observed with the wild-type protein . YiaC was the only GCN5-related N-acetyltransferase (GNAT) family protein that resulted in lactylation of lysines when overexpressed, as measured in whole E. coli cell lysates by immunoblotting with a pan-lysine lactylation (Kla) antibody. ΔyiaC experiments confirmed the lactylation by YiaC and found over 1000 unique lysine sites in 478 proteins. Kinetic analysis found that YiaC has strong binding affinity to both lactyl-CoA, formed by EG12432-MONOMER, and to acetyl-CoA (KD = 6.83 and 5.57, respectively) but did not bind to succinyl-CoA. YiaC's lactylation activity was found to be more efficient than its acetylation activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37664|protein.P37664]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011595,ECOCYC:EG12270,GeneID:946460`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3713652-3714092:+; feature_type=gene
