---
entity_id: "gene.b0029"
entity_type: "gene"
name: "ispH"
source_database: "NCBI RefSeq"
source_id: "gene-b0029"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0029"
  - "ispH"
---

# ispH

`gene.b0029`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0029`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispH (gene.b0029) is a gene entity. It encodes ispH (protein.P62623). Encoded protein function: FUNCTION: Catalyzes the conversion of 1-hydroxy-2-methyl-2-(E)-butenyl 4-diphosphate (HMBPP) into a mixture of isopentenyl diphosphate (IPP) and dimethylallyl diphosphate (DMAPP). Acts in the terminal step of the DOXP/MEP pathway for isoprenoid precursor biosynthesis (PubMed:11418107, PubMed:11818558, PubMed:12706830, PubMed:19569147, PubMed:22137895). In vitro, can also hydrate acetylenes to aldehydes and ketones via anti-Markovnikov/Markovnikov addition (PubMed:22948824). {ECO:0000269|PubMed:11418107, ECO:0000269|PubMed:11818558, ECO:0000269|PubMed:12706830, ECO:0000269|PubMed:19569147, ECO:0000269|PubMed:22137895, ECO:0000269|PubMed:22948824}. EcoCyc product frame: EG11081-MONOMER. EcoCyc synonyms: yaaE, lytB. Genomic coordinates: 26277-27227.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62623|protein.P62623]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ispH; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ispH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000103,ECOCYC:EG11081,GeneID:944777`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:26277-27227:+; feature_type=gene
