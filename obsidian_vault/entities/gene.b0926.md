---
entity_id: "gene.b0926"
entity_type: "gene"
name: "mepK"
source_database: "NCBI RefSeq"
source_id: "gene-b0926"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0926"
  - "mepK"
---

# mepK

`gene.b0926`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0926`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mepK (gene.b0926) is a gene entity. It encodes mepK (protein.P0AB06). Encoded protein function: FUNCTION: L,D-endopeptidase that cleaves meso-diaminopimelic acid (mDAP)-mDAP cross-links in peptidoglycan (PubMed:30940749). It works in conjunction with other elongation-specific D,D-endopeptidases to make space for efficient incorporation of nascent peptidoglycan strands into the sacculus and thus enable cell wall expansion (PubMed:30940749). In vitro, is able to cleave the mDAP cross-links of soluble muropeptides and of intact peptidoglycan sacculi (PubMed:30940749). Shows a weak D,D-endopeptidase activity (PubMed:30940749). {ECO:0000269|PubMed:30940749}. EcoCyc product frame: G6474-MONOMER. EcoCyc synonyms: ycbK. Genomic coordinates: 983075-983623. EcoCyc protein note: MepK is an L,D-endopeptidase which cleaves the cross-bridges between meso-diaminopimelic acid residues (mDAP-mDAP or 3→3 cross-links) in peptidoglycan. Peptidoglycan isolated from a ΔmepK strain contains an increased percentage of soluble muropeptides containing mDAP-mDAP linkages compared to wild type; purified MepK cleaves 'tri-tetra' muropeptides (ie. peptidoglycan dimers containing an mDAP3-mDAP3 crosslink) to produce tripeptide and tetrapeptide disaccharides...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB06|protein.P0AB06]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003145,ECOCYC:G6474,GeneID:945538`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:983075-983623:+; feature_type=gene
