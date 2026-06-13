---
entity_id: "gene.b3881"
entity_type: "gene"
name: "yihT"
source_database: "NCBI RefSeq"
source_id: "gene-b3881"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3881"
  - "yihT"
---

# yihT

`gene.b3881`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3881`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihT (gene.b3881) is a gene entity. It encodes yihT (protein.P32141). Encoded protein function: FUNCTION: Cleaves 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) to form dihydroxyacetone phosphate (DHAP) and 3-sulfolactaldehyde (SLA). {ECO:0000255|HAMAP-Rule:MF_01912, ECO:0000269|PubMed:24463506}. EcoCyc product frame: EG11846-MONOMER. EcoCyc synonyms: squT. Genomic coordinates: 4071773-4072651. EcoCyc protein note: 6-Deoxy-6-sulfofructose-1-phosphate aldolase (YihT) catalyzes the cleavage of CPD-16502 to yield DIHYDROXY-ACETONE-PHOSPHATE and CPD-16503 , a part of the PWY-7446 pathway. Expression of YihT is induced by growth on sulfoquinovose and lactose . A yihT mutant is unable to grow on sulfoquinovose as the sole source of carbon .

## Biological Role

Repressed by csqR (protein.P32144). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32141|protein.P32141]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yihT; function=+
- `represses` <-- [[protein.P32144|protein.P32144]] `RegulonDB` `S` - regulator=CsqR; target=yihT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012675,ECOCYC:EG11846,GeneID:948373`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4071773-4072651:-; feature_type=gene
