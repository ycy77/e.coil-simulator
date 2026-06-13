---
entity_id: "gene.b3839"
entity_type: "gene"
name: "tatC"
source_database: "NCBI RefSeq"
source_id: "gene-b3839"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3839"
  - "tatC"
---

# tatC

`gene.b3839`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3839`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tatC (gene.b3839) is a gene entity. It encodes tatC (protein.P69423). Encoded protein function: FUNCTION: Part of the twin-arginine translocation (Tat) system that transports large folded proteins containing a characteristic twin-arginine motif in their signal peptide across membranes. Together with TatB, TatC is part of a receptor directly interacting with Tat signal peptides. {ECO:0000255|HAMAP-Rule:MF_00902, ECO:0000269|PubMed:11922668, ECO:0000269|PubMed:14580344, ECO:0000269|PubMed:19666509, ECO:0000269|PubMed:20926683, ECO:0000269|PubMed:9660752}. EcoCyc product frame: EG11479-MONOMER. EcoCyc synonyms: mttB, yigU, yigV. Genomic coordinates: 4022736-4023512. EcoCyc protein note: TatC is an inner membrane component of the twin arginine translocation (Tat) complex for the export of folded proteins. TatC and TatB form a functional unit that is thought to act as the substrate receptor for the Tat complex. TatC is an integral inner membrane protein . Deletion of tatC blocks the export of precursor proteins that contain twin-arginine signal sequences and are predicted to bind redox cofactors Membrane topology predictions using experimentally determined C terminus locations indicate that TatC has 6 transmembrane helices and the C-terminus is located in the periplasm . TatC may form functional dimers...

## Enriched Pathways

- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69423|protein.P69423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012547,ECOCYC:EG11479,GeneID:948328`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4022736-4023512:+; feature_type=gene
