---
entity_id: "gene.b0568"
entity_type: "gene"
name: "nfrA"
source_database: "NCBI RefSeq"
source_id: "gene-b0568"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0568"
  - "nfrA"
---

# nfrA

`gene.b0568`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0568`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfrA (gene.b0568) is a gene entity. It encodes nfrA (protein.P31600). Encoded protein function: FUNCTION: (Microbial infection) Allows N4 phage attachment by binding to the viral non-contractile sheath protein. {ECO:0000269|PubMed:19011026}. EcoCyc product frame: EG11740-MONOMER. Genomic coordinates: 587982-590954. EcoCyc protein note: NfrA is an outer membrane protein required for the secretion of an uncharacterized exopolysaccharide (termed N4 glycan receptor or NGR) that impedes flagellar activity and serves as the primary receptor for lytic bacteriophage N4 . nfrA is located together with EG11739 nfrB, encoding a C-DI-GMP-activated glycosyltransferase, and EG12448 ybcH encoding a periplasmic protein, and the three proteins likely constitute an exopolysaccharide production/secretion system . Early studies characterized nfrA mutations which conferred N4 resistance in E. coli K-12 strain SC1100 . Sequence analysis indicates that it contains no significant hydrophobic regions apart from the signal peptide, and no significant β-sheet structure . NfrA is predicted to be an outer membrane, TPR-rich, β-barrel protein . NfrA (E. coli K-12 strain W3350) interacts physically with phage N4 tail sheath protein gp65 in vitro and in vivo . NfrA binds human complement component C3 in vitro; NfrA is implicated in a pathway of glycine-promoted, complement-dependent, cell death...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31600|protein.P31600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001939,ECOCYC:EG11740,GeneID:944741`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:587982-590954:-; feature_type=gene
