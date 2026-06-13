---
entity_id: "gene.b1500"
entity_type: "gene"
name: "safA"
source_database: "NCBI RefSeq"
source_id: "gene-b1500"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1500"
  - "safA"
---

# safA

`gene.b1500`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1500`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

safA (gene.b1500) is a gene entity. It encodes safA (protein.P76136). Encoded protein function: FUNCTION: Connects the signal transduction between the two-component systems EvgS/EvgA and PhoQ/PhoP, by directly interacting with PhoQ and thus activating the PhoQ/PhoP system, in response to acid stress conditions (PubMed:17998538). Activates the PhoQ/PhoP system by increasing autophosphorylation of PhoQ, thereby leading to the accumulation of phospho-PhoP (PubMed:23563556). {ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:23563556}. EcoCyc product frame: MONOMER0-2841. EcoCyc synonyms: yneN. Genomic coordinates: 1583762-1583959. EcoCyc protein note: SafA is a small membrane protein that functions to connect the the PWY0-1490 "EvgS/EvgA" and PWY0-1458 "PhoQ/PhoP" two component systems; activation of the EvgS/EvgA system induces SafA which in turn activates the PhoQ/PhoP system to induce PhoP regulated genes (see ). SafA contributes to a complex network of acid resistance gene regulation (see ). safA forms an operon with ydeO; safA-ydeO is a member of the EvgA regulon ; safA-ydeO is up-regulated when the EvgS/EvgA two-component system is activated . Deletion of safA results in a slight decrease in survival at pH 2.5 . Expression of safA from a heterologous promoter activates expression of PhoP regulon genes (eg mgtA, mgrB, rstAB, slyB and others) in a PhoQ/PhoP dependent manner...

## Biological Role

Repressed by phoP (protein.P23836). Activated by evgA (protein.P0ACZ4), glaR (protein.P37338).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76136|protein.P76136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=safA; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=safA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=safA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004994,ECOCYC:G6790,GeneID:946061`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1583762-1583959:-; feature_type=gene
