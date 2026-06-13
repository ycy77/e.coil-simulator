---
entity_id: "gene.b3421"
entity_type: "gene"
name: "rtcB"
source_database: "NCBI RefSeq"
source_id: "gene-b3421"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3421"
  - "rtcB"
---

# rtcB

`gene.b3421`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3421`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rtcB (gene.b3421) is a gene entity. It encodes rtcB (protein.P46850). Encoded protein function: FUNCTION: GTP-dependent RNA ligase that is involved in RNA repair (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Joins RNA with 2',3'-cyclic-phosphate or 3'-phosphate ends to RNA with 5'-hydroxy ends (PubMed:21224389, PubMed:21757685, PubMed:22045815, PubMed:22474365, PubMed:22730297, PubMed:26858100). Also acts as a DNA ligase in case of DNA damage by splicing 'dirty' DNA breaks, characterized by 3'-phosphate (or cyclic-phosphate) and 5'-hydroxy ends that cannot be sealed by classical DNA ligases (PubMed:24218597). Repairs tRNA cleaved by colicins D or E5, does not repair damaged 16S rRNA (By similarity). {ECO:0000250|UniProtKB:P0DX92, ECO:0000269|PubMed:21224389, ECO:0000269|PubMed:21757685, ECO:0000269|PubMed:22045815, ECO:0000269|PubMed:22474365, ECO:0000269|PubMed:22730297, ECO:0000269|PubMed:24218597, ECO:0000269|PubMed:26858100}.; FUNCTION: Able to catalyze tRNA splicing in vivo in yeast, but bacteria are not known to splice tRNA. {ECO:0000269|PubMed:21757685}. EcoCyc product frame: G7751-MONOMER. EcoCyc synonyms: yhgL. Genomic coordinates: 3556853-3558079. EcoCyc protein note: RtcB is a GTP-dependent 3'-5' RNA ligase with the ability to join RNA 2',3'-cyclic-PO4 or 3'-PO4 ends to RNA 5'-OH ends...

## Biological Role

Activated by rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46850|protein.P46850]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rtcB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011170,ECOCYC:G7751,GeneID:947929`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3556853-3558079:-; feature_type=gene
