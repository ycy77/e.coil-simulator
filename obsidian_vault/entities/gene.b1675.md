---
entity_id: "gene.b1675"
entity_type: "gene"
name: "fumD"
source_database: "NCBI RefSeq"
source_id: "gene-b1675"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1675"
  - "fumD"
---

# fumD

`gene.b1675`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1675`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fumD (gene.b1675) is a gene entity. It encodes fumD (protein.P0ACX5). Encoded protein function: FUNCTION: In vitro catalyzes the addition of water to fumarate, forming malate. Cannot catalyze the reverse reaction. Cannot use the cis-isomer maleate as substrate. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: G6903-MONOMER. EcoCyc synonyms: ydhZ. Genomic coordinates: 1754932-1755141. EcoCyc protein note: The fumarase activity of FumD was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . fumD is part of a functional interaction network that includes Fe-S cluster biosynthesis genes. A fumD mutant reaches slightly higher cell density in stationary phase than wild type when growing in media with sublethal levels of streptomycin, an aminoglycoside antibiotic . FumD: "fumarase D"

## Biological Role

Repressed by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), nac (protein.Q47005). Activated by pdhR (protein.P0ACL9).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACX5|protein.P0ACX5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB|EcoCyc` `C` - regulator=PdhR; target=fumD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=fumD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005591,ECOCYC:G6903,GeneID:946180`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1754932-1755141:-; feature_type=gene
