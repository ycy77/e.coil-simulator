---
entity_id: "gene.b1851"
entity_type: "gene"
name: "edd"
source_database: "NCBI RefSeq"
source_id: "gene-b1851"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1851"
  - "edd"
---

# edd

`gene.b1851`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1851`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

edd (gene.b1851) is a gene entity. It encodes edd (protein.P0ADF6). Encoded protein function: FUNCTION: Catalyzes the dehydration of 6-phospho-D-gluconate to 2-dehydro-3-deoxy-6-phospho-D-gluconate. {ECO:0000255|HAMAP-Rule:MF_02094, ECO:0000269|PubMed:17102132, ECO:0000269|PubMed:1846355}. EcoCyc product frame: PGLUCONDEHYDRAT-MONOMER. Genomic coordinates: 1932793-1934604. EcoCyc protein note: Phosphogluconate dehydratase catalyzes the dehydration of D-gluconate 6-phosphate to 2-dehydro-3-deoxy-D-gluconate 6-phosphate. This is the first reaction of the ENTNER-DOUDOROFF-PWY " Entner-Doudoroff pathway" which constitutes the primary route of gluconate metabolism in E. coli. Phosphogluconate dehydratase is induced by growth of cells on gluconate . The enzyme is sensitive to oxidants such as superoxide and hydrogen peroxide due to its [4Fe-4S] iron-sulfur cluster content. It is also inactivated by iron chelators and thiol-reactive compounds. Fluoride ions protect the enzyme from the effects of oxidants . Under continuous culture conditions induction of phosphogluconate dehydratase is favored at low oxygen concentrations . Edd from E. coli K-12, a laboratory strain, has not been well characterized biochemically. However, using E...

## Biological Role

Repressed by cra (protein.P0ACP1), gntR (protein.P0ACP5). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rpoD (protein.P00579).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADF6|protein.P0ADF6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=edd; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=edd; function=-
- `represses` <-- [[protein.P0ACP5|protein.P0ACP5]] `RegulonDB` `S` - regulator=GntR; target=edd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006166,ECOCYC:EG10257,GeneID:946362`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1932793-1934604:-; feature_type=gene
