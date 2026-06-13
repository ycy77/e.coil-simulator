---
entity_id: "gene.b2733"
entity_type: "gene"
name: "mutS"
source_database: "NCBI RefSeq"
source_id: "gene-b2733"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2733"
  - "mutS"
---

# mutS

`gene.b2733`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2733`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutS (gene.b2733) is a gene entity. It encodes mutS (protein.P23909). Encoded protein function: FUNCTION: This protein is involved in the repair of mismatches in DNA. It is possible that it carries out the mismatch recognition step. This protein has a weak ATPase activity. EcoCyc product frame: EG10625-MONOMER. EcoCyc synonyms: ant, plm, fdv. Genomic coordinates: 2857093-2859654. EcoCyc protein note: Purified MutS binds to DNA regions containing a mismatched base pair .

## Biological Role

Repressed by arcZ (gene.b4450), hfq (protein.P0A6X3). Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23909|protein.P23909]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mutS; function=+
- `represses` <-- [[gene.b4450|gene.b4450]] `RegulonDB` `S` - regulator=ArcZ; target=mutS; function=-
- `represses` <-- [[protein.P0A6X3|protein.P0A6X3]] `RegulonDB` `S` - regulator=Hfq; target=mutS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008977,ECOCYC:EG10625,GeneID:947206`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2857093-2859654:+; feature_type=gene
