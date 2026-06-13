---
entity_id: "gene.b0696"
entity_type: "gene"
name: "kdpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0696"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0696"
  - "kdpC"
---

# kdpC

`gene.b0696`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0696`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdpC (gene.b0696) is a gene entity. It encodes kdpC (protein.P03961). Encoded protein function: FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit acts as a catalytic chaperone that increases the ATP-binding affinity of the ATP-hydrolyzing subunit KdpB by the formation of a transient KdpB/KdpC/ATP ternary complex (PubMed:21711450). {ECO:0000269|PubMed:21711450, ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:8499455}. EcoCyc product frame: EG10515-MONOMER. EcoCyc synonyms: kac. Genomic coordinates: 724407-724979. EcoCyc protein note: KdpC is an inner membrane subunit of a potassium ion transporting P-type ATPase complex. A non-polar ΔkdpC strain is unable to grow under low potassium ((G116R)BC, KdpC has a single transmembrane helix and a soluble domain located on the periplasmic side of the membrane .

## Biological Role

Activated by rpoD (protein.P00579), kdpE (protein.P21866).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03961|protein.P03961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdpC; function=+
- `activates` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `C` - regulator=KdpE; target=kdpC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002374,ECOCYC:EG10515,GeneID:947508`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:724407-724979:-; feature_type=gene
