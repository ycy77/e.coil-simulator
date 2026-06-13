---
entity_id: "gene.b3352"
entity_type: "gene"
name: "yheS"
source_database: "NCBI RefSeq"
source_id: "gene-b3352"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3352"
  - "yheS"
---

# yheS

`gene.b3352`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3352`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yheS (gene.b3352) is a gene entity. It encodes yheS (protein.P63389). Encoded protein function: FUNCTION: Involved in peptide bond synthesis. Releases SecM-induced translation arrest during translation; releases arrest even after the SecM nascent peptide has stalled the ribosome (PubMed:38661232). Genetic data indicate it may be involved in ribosome assembly or function (PubMed:30597160). {ECO:0000269|PubMed:38661232, ECO:0000305|PubMed:30597160}. EcoCyc product frame: YHES-MONOMER. Genomic coordinates: 3481289-3483202. EcoCyc protein note: YheS is a member of the ABCF family within the ATP-binding cassette (ABC) superfamily . There are four ABCF family proteins within E. coli K-12: YheS, YJJK-MONOMER "EttA", UUP-MONOMER "Uup" and G6423-MONOMER "YbiT", all of which are involved in noncanonical translation of 'hard-to-translate' nascent peptides getting them through the ribosome exit tunnel. YheS releases nascent EG11087-MONOMER "SecM" from translational arrest . Genetic interaction data of YheS point to a role in ribosome assembly or function . Overexpression of YheS in a ΔbipA mutant exacerbates its cold-sensitive growth defect . Using the E. coli CFT073 YheS protein, overexpression of an EQ2 mutant of YheS (carrying substitutions in the predicted ATPase active sites) inhibits protein synthesis...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63389|protein.P63389]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010955,ECOCYC:EG12903,GeneID:947856`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3481289-3483202:+; feature_type=gene
