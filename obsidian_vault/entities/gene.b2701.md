---
entity_id: "gene.b2701"
entity_type: "gene"
name: "mltB"
source_database: "NCBI RefSeq"
source_id: "gene-b2701"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2701"
  - "mltB"
---

# mltB

`gene.b2701`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2701`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mltB (gene.b2701) is a gene entity. It encodes mltB (protein.P41052). Encoded protein function: FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division. EcoCyc product frame: G7410-MONOMER. EcoCyc synonyms: slt. Genomic coordinates: 2824491-2825576. EcoCyc protein note: mltB encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltB is an outer membrane lipoprotein . Proteolytic cleavage of MltB releases a soluble, active form of the protein (known as Slt35) . Purified Slt35 has peptidoglycan hydrolase activity, releasing 1,6-anhydromuropeptides from isolated peptidoglycan polymer . Purified, soluble MltB is able to degrade a synthetic peptidoglycan substrate containing a short chain backbone of only two repeats of GlcNAc-MurNAc...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41052|protein.P41052]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008885,ECOCYC:G7410,GeneID:947184`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2824491-2825576:-; feature_type=gene
