---
entity_id: "gene.b0305"
entity_type: "gene"
name: "rclR"
source_database: "NCBI RefSeq"
source_id: "gene-b0305"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0305"
  - "rclR"
---

# rclR

`gene.b0305`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0305`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rclR (gene.b0305) is a gene entity. It encodes rclR (protein.P77379). Encoded protein function: FUNCTION: Involved in reactive chlorine species (RCS) stress resistance. Up-regulates, in response to hypochlorous acid (HOCl), the expression of three genes essential for survival of RCS stress (rclA, rclB and rclC) and its own expression. {ECO:0000269|PubMed:24078635}. EcoCyc product frame: G6175-MONOMER. EcoCyc synonyms: ykgD. Genomic coordinates: 320227-321081. EcoCyc protein note: RclR (formerly YkgD) is a redox-sensitive transcriptional activator that belongs to the AraC family, whose highly conserved cysteine residues are highly specifically sensitive to oxidation by reactive chlorine species (RCS) . RclR relies on the reversible oxidation of conserved redox-sensitive cysteine residues to specifically sense RCS and control the expression of genes essential for survival under reactive chlorine (HOCl) stress . RclR is activated by hypochlorous acid (HOCl) or N-chlorotaurine, and that activation may involve formation of one disulfide bond. RclR contains two conserved cysteine residues (Cys-21 and Cys-89) and two conserved histidine residues (His-42 and His-75). Cys-21 and Cys-89 are important in the activation of RclR in vivo. Cys-21 could play the more critical role in the RclR redox response...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77379|protein.P77379]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001054,ECOCYC:G6175,GeneID:945616`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:320227-321081:+; feature_type=gene
