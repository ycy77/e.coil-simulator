---
entity_id: "gene.b2608"
entity_type: "gene"
name: "rimM"
source_database: "NCBI RefSeq"
source_id: "gene-b2608"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2608"
  - "rimM"
---

# rimM

`gene.b2608`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2608`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimM (gene.b2608) is a gene entity. It encodes rimM (protein.P0A7X6). Encoded protein function: FUNCTION: One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late assembly stage of the 30S ribosomal subunit. An accessory protein needed during the final step in assembly of the 30S ribosomal subunit, for assembly of the head region (the 16S rRNA 3' domain) (PubMed:11514519, PubMed:15496525, PubMed:20188109, PubMed:23611982, PubMed:27382067). It may act while Era is associated and before RimP in 30S subunit assembly (PubMed:20188109). Essential for efficient processing of 16S rRNA; a deletion mutant accumulates 17S rRNA (PubMed:9422595). Deletions do not assemble the head-associated ribosomal proteins correctly (PubMed:23611982, PubMed:27382067). May be needed both before and after RbfA during the maturation of 16S rRNA. It has affinity for free ribosomal 30S subunits but not for 70S ribosomes (PubMed:9226267). {ECO:0000269|PubMed:11514519, ECO:0000269|PubMed:15496525, ECO:0000269|PubMed:20188109, ECO:0000269|PubMed:23611982, ECO:0000269|PubMed:27382067, ECO:0000269|PubMed:9226267, ECO:0000269|PubMed:9422595}. EcoCyc product frame: EG11153-MONOMER. EcoCyc synonyms: yfjA. Genomic coordinates: 2745370-2745918. EcoCyc protein note: RimM is an assembly factor for the 30S ribosomal subunit...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7X6|protein.P0A7X6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rimM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008579,ECOCYC:EG11153,GeneID:947101`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2745370-2745918:-; feature_type=gene
