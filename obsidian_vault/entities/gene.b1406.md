---
entity_id: "gene.b1406"
entity_type: "gene"
name: "pdxI"
source_database: "NCBI RefSeq"
source_id: "gene-b1406"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1406"
  - "pdxI"
---

# pdxI

`gene.b1406`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1406`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxI (gene.b1406) is a gene entity. It encodes pdxI (protein.P25906). Encoded protein function: FUNCTION: Catalyzes the NAD(P)H-dependent reduction of pyridoxal to pyridoxine in vitro. Is not able to reduce 4-pyridoxate, and to oxidize pyridoxine or pyridoxamine (PubMed:27941785). Has Kemp eliminase activity towards the non-physiological substrate 5-nitrobenzisoxazole, producing 4-nitro-2-cyanophenol; this activity is not considered to be physiologically relevant (PubMed:21332126). {ECO:0000269|PubMed:21332126, ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG11309-MONOMER. EcoCyc synonyms: ydbC. Genomic coordinates: 1474221-1475081. EcoCyc protein note: The NADPH-dependent pyridoxal reductase (PdxI) contributes to the PLPSAL-PWY (e.g. vitamin B6 salvage) pathway . The catalytic activity of PdxI was first discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . Crystal structures of unliganded, NADPH-bound and NADPH-PL bound PdxI have been determined to resolutions of 2.0 - 2.3 Å PdxI belongs to aldo-keto reductase (AKR) superfamily with a TIM barrel-fold made of only 6 instead of 8 beta strands and with an Arg126 replacing the catalytic His residue...

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25906|protein.P25906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004698,ECOCYC:EG11309,GeneID:945980`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1474221-1475081:+; feature_type=gene
