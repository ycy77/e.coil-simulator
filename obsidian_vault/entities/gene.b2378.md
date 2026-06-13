---
entity_id: "gene.b2378"
entity_type: "gene"
name: "lpxP"
source_database: "NCBI RefSeq"
source_id: "gene-b2378"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2378"
  - "lpxP"
---

# lpxP

`gene.b2378`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2378`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxP (gene.b2378) is a gene entity. It encodes lpxP (protein.P0ACV2). Encoded protein function: FUNCTION: Catalyzes the transfer of palmitoleate from palmitoleoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(palmitoleoyl)-lipid IV(A). Required for the biosynthesis of a distinct molecular species of lipid A, which is present only in cells grown at low temperatures. It may confer a selective advantage to cells growing at lower temperatures by making the outer membrane a more effective barrier to harmful chemicals. {ECO:0000269|PubMed:10092655, ECO:0000269|PubMed:11830594}. EcoCyc product frame: PALMITOTRANS-MONOMER. EcoCyc synonyms: ddg. Genomic coordinates: 2495645-2496565. EcoCyc protein note: In wild-type E. coli grown at 12°C, two-thirds of the lipid A molecules contain palmitoleate instead of laurate . Palmitoleoyl acyltransferase (LpxP) is the sole enzyme that catalyzes the incorporation of palmitoleate into lipid A in E. coli . lpxP expression is induced by cold shock . An lpxP mutant does not exhibit an obvious growth defect even when grown at 12°C; however, the mutant is hypersensitive to certain antibiotics at low temperatures . A triple lpxL lpxM lpxP mutant lacking all secondary acyl chains of lipid A grows slowly in minimal medium, but is not viable at temperatures above 32°C in rich medium...

## Biological Role

Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACV2|protein.P0ACV2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lpxP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007848,ECOCYC:G7241,GeneID:946847`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2495645-2496565:+; feature_type=gene
