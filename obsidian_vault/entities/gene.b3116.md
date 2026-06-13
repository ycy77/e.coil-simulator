---
entity_id: "gene.b3116"
entity_type: "gene"
name: "tdcC"
source_database: "NCBI RefSeq"
source_id: "gene-b3116"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3116"
  - "tdcC"
---

# tdcC

`gene.b3116`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3116`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcC (gene.b3116) is a gene entity. It encodes tdcC (protein.P0AAD8). Encoded protein function: FUNCTION: Involved in the import of threonine and serine into the cell, with the concomitant import of a proton (symport system). {ECO:0000255|HAMAP-Rule:MF_01583, ECO:0000269|PubMed:2115866, ECO:0000269|PubMed:9498571}. EcoCyc product frame: TDCC-MONOMER. Genomic coordinates: 3263686-3265017. EcoCyc protein note: TdcC is a threonine transport system, likely to function as a threonine/proton symporter. Disruption of tdcC reduced threonine uptake under anaerobic conditions, and this defect could be complemented by the cloned tdcC gene . The TdcC transport system displayed a Km of approx 6 μM and threonine transport was inhibited by uncouplers, suggesting it is a high affinity threonine/proton symporter . TdcC has also been shown to be a proton-driven serine transporter . TdcC is a member of the hydroxy/aromatic amino acid permease (HAAAP) family of transporters, and is homologous to the serine transporter SdaC. The tdcC gene is located in the tdcABC operon, which also codes for threonine dehydratase . Expression of tdc-lacZ fusions has indicated that this operon is expressed under anaerobic conditions . Threonine and serine imported under anaerobic conditions are degraded to ammonia and the corresponding α-keto acids.

## Biological Role

Activated by crp (protein.P0ACJ8), tdcA (protein.P0ACQ7), tdcR (protein.P11866).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAD8|protein.P0AAD8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tdcC; function=+
- `activates` <-- [[protein.P0ACQ7|protein.P0ACQ7]] `RegulonDB` `S` - regulator=TdcA; target=tdcC; function=+
- `activates` <-- [[protein.P11866|protein.P11866]] `RegulonDB` `S` - regulator=TdcR; target=tdcC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010247,ECOCYC:EG10991,GeneID:947629`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3263686-3265017:-; feature_type=gene
