---
entity_id: "gene.b1528"
entity_type: "gene"
name: "ydeA"
source_database: "NCBI RefSeq"
source_id: "gene-b1528"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1528"
  - "ydeA"
---

# ydeA

`gene.b1528`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1528`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeA (gene.b1528) is a gene entity. It encodes sotB (protein.P31122). Encoded protein function: FUNCTION: Involved in the efflux of sugars. The physiological role may be the reduction of the intracellular concentration of toxic sugars or sugar metabolites. Transports L-arabinose and to a lesser extent IPTG. Seems to contribute to the control of the arabinose regulon. EcoCyc product frame: YDEA-MONOMER. Genomic coordinates: 1617028-1618218. EcoCyc protein note: YdeA is a member of the major facilitator superfamily (MFS) of transporters . Overexpression of ydeA interferes with the intracellular accumulation of arabinose and this effect is dependent on the proton motive force; mutational activation of the ydeA promoter inhibits activation of the arabinose-inducible PBAD promoter (see also ). Deletion of ydeA (in strain MG1655) does not affect the intracellular concentration of arabinose; overexpression of ydeA reduces the intracellular concentration of arabinose; expression of ydeA is induced by arabinose . YdeA may function to limit the acumulation of toxic sugar phosphates . Crystal structures of YdeA (from E. coli strain BL21) in different conformations have been determined and are informative of the alternating access mechanism of transport . Overexpression of cloned ydeA in a K-12 strain which lacks the major efflux pump permease AcrB (E...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31122|protein.P31122]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005103,ECOCYC:EG11636,GeneID:947218`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1617028-1618218:+; feature_type=gene
