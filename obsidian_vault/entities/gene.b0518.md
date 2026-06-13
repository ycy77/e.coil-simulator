---
entity_id: "gene.b0518"
entity_type: "gene"
name: "fdrA"
source_database: "NCBI RefSeq"
source_id: "gene-b0518"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0518"
  - "fdrA"
---

# fdrA

`gene.b0518`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0518`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdrA (gene.b0518) is a gene entity. It encodes allF (protein.Q47208). Encoded protein function: FUNCTION: Component of a carbamoyltransferase involved in the anaerobic nitrogen utilization via the assimilation of allantoin (PubMed:34494882, PubMed:38888336). Catalyzes the conversion of oxalurate (N-carbamoyl-2-oxoglycine) to oxamate and carbamoyl phosphate (PubMed:38888336). {ECO:0000269|PubMed:34494882, ECO:0000269|PubMed:38888336}. EcoCyc product frame: G6287-MONOMER. EcoCyc synonyms: ylbD, fdrA. Genomic coordinates: 546680-548347. EcoCyc protein note: Using genome and metabolic context methods, hypothesize that fdrA encodes an oxamate:CoA ligase which continues the degradation of oxamate produced by the PWY0-41 "anaerobic allantoin degradation pathway". The fate of oxamate is not clear; suggest that oxamate is not degraded further and they provide evidence that FdrA is critical for oxamate production during anaerobic allantoin degradation and may be the orphan enzyme OXAMATE-CARBAMOYLTRANSFERASE-RXN oxamate carbomoyltransferase (OXTCase). The OXTCase activity was subsequently found to require the first 3 genes in the TU0-12962 operon; all three of which are required to complement the triple mutant, ΔallFGH...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47208|protein.Q47208]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001784,ECOCYC:G6287,GeneID:946298`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:546680-548347:+; feature_type=gene
