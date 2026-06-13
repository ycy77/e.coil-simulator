---
entity_id: "gene.b2838"
entity_type: "gene"
name: "lysA"
source_database: "NCBI RefSeq"
source_id: "gene-b2838"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2838"
  - "lysA"
---

# lysA

`gene.b2838`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2838`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysA (gene.b2838) is a gene entity. It encodes lysA (protein.P00861). Encoded protein function: FUNCTION: Specifically catalyzes the decarboxylation of meso-diaminopimelate (meso-DAP) to L-lysine. Is not active against the DD- or LL-isomers of diaminopimelate. {ECO:0000269|PubMed:11856852, ECO:0000269|PubMed:14343156, ECO:0000269|PubMed:18508763}. EcoCyc product frame: DIAMINOPIMDECARB-MONOMER. Genomic coordinates: 2977637-2978899.

## Biological Role

Activated by argP (protein.P0A8S1), nac (protein.Q47005).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00861|protein.P00861]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=lysA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lysA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009309,ECOCYC:EG10549,GeneID:947313`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2977637-2978899:-; feature_type=gene
