---
entity_id: "gene.b2323"
entity_type: "gene"
name: "fabB"
source_database: "NCBI RefSeq"
source_id: "gene-b2323"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2323"
  - "fabB"
---

# fabB

`gene.b2323`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2323`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabB (gene.b2323) is a gene entity. It encodes fabB (protein.P0A953). Encoded protein function: FUNCTION: Involved in the type II fatty acid elongation cycle. Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Can also use unsaturated fatty acids (PubMed:19679654, PubMed:3076377, PubMed:8910376). Catalyzes a key reaction in unsaturated fatty acid (UFA) synthesis, the elongation of the cis-3-decenoyl-ACP produced by FabA (PubMed:19679654). Can use acyl chains from C-6 to C-14 (PubMed:19679654, PubMed:22017312, PubMed:8910376, PubMed:9013860). Has an absolute requirement for an ACP substrate as the acyl donor, and no activity is detected when both substrates are based on CoA (PubMed:22017312). {ECO:0000269|PubMed:19679654, ECO:0000269|PubMed:22017312, ECO:0000269|PubMed:3076377, ECO:0000269|PubMed:8910376, ECO:0000269|PubMed:9013860}. EcoCyc product frame: FABB-MONOMER. EcoCyc synonyms: fabC. Genomic coordinates: 2440385-2441605.

## Biological Role

Repressed by fabR (protein.P0ACU5). Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A953|protein.P0A953]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fabB; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fabB; function=+
- `represses` <-- [[protein.P0ACU5|protein.P0ACU5]] `RegulonDB` `C` - regulator=FabR; target=fabB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007675,ECOCYC:EG10274,GeneID:946799`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2440385-2441605:-; feature_type=gene
