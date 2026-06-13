---
entity_id: "gene.b2587"
entity_type: "gene"
name: "kgtP"
source_database: "NCBI RefSeq"
source_id: "gene-b2587"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2587"
  - "kgtP"
---

# kgtP

`gene.b2587`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2587`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kgtP (gene.b2587) is a gene entity. It encodes kgtP (protein.P0AEX3). Encoded protein function: FUNCTION: Uptake of alpha-ketoglutarate across the boundary membrane with the concomitant import of a cation (symport system). {ECO:0000269|PubMed:2053984}. EcoCyc product frame: KGTP-MONOMER. EcoCyc synonyms: witA. Genomic coordinates: 2724448-2725746. EcoCyc protein note: KgtP is a proton-driven transporter for α-ketoglutarate. kgtP mutants show greatly impaired growth on α-ketoglutarate which can be complemented by the cloned kgtP gene . KgtP-dependent α-ketoglutarate/proton symport activity has been demonstrated in membrane vesicles . KgtP displays a Km for α-ketoglutarate of 13-46 μM. KgtP-mediated α-ketoglutarate transport could be partially inhibited by fumarate, malate and succinate . Consistent with its function as an α-ketoglutarate/proton symport, KgtP is a member of the major facilitator superfamily . Alkaline phosphatase fusions have demonstrated that KgtP consists of twelve transmembrane spanning segments . Arg-92 and Asp-88 have been shown to be essential residues in the KgtP transporter . kgtP appears to be constitutively expressed . KgtP has been implicated in arabinose efflux .

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEX3|protein.P0AEX3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=kgtP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008515,ECOCYC:EG10522,GeneID:947069`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2724448-2725746:-; feature_type=gene
