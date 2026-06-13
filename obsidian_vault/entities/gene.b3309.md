---
entity_id: "gene.b3309"
entity_type: "gene"
name: "rplX"
source_database: "NCBI RefSeq"
source_id: "gene-b3309"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3309"
  - "rplX"
---

# rplX

`gene.b3309`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3309`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplX (gene.b3309) is a gene entity. It encodes rplX (protein.P60624). Encoded protein function: FUNCTION: One of two assembly initiator proteins, it binds directly to the 5'-end of the 23S rRNA, where it nucleates assembly of the 50S subunit. It is not thought to be involved in the functions of the mature 50S subunit in vitro. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:357435, ECO:0000269|PubMed:6760192}.; FUNCTION: One of the proteins that surrounds the polypeptide exit tunnel on the outside of the subunit. {ECO:0000269|PubMed:16292303, ECO:0000269|PubMed:357435}. EcoCyc product frame: EG10884-MONOMER. Genomic coordinates: 3447453-3447767. EcoCyc protein note: The L24 protein is a component of the 50S subunit of the ribosome. L3 and L24 are the two proteins that initiate assembly of the 50S subunit; L24 is not thought to be involved in ribosomal function . L24 contacts the M domain finger loop of the signal recognition particle . L24 binds directly to 23S rRNA ; binding of L24 together with L4 to 23S rRNA leads to a change in tertiary structure of the RNA . L4 and L24 cooperatively bind and stabilize the structure of an rRNA fragment containing their binding site . rplX mutants are temperature sensitive and show a very slow growth rate . The defect is in the assembly of 50S subunits...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60624|protein.P60624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010835,ECOCYC:EG10884,GeneID:947810`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3447453-3447767:-; feature_type=gene
