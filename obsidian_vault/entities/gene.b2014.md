---
entity_id: "gene.b2014"
entity_type: "gene"
name: "plaP"
source_database: "NCBI RefSeq"
source_id: "gene-b2014"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2014"
  - "plaP"
---

# plaP

`gene.b2014`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2014`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plaP (gene.b2014) is a gene entity. It encodes plaP (protein.P0AA47). Encoded protein function: FUNCTION: Putrescine importer. Required for induction of type 1 pili-driven surface motility. {ECO:0000269|PubMed:21266585}. EcoCyc product frame: YEEF-MONOMER. EcoCyc synonyms: yeeF. Genomic coordinates: 2085704-2087062. EcoCyc protein note: PlaP is a low-affinity putrescine importer . PlaP is a member of the APC (amino acid/polyamine/organocation) superfamily and functions as a putrescine:proton symporter . PlaP is required for the induction of type-I pili driven motility induced by putrescine as a signaling molecule (see also ). Expression of plaP decreased in response to treatment with acetate and sodium salicylate . CRP was identified as a repressor for plaP expression using run-off transcription/microarray analysis . The binding site of CRP overlaps the binding site of RNA polymerase . plaP has also shown to be repressed under anaerobic conditions . PlaP and B1296-MONOMER PuuP are receptors for the group 5 CDI ionophore toxins . plaP: putrescine low affinity permease

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA47|protein.P0AA47]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006696,ECOCYC:EG11896,GeneID:946533`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2085704-2087062:-; feature_type=gene
