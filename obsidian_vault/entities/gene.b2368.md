---
entity_id: "gene.b2368"
entity_type: "gene"
name: "emrK"
source_database: "NCBI RefSeq"
source_id: "gene-b2368"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2368"
  - "emrK"
---

# emrK

`gene.b2368`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2368`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emrK (gene.b2368) is a gene entity. It encodes emrK (protein.P52599). Encoded protein function: FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}. EcoCyc product frame: G7233-MONOMER. Genomic coordinates: 2482176-2483339. EcoCyc protein note: EmrK is the membrane fusion protein of a putative tripartite efflux pump complex EmrK has 50.45% sequence identity with the EG11354-MONOMER "EmrA" membrane fusion protein . An emrK-lacZ' protein fusion shows increased expression upon prolonged (24hr) incubation with sub-inhibitory concentrations of tetracycline, chloramphenicol or salicylate; EmrAB is implicated in tetracycline efflux . Expression of emrK increases when cells are exposed to 2mM indole emrK was identified in a screen for genes that reduce the lethal effects of stress. An emrK insertion mutant is more sensitive than wild type to mitomycin C and other stresses such as UV irradiation .

## Biological Role

Repressed by nac (protein.Q47005). Activated by evgA (protein.P0ACZ4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52599|protein.P52599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=emrK; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=emrK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007808,ECOCYC:G7233,GeneID:946840`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2482176-2483339:-; feature_type=gene
