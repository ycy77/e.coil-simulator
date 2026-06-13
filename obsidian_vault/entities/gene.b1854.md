---
entity_id: "gene.b1854"
entity_type: "gene"
name: "pykA"
source_database: "NCBI RefSeq"
source_id: "gene-b1854"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1854"
  - "pykA"
---

# pykA

`gene.b1854`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1854`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pykA (gene.b1854) is a gene entity. It encodes pykA (protein.P21599). Encoded protein function: FUNCTION: Catalyzes the formation of pyruvate in the last step of glycolysis, it is irreversible under physiological conditions. The reaction is critical for the control of metabolic flux in the second part of glycolysis. {ECO:0000305}. EcoCyc product frame: PKII-MONOMER. Genomic coordinates: 1937649-1939091.

## Biological Role

Repressed by dicF (gene.b1574). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21599|protein.P21599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=pykA; function=+
- `represses` <-- [[gene.b1574|gene.b1574]] `RegulonDB` `S` - regulator=DicF; target=pykA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006182,ECOCYC:EG10803,GeneID:946527`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1937649-1939091:+; feature_type=gene
