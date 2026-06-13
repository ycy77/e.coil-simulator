---
entity_id: "gene.b3137"
entity_type: "gene"
name: "kbaY"
source_database: "NCBI RefSeq"
source_id: "gene-b3137"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3137"
  - "kbaY"
---

# kbaY

`gene.b3137`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3137`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kbaY (gene.b3137) is a gene entity. It encodes kbaY (protein.P0AB74). Encoded protein function: FUNCTION: Catalytic subunit of the tagatose-1,6-bisphosphate aldolase KbaYZ, which catalyzes the reversible aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to produce tagatose 1,6-bisphosphate (TBP). Requires KbaZ subunit for full activity and stability. {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:11976750}. EcoCyc product frame: TAGAALDOL1-MONOMER. EcoCyc synonyms: yraC, kba, agaY. Genomic coordinates: 3283143-3284003.

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB74|protein.P0AB74]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kbaY; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=kbaY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=kbaY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010307,ECOCYC:EG12768,GeneID:947644`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3283143-3284003:+; feature_type=gene
