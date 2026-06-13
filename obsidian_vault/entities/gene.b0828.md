---
entity_id: "gene.b0828"
entity_type: "gene"
name: "iaaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0828"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0828"
  - "iaaA"
---

# iaaA

`gene.b0828`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0828`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iaaA (gene.b0828) is a gene entity. It encodes iaaA (protein.P37595). Encoded protein function: FUNCTION: Degrades proteins damaged by L-isoaspartyl residue formation (also known as beta-Asp residues). Degrades L-isoaspartyl-containing di- and maybe also tripeptides. Also has L-asparaginase activity, although this may not be its principal function. {ECO:0000269|PubMed:11988085}.; FUNCTION: May be involved in glutathione, and possibly other peptide, transport, although these results could also be due to polar effects of disruption. {ECO:0000269|PubMed:11988085}. EcoCyc product frame: MONOMER0-3. EcoCyc synonyms: spt, ybiK. Genomic coordinates: 866568-867533.

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37595|protein.P37595]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=iaaA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002828,ECOCYC:EG12407,GeneID:945456`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:866568-867533:+; feature_type=gene
