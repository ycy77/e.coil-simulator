---
entity_id: "gene.b3567"
entity_type: "gene"
name: "xylG"
source_database: "NCBI RefSeq"
source_id: "gene-b3567"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3567"
  - "xylG"
---

# xylG

`gene.b3567`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3567`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylG (gene.b3567) is a gene entity. It encodes xylG (protein.P37388). Encoded protein function: FUNCTION: Part of the ABC transporter complex XylFGH involved in xylose import. Responsible for energy coupling to the transport system (Probable). The XylFGH system can also transport ribose in absence of xylose. {ECO:0000255|HAMAP-Rule:MF_01722, ECO:0000269|PubMed:9673030, ECO:0000305}. EcoCyc product frame: XYLG-MONOMER. Genomic coordinates: 3732201-3733742. EcoCyc protein note: xylG encodes the predicted ATP-binding subunit of a high-affinity xylose uptake system; XylG contains sequence motifs conserved in ATP-binding cassette proteins; XylG contains an ABC-ABC domain .

## Biological Role

Activated by xylR (protein.P0ACI3).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37388|protein.P37388]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011648,ECOCYC:EG12275,GeneID:948127`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3732201-3733742:+; feature_type=gene
