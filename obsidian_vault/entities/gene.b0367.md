---
entity_id: "gene.b0367"
entity_type: "gene"
name: "tauC"
source_database: "NCBI RefSeq"
source_id: "gene-b0367"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0367"
  - "tauC"
---

# tauC

`gene.b0367`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0367`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tauC (gene.b0367) is a gene entity. It encodes tauC (protein.Q47539). Encoded protein function: FUNCTION: Part of a binding-protein-dependent transport system for taurine. Probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: TAUC-MONOMER. EcoCyc synonyms: yaiJ, ssiC. Genomic coordinates: 386971-387798. EcoCyc protein note: TauC is the predicted inner membrane subunit of an ATP-dependent taurine uptake system; TauC contains six potential membrane-spanning regions . tauBC in-frame deletion mutants are unable to grow with taurine as a sulfur source and show reduced growth with decanesulfonate as a sulfur source .

## Biological Role

Activated by cysB (protein.P0A9F3), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47539|protein.Q47539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=tauC; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=tauC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001261,ECOCYC:G6219,GeneID:945026`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:386971-387798:+; feature_type=gene
