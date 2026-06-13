---
entity_id: "gene.b3368"
entity_type: "gene"
name: "cysG"
source_database: "NCBI RefSeq"
source_id: "gene-b3368"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3368"
  - "cysG"
---

# cysG

`gene.b3368`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3368`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysG (gene.b3368) is a gene entity. It encodes cysG (protein.P0AEA8). Encoded protein function: FUNCTION: Multifunctional enzyme that catalyzes the SAM-dependent methylations of uroporphyrinogen III at position C-2 and C-7 to form precorrin-2 via precorrin-1. Then it catalyzes the NAD-dependent ring dehydrogenation of precorrin-2 to yield sirohydrochlorin. Finally, it catalyzes the ferrochelation of sirohydrochlorin to yield siroheme. {ECO:0000255|HAMAP-Rule:MF_01646, ECO:0000269|PubMed:2407234, ECO:0000269|PubMed:2407558, ECO:0000269|PubMed:8243665, ECO:0000269|PubMed:8573073, ECO:0000269|PubMed:9461500}. EcoCyc product frame: SIROHEMESYN-MONOMER. Genomic coordinates: 3497828-3499201.

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), cra (protein.P0ACP1). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEA8|protein.P0AEA8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=cysG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=cysG; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=cysG; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=cysG; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=cysG; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=cysG; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=cysG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011010,ECOCYC:EG10188,GeneID:947880`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3497828-3499201:+; feature_type=gene
