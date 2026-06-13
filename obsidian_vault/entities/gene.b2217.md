---
entity_id: "gene.b2217"
entity_type: "gene"
name: "rcsB"
source_database: "NCBI RefSeq"
source_id: "gene-b2217"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2217"
  - "rcsB"
---

# rcsB

`gene.b2217`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2217`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcsB (gene.b2217) is a gene entity. It encodes rcsB (protein.P0DMC7). Encoded protein function: FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsB is the response regulator that binds to regulatory DNA regions. Can function both in an RcsA-dependent or RcsA-independent manner. The system regulates expression of numerous genes, including genes involved in colanic acid capsule synthesis, biofilm formation, cell division and outer membrane proteins synthesis. Also involved, with GadE, in control of glutamate-dependent acid resistance, and, with BglJ, in derepression of the cryptic bgl operon. The RcsB-BglJ activity is probably independent of RcsB phosphorylation. {ECO:0000255|HAMAP-Rule:MF_00981, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11566985, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:1597415, ECO:0000269|PubMed:20189963, ECO:0000269|PubMed:20952573}. EcoCyc product frame: MONOMER0-4556. Genomic coordinates: 2316177-2316827. EcoCyc protein note: RcsB protein for "Regulator capsule synthesis B," is a response regulator that belongs to the multicomponent RcsF/RcsC/RcsD/RcsA-RcsB phosphorelay system and is involved in the regulation of the synthesis of colanic acid capsule, cell division, periplasmic proteins, motility, biofilm formation, and a small RNA...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DMC7|protein.P0DMC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rcsB; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=rcsB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007333,ECOCYC:EG10821,GeneID:947441`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2316177-2316827:+; feature_type=gene
