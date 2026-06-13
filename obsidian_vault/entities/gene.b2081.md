---
entity_id: "gene.b2081"
entity_type: "gene"
name: "trhP"
source_database: "NCBI RefSeq"
source_id: "gene-b2081"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2081"
  - "trhP"
---

# trhP

`gene.b2081`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2081`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trhP (gene.b2081) is a gene entity. It encodes trhP (protein.P76403). Encoded protein function: FUNCTION: Involved in prephenate-dependent formation of 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). Involved differently in ho5U formation in each tRNA; tRNA(Leu3) and tRNA(Pro3) are major targets of TrhP (PubMed:31253794). {ECO:0000269|PubMed:31253794}. EcoCyc product frame: G7118-MONOMER. EcoCyc synonyms: yegQ. Genomic coordinates: 2165668-2167029. EcoCyc protein note: A ΔtrhP mutant contains reduced levels of the modified wobble base 5-oxyacetylU34-tRNA "cmo5U34": tRNALeu3 and tRNAPro3 retain only 5% of the wild type level of modification; tRNAAla1 and tRNAVal1 remain ~50% modified, and tRNASer1 and tRNAThr4 show reduced levels of modification. A ΔtrhP trhO double mutant has lost all modification of the U34 wobble base of tRNAVal1 and grows more slowly than wild type. Additional knockout of EG30094 serU, EG30104 thrW or EG30066 proK, which encode tRNAs responsible for decoding G-ending codons, results in further reduction of growth . TrhP requires PREPHENATE as a metabolite for 5-HYDROXYU34-TRNA ho5U34 formation . TrhP belongs to the U32 peptidase family; a prephenate-dependent hydroxylation chemistry that may be shared by U32-family proteins is described by...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76403|protein.P76403]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006891,ECOCYC:G7118,GeneID:946609`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2165668-2167029:+; feature_type=gene
