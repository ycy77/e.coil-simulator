---
entity_id: "gene.b0588"
entity_type: "gene"
name: "fepC"
source_database: "NCBI RefSeq"
source_id: "gene-b0588"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0588"
  - "fepC"
---

# fepC

`gene.b0588`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0588`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fepC (gene.b0588) is a gene entity. It encodes fepC (protein.P23878). Encoded protein function: FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1838574, PubMed:3011753). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:1838574, ECO:0000269|PubMed:3011753, ECO:0000305}. EcoCyc product frame: FEPC-MONOMER. Genomic coordinates: 619384-620199. EcoCyc protein note: fepC encodes the predicted ATP-binding subunit of a ferrric enterobactin ABC transporter complex . Insertional inactivation of fepC results in the loss of ferric enterobactin uptake

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23878|protein.P23878]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fepC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fepC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002025,ECOCYC:EG10295,GeneID:945201`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:619384-620199:-; feature_type=gene
