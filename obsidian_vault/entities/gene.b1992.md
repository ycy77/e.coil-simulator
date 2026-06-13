---
entity_id: "gene.b1992"
entity_type: "gene"
name: "cobS"
source_database: "NCBI RefSeq"
source_id: "gene-b1992"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1992"
  - "cobS"
---

# cobS

`gene.b1992`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1992`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cobS (gene.b1992) is a gene entity. It encodes cobS (protein.P36561). Encoded protein function: FUNCTION: Joins adenosylcobinamide-GDP and alpha-ribazole to generate adenosylcobalamin (Ado-cobalamin). Also synthesizes adenosylcobalamin 5'-phosphate from adenosylcobinamide-GDP and alpha-ribazole 5'-phosphate (By similarity). {ECO:0000250}. EcoCyc product frame: COBS-MONOMER. Genomic coordinates: 2064479-2065222. EcoCyc protein note: E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobS encodes a cobalamin 5'-phosphate synthase that carries out the penultimate step in adenosylcobalamin synthesis. Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36561|protein.P36561]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cobS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006613,ECOCYC:EG12150,GeneID:946520`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2064479-2065222:-; feature_type=gene
