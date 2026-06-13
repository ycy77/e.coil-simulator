---
entity_id: "gene.b1062"
entity_type: "gene"
name: "pyrC"
source_database: "NCBI RefSeq"
source_id: "gene-b1062"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1062"
  - "pyrC"
---

# pyrC

`gene.b1062`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1062`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrC (gene.b1062) is a gene entity. It encodes pyrC (protein.P05020). Encoded protein function: FUNCTION: Catalyzes the reversible cyclization of carbamoyl aspartate to dihydroorotate. {ECO:0000255|HAMAP-Rule:MF_00219, ECO:0000269|PubMed:15610022, ECO:0000269|PubMed:6142052}. EcoCyc product frame: DIHYDROOROT-MONOMER. Genomic coordinates: 1121561-1122607.

## Biological Role

Repressed by fur (protein.P0A9A9), purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05020|protein.P05020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pyrC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=pyrC; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=pyrC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003607,ECOCYC:EG10806,GeneID:945787`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1121561-1122607:-; feature_type=gene
