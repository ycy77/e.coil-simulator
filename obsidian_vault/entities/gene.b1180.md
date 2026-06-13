---
entity_id: "gene.b1180"
entity_type: "gene"
name: "ycgM"
source_database: "NCBI RefSeq"
source_id: "gene-b1180"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1180"
  - "ycgM"
---

# ycgM

`gene.b1180`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1180`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgM (gene.b1180) is a gene entity. It encodes ycgM (protein.P76004). Encoded protein function: FUNCTION: Tautomerase that converts enol-oxaloacetate to the keto form of oxaloacetate. {ECO:0000269|PubMed:38287013}. EcoCyc product frame: G6617-MONOMER. Genomic coordinates: 1228079-1228738. EcoCyc protein note: This protein belongs to a highly conserved fumarylacetoacetate hydrolase domain (FAHD)-containing protein family that carries out oxaloacetate (OAA) tautomerase (OAT) activity, which can run in reverse to convert enol-OAA to keto-OAA, thus removing the enol-OAA inhibition of CPLX0-8160 (SDH) within the TCA . A ΔycgM mutant showed significant growth defects and small cell size phenotypes relative to wild-type strains, whereas a double mutant with the catalytic subunit, EG10931, resulted in a similar phenotype that was less severe because the SDH couldn't form the SDH inhibitor, enol-OAA. Metabolic profiling results are consistent with SDH inhibition of the TCA cycle and with YcgM being a metabolite repair enzyme .

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76004|protein.P76004]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003957,ECOCYC:G6617,GeneID:946115`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1228079-1228738:+; feature_type=gene
