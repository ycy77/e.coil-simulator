---
entity_id: "gene.b1097"
entity_type: "gene"
name: "mltG"
source_database: "NCBI RefSeq"
source_id: "gene-b1097"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1097"
  - "mltG"
---

# mltG

`gene.b1097`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1097`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltG (gene.b1097) is a gene entity. It encodes mltG (protein.P28306). Encoded protein function: FUNCTION: Functions as a peptidoglycan terminase that cleaves nascent peptidoglycan strands endolytically to terminate their elongation (PubMed:26507882). Required for normal glycan strand length distribution (PubMed:26507882). May function as a terminase for both classes of peptidoglycan (PG) synthases (aPBP and SEDS-bPBP synthases) by cleaving PG chains as they are being actively synthesized (PubMed:33278861). {ECO:0000269|PubMed:26507882, ECO:0000269|PubMed:33278861}. EcoCyc product frame: EG11494-MONOMER. EcoCyc synonyms: yceG. Genomic coordinates: 1154112-1155134. EcoCyc protein note: MltG is an inner membrane enzyme with endolytic murein transglycosylase activity; it may function to terminate nascent peptidoglycan (PG) synthesis . Evidence for an antagonistic relationship between MltG function and PG synthases supports this contention . Purified, soluble MltG degrades purified murein sacculi and releases monomeric GlcNAc-anhydroMurNAc tetrapeptide plus linear tetra- and hexasaccharide oligomers terminating with an anhydroMurNAc end . MltG is predicted to contain a single transmembrane region with a small N-terminal domain located in the cytoplasm and a large C-terminal domain in the periplasm . MltG interacts with CPLX0-3951 "MrcB" (PBP1B) and with itself...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28306|protein.P28306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003712,ECOCYC:EG11494,GeneID:945660`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1154112-1155134:+; feature_type=gene
