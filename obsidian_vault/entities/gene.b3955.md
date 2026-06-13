---
entity_id: "gene.b3955"
entity_type: "gene"
name: "eptC"
source_database: "NCBI RefSeq"
source_id: "gene-b3955"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3955"
  - "eptC"
---

# eptC

`gene.b3955`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3955`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eptC (gene.b3955) is a gene entity. It encodes eptC (protein.P0CB39). Encoded protein function: FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the outer membrane lipopolysaccharide core. {ECO:0000250}. EcoCyc product frame: EG11914-MONOMER. EcoCyc synonyms: yijP. Genomic coordinates: 4148532-4150265. EcoCyc protein note: EptC is required for the incorporation of phosphoethanolamine (P-EtN) onto the phosphorylated heptose I residue of E. coli K-12 lipopolysaccharide (LPS) . P-EtN modifications are absent on the LPS of E. coli grown under phosphate-rich conditions but are enriched in the LPS from growth under phosphate-limiting conditions . eptC deleted strains have severe growth defects in the presence of SDS (0.25% - 1%) and are more sensitive to Zn2+ than the wild-type . Transcription of an eptC-lacZ fusion is reduced 4-5 fold in a phoR deletion mutant and reduced 2-fold in a basR deletion mutant. Two putative PhoB binding sites are located in the promoter region of eptC . LPS from an E. coli strain lacking all three ept genes (eptA, eptB and eptC) does not contain any P-EtN modifications . EptC (formerly YijP) has similarity to YijP of Ecoli . K1, which is required for that strain to invade brain microvascular endothelial cells and thereby cross the blood-brain barrier . Reviews discuss the role of YijP in meningitis caused by pathogenic E. coli...

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CB39|protein.P0CB39]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012947,ECOCYC:EG11914,GeneID:948458`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4148532-4150265:-; feature_type=gene
