---
entity_id: "gene.b0002"
entity_type: "gene"
name: "thrA"
source_database: "NCBI RefSeq"
source_id: "gene-b0002"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0002"
  - "thrA"
---

# thrA

`gene.b0002`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0002`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thrA (gene.b0002) is a gene entity. It encodes thrA (protein.P00561). Encoded protein function: FUNCTION: Bifunctional aspartate kinase and homoserine dehydrogenase that catalyzes the first and the third steps toward the synthesis of lysine, methionine and threonine from aspartate. {ECO:0000250|UniProtKB:Q9SA18}. EcoCyc product frame: ASPKINIHOMOSERDEHYDROGI-MONOMER. EcoCyc synonyms: thrA2, Hs, thrA1, thrD. Genomic coordinates: 337-2799.

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00561|protein.P00561]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=thrA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=thrA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=thrA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000008,ECOCYC:EG10998,GeneID:945803`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:337-2799:+; feature_type=gene
