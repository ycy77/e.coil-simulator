---
entity_id: "gene.b2963"
entity_type: "gene"
name: "mltC"
source_database: "NCBI RefSeq"
source_id: "gene-b2963"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2963"
  - "mltC"
---

# mltC

`gene.b2963`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2963`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltC (gene.b2963) is a gene entity. It encodes mltC (protein.P0C066). Encoded protein function: FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. {ECO:0000255|HAMAP-Rule:MF_01616}. EcoCyc product frame: G7533-MONOMER. EcoCyc synonyms: yggZ. Genomic coordinates: 3104433-3105512. EcoCyc protein note: mltC encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. mltC contains a putative lipoprotein signal sequence; MltC has peptidoglycan hydrolase activity . Purified MltC (residues 19-359) degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tetra2-A2 (a GlcNAc-1,6-anhydro-MurNAc dimer with crosslinked tetrapeptide stems); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem) plus other variations in smaller amounts...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C066|protein.P0C066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009725,ECOCYC:G7533,GeneID:945428`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3104433-3105512:+; feature_type=gene
