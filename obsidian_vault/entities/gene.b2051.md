---
entity_id: "gene.b2051"
entity_type: "gene"
name: "gmm"
source_database: "NCBI RefSeq"
source_id: "gene-b2051"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2051"
  - "gmm"
---

# gmm

`gene.b2051`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2051`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gmm (gene.b2051) is a gene entity. It encodes gmm (protein.P32056). Encoded protein function: FUNCTION: Hydrolyzes both GDP-mannose and GDP-glucose (PubMed:10913267, PubMed:23481913, PubMed:7592609). Could participate in the regulation of cell wall biosynthesis by influencing the concentration of GDP-mannose or GDP-glucose in the cell. Might also be involved in the biosynthesis of the slime polysaccharide colanic acid (PubMed:10913267, PubMed:7592609). {ECO:0000269|PubMed:10913267, ECO:0000269|PubMed:23481913, ECO:0000269|PubMed:7592609}. EcoCyc product frame: GDPMANMANHYDRO-MONOMER. EcoCyc synonyms: nudD, wcaH, yefC. Genomic coordinates: 2125743-2126222. EcoCyc protein note: GDP-mannose mannosyl hydrolase (GDPMH) is able to hydrolyze both GDP-mannose and GDP-glucose. Its biological role is as yet unknown, though it may participate in the regulation of cell wall biosynthesis by influencing the cell concentration of GDP-mannose or GDP-glucose . The enzyme was first identified as a member of the Nudix hydrolase family . However, unlike other Nudix hydrolases, GDPMH catalyzes the nucleophilic substitution at C1' rather than phosphorus and requires one divalent cation per active site to facilitate the departure of GMP . The divalent cation binding site, the general base catalyst, and other residues important for catalytic activity were identified by site-directed mutagenesis...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32056|protein.P32056]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006796,ECOCYC:EG11789,GeneID:946559`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2125743-2126222:-; feature_type=gene
