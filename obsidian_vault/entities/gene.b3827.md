---
entity_id: "gene.b3827"
entity_type: "gene"
name: "bioP"
source_database: "NCBI RefSeq"
source_id: "gene-b3827"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3827"
  - "bioP"
---

# bioP

`gene.b3827`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3827`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioP (gene.b3827) is a gene entity. It encodes bioP (protein.P0ADP5). Encoded protein function: FUNCTION: Uptake of biotin. Acts probably by facilitated diffusion. {ECO:0000269|Ref.5}. EcoCyc product frame: EG11471-MONOMER. EcoCyc synonyms: yigM. Genomic coordinates: 4011076-4011975. EcoCyc protein note: YigM is a biotin transporter in E. coli K-12 The uptake of labeled biotin is abolished in an E. coli ΔyigM strain (Keio collection strain K-12 BW25113); overexpression of YigM results in increased biotin uptake in both the wild type and in a ΔyigM strain; uptake assays in whole cells and in membrane vesicles suggest biotin is taken up by facilitated diffusion . Biotin transport in E. coli K-12 (strains Y10-1 and 54117-Pasteur collection) is an active process and is inhibited by uncouplers . Biotin transport is regulated by the concentration of biotin in the medium with reduced transport at higher biotin concentrations . Biotinylated peptides up to 31 amino acids long can be taken up by E. coli through the biotin transport system . YigM is predicted to contain 10 transmembrane domains with the C and N-termini located in the cytoplasm . Expression of a yigM promoter reporter decreases with increasing concentration of biotin; a putative truncated BirA binding site is located in the promoter region of YigM . yigM may have a σ54-dependent promoter...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADP5|protein.P0ADP5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012504,ECOCYC:EG11471,GeneID:948309`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4011076-4011975:+; feature_type=gene
