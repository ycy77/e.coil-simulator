---
entity_id: "gene.b0775"
entity_type: "gene"
name: "bioB"
source_database: "NCBI RefSeq"
source_id: "gene-b0775"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0775"
  - "bioB"
---

# bioB

`gene.b0775`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0775`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioB (gene.b0775) is a gene entity. It encodes bioB (protein.P12996). Encoded protein function: FUNCTION: Catalyzes the conversion of dethiobiotin (DTB) to biotin by the insertion of a sulfur atom into dethiobiotin via a radical-based mechanism. {ECO:0000269|PubMed:8142361}. EcoCyc product frame: BIOTIN-SYN-MONOMER. Genomic coordinates: 809344-810384.

## Biological Role

Repressed by birA (protein.P06709).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12996|protein.P12996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P06709|protein.P06709]] `RegulonDB` `S` - regulator=BirA; target=bioB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002644,ECOCYC:EG10118,GeneID:945370`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:809344-810384:+; feature_type=gene
