---
entity_id: "gene.b3206"
entity_type: "gene"
name: "npr"
source_database: "NCBI RefSeq"
source_id: "gene-b3206"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3206"
  - "npr"
---

# npr

`gene.b3206`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3206`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

npr (gene.b3206) is a gene entity. It encodes ptsO (protein.P0A9N0). Encoded protein function: FUNCTION: Component of the phosphoenolpyruvate-dependent nitrogen-metabolic phosphotransferase system (nitrogen-metabolic PTS), that seems to be involved in regulating nitrogen metabolism. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein NPr by enzyme I-Ntr. Phospho-NPr then transfers it to EIIA-Ntr. Could function in the transcriptional regulation of sigma-54 dependent operons in conjunction with the NPr (PtsO) and EIIA-Ntr (PtsN) proteins. EcoCyc product frame: MONOMER0-4292. EcoCyc synonyms: yhbK, ptsO, rpoR. Genomic coordinates: 3347966-3348238. EcoCyc protein note: NPr is the second phosphotransfer protein of the nitrogen phosphoenolpyruvate (PEP)-dependent phosphotransferase system (PTSNtr) in E. coli K-12. The exact function of the PTSNtr is not clear - it has been implicated in the regulation of nitrogen metabolism and in potassium homeostasis (reviewed in but see also ). EG12188-MONOMER "PtsP", also known as enzyme INtr, phosphorylates NPr in vitro. This reaction occurs at an optimum pH of 8.0, is dependent on Mg2+, is stimulated by high ionic strength, and has two Km values for Npr of 2 and 10 μM...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9N0|protein.P0A9N0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=npr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010524,ECOCYC:EG12147,GeneID:947914`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3347966-3348238:+; feature_type=gene
