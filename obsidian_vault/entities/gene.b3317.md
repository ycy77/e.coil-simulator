---
entity_id: "gene.b3317"
entity_type: "gene"
name: "rplB"
source_database: "NCBI RefSeq"
source_id: "gene-b3317"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3317"
  - "rplB"
---

# rplB

`gene.b3317`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3317`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplB (gene.b3317) is a gene entity. It encodes rplB (protein.P60422). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins (PubMed:3298242). Located near the base of the L1 stalk, it is probably also mobile. Required for association of the 30S and 50S subunits to form the 70S ribosome, for tRNA binding and peptide bond formation (PubMed:8722025). It has been suggested to have peptidyltransferase activity; this is highly controversial. {ECO:0000269|PubMed:10756104, ECO:0000269|PubMed:11013226, ECO:0000269|PubMed:11114255, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:8722025}.; FUNCTION: In the E.coli 70S ribosome in the initiation state it has been modeled to make several contacts with the 16S rRNA (forming bridge B7b, PubMed:12809609); these contacts are broken in the model with bound EF-G. {ECO:0000269|PubMed:12809609}. EcoCyc product frame: EG10865-MONOMER. Genomic coordinates: 3450543-3451364. EcoCyc protein note: The L2 protein is a component of the 50S subunit of the ribosome and is part of the peptidyltransferase center. L2 is highly evolutionarily conserved . L2 is required for the association of the 30S and 50S subunits ; one end of the elongated L2 protein is located at the intersubunit interface of the 50S subunit...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60422|protein.P60422]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplB; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010854,ECOCYC:EG10865,GeneID:947820`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3450543-3451364:-; feature_type=gene
