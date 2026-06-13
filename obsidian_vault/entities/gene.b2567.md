---
entity_id: "gene.b2567"
entity_type: "gene"
name: "rnc"
source_database: "NCBI RefSeq"
source_id: "gene-b2567"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2567"
  - "rnc"
---

# rnc

`gene.b2567`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2567`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnc (gene.b2567) is a gene entity. It encodes rnc (protein.P0A7Y0). Encoded protein function: FUNCTION: Digests double-stranded RNA formed within single-strand substrates, but not RNA-DNA hybrids. Involved in the processing of rRNA precursors, viral transcripts, some mRNAs and at least 1 tRNA (metY, a minor form of tRNA-init-Met). Cleaves the 30S primary rRNA transcript to yield the immediate precursors to the 16S and 23S rRNAs; cleavage can occur in assembled 30S, 50S and even 70S subunits and is influenced by the presence of ribosomal proteins. The E.coli enzyme does not cleave R.capsulatus rRNA precursor, although R.capsulatus will complement an E.coli disruption, showing substrate recognition is different. Removes the intervening sequences from Salmonella typhimurium rRNA precursor. Complements the pre-crRNA processing defect in an rnc deletion in S.pyogenes strain 370, although this E.coli strain does not have the corresponding CRISPR locus (strain TOP10) (PubMed:23535272). {ECO:0000269|PubMed:2085545, ECO:0000269|PubMed:23535272, ECO:0000269|PubMed:2406020, ECO:0000269|PubMed:2481042, ECO:0000269|PubMed:3903434, ECO:0000269|PubMed:4587248, ECO:0000269|PubMed:4592261, ECO:0000269|PubMed:4610145, ECO:0000269|PubMed:4865702, ECO:0000269|PubMed:6159890, ECO:0000269|PubMed:932008}. EcoCyc product frame: EG10857-MONOMER. Genomic coordinates: 2703383-2704063.

## Enriched Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Y0|protein.P0A7Y0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008448,ECOCYC:EG10857,GeneID:947033`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2703383-2704063:-; feature_type=gene
