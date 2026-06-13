---
entity_id: "gene.b4079"
entity_type: "gene"
name: "fdhF"
source_database: "NCBI RefSeq"
source_id: "gene-b4079"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4079"
  - "fdhF"
---

# fdhF

`gene.b4079`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4079`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdhF (gene.b4079) is a gene entity. It encodes fdhF (protein.P07658). Encoded protein function: FUNCTION: Decomposes formic acid to hydrogen and carbon dioxide under anaerobic conditions in the absence of exogenous electron acceptors. EcoCyc product frame: FORMATEDEHYDROGH-MONOMER. EcoCyc synonyms: chlF. Genomic coordinates: 4297219-4299366. EcoCyc protein note: Formate dehydrogenase-H is one of three membrane-associated formate dehydrogenase isoenzymes in E. coli . All are functional in the anaerobic metabolism of the organism. Formate dehydrogenase-H (FDH-H) is located in the cytoplasm and together with hydrogenase-3, FDH-H forms the formate-hydrogen lyase complex . FDH-H plays a role in the formate-dependent catabolism of urate . The enzyme is oxygen sensitive and contains selenium as selenocysteine incorporated cotranslationally at the position of an in-frame UGA stop codon in the FdhF open reading frame . fdhF mRNA contains a cis-acting element - the selenocysteine insertion sequence (SECIS) - which in combination with the specialized elongation factor CPLX0-8053 SelB is required for UGA-directed selenocysteine incorporation (and see ). A crystal structure of FDH-H has been solved at 2...

## Biological Role

Repressed by narL (protein.P0AF28). Activated by fhlA (protein.P19323).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07658|protein.P07658]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=fdhF; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=fdhF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013363,ECOCYC:EG10285,GeneID:948584`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4297219-4299366:-; feature_type=gene
