---
entity_id: "gene.b0731"
entity_type: "gene"
name: "mngA"
source_database: "NCBI RefSeq"
source_id: "gene-b0731"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0731"
  - "mngA"
---

# mngA

`gene.b0731`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0731`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mngA (gene.b0731) is a gene entity. It encodes mngA (protein.P54745). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:14645248, PubMed:9063979). This system is involved in mannosyl-D-glycerate transport (PubMed:14645248). Also involved in thermoinduction of ompC (PubMed:9063979). {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:9063979}. EcoCyc product frame: HRSA-MONOMER. EcoCyc synonyms: frx, hrsA. Genomic coordinates: 765984-767960. EcoCyc protein note: MngA, a PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in . MngA takes up exogenous 2-O-α-mannosyl-D-glycerate (MG), releasing the phosphate ester into the cell cytoplasm for hydrolysis by the mngB encoded EG13236-MONOMER . E. coli K-12 can use MG as the sole source of carbon. An E. coli ΔmngA strain cannot grow with MG as sole carbon source. MG induces expression of mngA...

## Biological Role

Repressed by mngR (protein.P13669).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P54745|protein.P54745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P13669|protein.P13669]] `RegulonDB` `S` - regulator=MngR; target=mngA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002493,ECOCYC:EG13235,GeneID:945355`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:765984-767960:+; feature_type=gene
