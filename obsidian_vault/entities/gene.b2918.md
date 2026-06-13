---
entity_id: "gene.b2918"
entity_type: "gene"
name: "argK"
source_database: "NCBI RefSeq"
source_id: "gene-b2918"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2918"
  - "argK"
---

# argK

`gene.b2918`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2918`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argK (gene.b2918) is a gene entity. It encodes argK (protein.P27254). Encoded protein function: FUNCTION: Binds and hydrolyzes GTP (PubMed:18950999). Likely functions as a G-protein chaperone that assists AdoCbl cofactor delivery to the methylmalonyl-CoA mutase (MCM) ScpA and reactivation of the enzyme during catalysis. {ECO:0000269|PubMed:18950999, ECO:0000305}. EcoCyc product frame: EG11445-MONOMER. EcoCyc synonyms: ygfD. Genomic coordinates: 3062987-3063982. EcoCyc protein note: YgfD is a member of the G3E family of P-loop GTPases . The YgfD protein and CPLX0-7741 (encoded upstream of YgfD) interact both in vivo and in vitro; detection of the interaction depends on the presence of a non-hydrolyzable GTP analog . YgfD was first identified as an ATPase, ArgK, that appeared to phosphorylate the periplasmic binding proteins of the lysine, arginine, ornithine transport system as well as the arginine, ornithine transport system . However, the kinase activity of ArgK did not affect transport activity . Neither the molecular weight nor the pI of ArgK are similar to that of the protein kinase that was purified based on its activity . Overexpression of YgfD contributes to increased production of 1-propanol in an engineered E. coli strain .

## Enriched Pathways

- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27254|protein.P27254]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009579,ECOCYC:EG11445,GeneID:947412`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3062987-3063982:+; feature_type=gene
