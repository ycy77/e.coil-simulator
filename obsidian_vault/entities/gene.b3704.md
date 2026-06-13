---
entity_id: "gene.b3704"
entity_type: "gene"
name: "rnpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3704"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3704"
  - "rnpA"
---

# rnpA

`gene.b3704`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3704`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnpA (gene.b3704) is a gene entity. It encodes rnpA (protein.P0A7Y8). Encoded protein function: FUNCTION: RNaseP catalyzes the removal of the 5'-leader sequence from pre-tRNA to produce the mature 5'-terminus. It can also cleave other RNA substrates such as 4.5S RNA. The protein component plays an auxiliary but essential role in vivo by binding to the 5'-leader sequence and broadening the substrate specificity of the ribozyme. {ECO:0000255|HAMAP-Rule:MF_00227, ECO:0000269|PubMed:22298511}. EcoCyc product frame: EG10862-MONOMER. Genomic coordinates: 3884493-3884852. EcoCyc protein note: RnpA protein and RnpB RNA together comprise the ribonuclease P (RNase P) holoenzyme . RNase P acts in processing of tRNA precursor molecules and the stable 4.5 S RNA precursor . The RnpB RNA subunit alone exhibits catalytic activity toward tRNA precursors in vitro under high ionic strength conditions, but requires the protein subunit under physiological conditions and for efficient activity toward a 4.5 S RNA precursor substrate . The protein subunit stabilizes the global structure of the RNA component, allowing it to exhibit the properties of the holoenzyme complex . RNase P also exhibits activity toward C4 repressor RNA of bacteriophages P1 and P7, which may indicate a role for RNase P in lysogeny/lysis regulation , and toward CI RNA, which is involved in immunity to bacteriophage P4...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Y8|protein.P0A7Y8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012117,ECOCYC:EG10862,GeneID:948215`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3884493-3884852:+; feature_type=gene
