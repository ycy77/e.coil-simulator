---
entity_id: "gene.b2871"
entity_type: "gene"
name: "ygeX"
source_database: "NCBI RefSeq"
source_id: "gene-b2871"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2871"
  - "ygeX"
---

# ygeX

`gene.b2871`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2871`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeX (gene.b2871) is a gene entity. It encodes ygeX (protein.P66899). Encoded protein function: FUNCTION: Catalyzes the alpha,beta-elimination reaction of both L- and D-alpha,beta-diaminopropionate (DAP) to form pyruvate and ammonia. In vitro the D-isomer of serine is degraded to pyruvate, though very poorly; other amino acids (L-serine, D- and L-threonine, D- and L-beta-Cl-alanine) are not substrates. In vivo allows poor growth on L-DAP or a DL-DAP mixture but not on D-DAP alone, this may be due to a poor promoter. DL-DAP is toxic in the absence of this enzyme, it may inhibit enzymes involved in the synthesis of pyruvate and aspartate, as well as amino acids derived from them. {ECO:0000269|PubMed:12596860, ECO:0000269|PubMed:12821154, ECO:0000269|PubMed:22505717, ECO:0000269|PubMed:22904288}. EcoCyc product frame: G7490-MONOMER. Genomic coordinates: 3007510-3008706. EcoCyc protein note: Unlike Salmonella typhimurium, E. coli only shows weak growth on 2,3-diaminopropionate as the sole source of carbon. This difference may be due to the very low expression levels of 2,3-diaminopropionate ammonia-lyase in E. coli . 2,3-Diaminopropionate ammonia-lyase is not stereospecific and catalyzes the α,β-elimination of both the D and L stereoisomer of 2,3-diaminopropionate...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P66899|protein.P66899]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009428,ECOCYC:G7490,GeneID:947012`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3007510-3008706:+; feature_type=gene
