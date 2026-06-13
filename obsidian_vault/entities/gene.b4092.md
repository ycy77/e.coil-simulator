---
entity_id: "gene.b4092"
entity_type: "gene"
name: "phnP"
source_database: "NCBI RefSeq"
source_id: "gene-b4092"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4092"
  - "phnP"
---

# phnP

`gene.b4092`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4092`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnP (gene.b4092) is a gene entity. It encodes phnP (protein.P16692). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the cyclic ribose-phosphate to form alpha-D-ribose 1,5-bisphosphate. {ECO:0000269|PubMed:19366688, ECO:0000269|PubMed:21341651}. EcoCyc product frame: EG10725-MONOMER. Genomic coordinates: 4314344-4315102.

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16692|protein.P16692]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnP; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013412,ECOCYC:EG10725,GeneID:948600`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4314344-4315102:-; feature_type=gene
