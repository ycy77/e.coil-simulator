---
entity_id: "gene.b2720"
entity_type: "gene"
name: "hycF"
source_database: "NCBI RefSeq"
source_id: "gene-b2720"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2720"
  - "hycF"
---

# hycF

`gene.b2720`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2720`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycF (gene.b2720) is a gene entity. It encodes hycF (protein.P16432). Encoded protein function: FUNCTION: Probable electron transfer protein for hydrogenase 3. EcoCyc product frame: HYCF-MONOMER. EcoCyc synonyms: hevF. Genomic coordinates: 2844210-2844752. EcoCyc protein note: The hycBCDEFG genes in E.coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycF is thought to be a 4Fe-4S ferredoxin type protein, an intermediate electron carrier protein . In the cryo-EM structures of FHL reported by , HycF interacts with HycB and with FdhF, and it coordinates an unpredicted metal ion (tentatively assigned as an iron).

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16432|protein.P16432]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycF; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycF; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008942,ECOCYC:EG10479,GeneID:947048`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2844210-2844752:-; feature_type=gene
