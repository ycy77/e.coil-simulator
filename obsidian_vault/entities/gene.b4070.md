---
entity_id: "gene.b4070"
entity_type: "gene"
name: "nrfA"
source_database: "NCBI RefSeq"
source_id: "gene-b4070"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4070"
  - "nrfA"
---

# nrfA

`gene.b4070`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4070`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfA (gene.b4070) is a gene entity. It encodes nrfA (protein.P0ABK9). Encoded protein function: FUNCTION: Catalyzes the reduction of nitrite to ammonia, consuming six electrons in the process (PubMed:11863430, PubMed:18311941, PubMed:20629638, PubMed:9593308). Has very low activity toward hydroxylamine (PubMed:11863430). Has even lower activity toward sulfite (PubMed:20629638). Sulfite reductase activity is maximal at neutral pH (By similarity). {ECO:0000250|UniProtKB:L0DSL2, ECO:0000269|PubMed:11863430, ECO:0000269|PubMed:18311941, ECO:0000269|PubMed:20629638, ECO:0000269|PubMed:9593308, ECO:0000305|PubMed:7934939}. EcoCyc product frame: CYTOCHROMEC552-MONOMER. Genomic coordinates: 4287764-4289200.

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABK9|protein.P0ABK9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfA; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfA; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfA; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfA; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013342,ECOCYC:EG11781,GeneID:948571`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4287764-4289200:+; feature_type=gene
