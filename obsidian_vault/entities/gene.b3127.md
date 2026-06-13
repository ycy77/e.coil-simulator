---
entity_id: "gene.b3127"
entity_type: "gene"
name: "garP"
source_database: "NCBI RefSeq"
source_id: "gene-b3127"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3127"
  - "garP"
---

# garP

`gene.b3127`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3127`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

garP (gene.b3127) is a gene entity. It encodes garP (protein.P0AA80). Encoded protein function: FUNCTION: Probably involved in the uptake of galactarate and/or D-glucarate (Probable). May also transport D-glycerate (Probable). {ECO:0000305|PubMed:10762278, ECO:0000305|PubMed:9772162}. EcoCyc product frame: YHAU-MONOMER. EcoCyc synonyms: yhaU. Genomic coordinates: 3273573-3274907. EcoCyc protein note: GarP is a putative substrate:proton symporter which is implicated in uptake of the diacid sugars, galactarate and D-glucarate. garP is located in a polycistronic operon along with genes whose products are involved in galactarate and D-glucarate metabolism; garP encodes a potential D-glucarate or galactarate transporter . A Φ(garP-lacZ) transcriptional fusion is induced in cultures grown in the presence of galactarate, D-glucarate or D-glycerate; a polar garP::Tn5 insertion mutant has 'impaired' D-glucarate and D-glycerate utilization . In the Transporter Classification Database GarP is a member of the Anion:Cation Symporter (ACS) Family within the Major Facilitator Superfamily (MFS) . GarP may function as a proton-driven glucarate symporter and perhaps a glucarate:glycerate antiporter; it may form part of a membrane transport metabolon linking the transport of glucarate with the enzymes responsible for its metabolism...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA80|protein.P0AA80]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=garP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010279,ECOCYC:EG12760,GeneID:947642`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3273573-3274907:-; feature_type=gene
