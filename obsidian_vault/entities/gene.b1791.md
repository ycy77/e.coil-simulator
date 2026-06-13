---
entity_id: "gene.b1791"
entity_type: "gene"
name: "nimT"
source_database: "NCBI RefSeq"
source_id: "gene-b1791"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1791"
  - "nimT"
---

# nimT

`gene.b1791`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1791`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nimT (gene.b1791) is a gene entity. It encodes nimT (protein.P76242). Encoded protein function: FUNCTION: Involved in efflux of 2-nitroimidazole. {ECO:0000269|PubMed:25790494}. EcoCyc product frame: B1791-MONOMER. EcoCyc synonyms: yeaN. Genomic coordinates: 1875673-1876854. EcoCyc protein note: A ΔnimT mutant is more sensitive to the natural antibiotic, 2-nitroimidazole, than wild type under both aerobic and anaerobic conditions. nimT appears to be the single target gene of the G6976-MONOMER "NimR" transcriptional regulator . Overexpression of nimT from a plasmid confers resistance to the toxic chemical, bromoacetate . NimT (formerly YeaN) is a member of the Cyanate Porter (CP) family within the Major Facilitator Superfamily (MFS) of transporters .

## Biological Role

Repressed by nimR (protein.P76241).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76242|protein.P76242]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P76241|protein.P76241]] `RegulonDB` `C` - regulator=NimR; target=nimT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005962,ECOCYC:G6977,GeneID:946309`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1875673-1876854:+; feature_type=gene
