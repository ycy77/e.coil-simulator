---
entity_id: "gene.b0881"
entity_type: "gene"
name: "clpS"
source_database: "NCBI RefSeq"
source_id: "gene-b0881"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0881"
  - "clpS"
---

# clpS

`gene.b0881`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0881`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clpS (gene.b0881) is a gene entity. It encodes clpS (protein.P0A8Q6). Encoded protein function: FUNCTION: Involved in the modulation of the specificity of the ClpAP-mediated ATP-dependent protein degradation. {ECO:0000255|HAMAP-Rule:MF_00302, ECO:0000269|PubMed:11931773}. EcoCyc product frame: G6463-MONOMER. EcoCyc synonyms: yljA. Genomic coordinates: 922913-923233. EcoCyc protein note: ClpS is a specificity adapter for the CPLX0-3104 protease complex, targeting it to aggregated proteins, N-end rule substrates, and others. ClpS binds to the ClpA amino-terminus and affects the specificity of protein degradation by the ClpAP chaperone-protease complex, possibly by interfering with interactions between substrate and ClpA . ClpS stimulates ClpAP recognition and degradation of aggregated protein substrates while it inhibits degradation of non-aggregated substrates, including ClpA . ClpS also links ClpAP to the N-end rule degradation pathway, binding to the amino-terminal destabilizing residues in N-end substrates and targeting those substrates for degradation by ClpAP . A mutant protein lacking the flexible 17 amino-terminal residues shows a defect in ClpA inhibition but does not show a defect in interaction with ClpA . Binding of ClpA and ClpS requires ClpS residues E79 and K84, as does proteolytic activity by the ClpAPS complex...

## Biological Role

Repressed by phoP (protein.P23836). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Q6|protein.P0A8Q6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=clpS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002998,ECOCYC:G6463,GeneID:948443`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:922913-923233:+; feature_type=gene
