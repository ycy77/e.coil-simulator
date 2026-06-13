---
entity_id: "gene.b3491"
entity_type: "gene"
name: "yhiM"
source_database: "NCBI RefSeq"
source_id: "gene-b3491"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3491"
  - "yhiM"
---

# yhiM

`gene.b3491`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3491`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhiM (gene.b3491) is a gene entity. It encodes yhiM (protein.P37630). Encoded protein function: Inner membrane protein YhiM EcoCyc product frame: MONOMER0-2489. Genomic coordinates: 3634841-3635893. EcoCyc protein note: Expression of yhiM is negatively regulated by trimethylamine N-oxide (TMAO) via the TorR transcriptional regulator . Expression of yhiM is induced under acid stress . Transposon insertion mutants of E.coli yhiM are unable to grow at pH 2.5 . YhiM is necessary for RpoS, glutamine and lysine-dependent acid resistance but is not required for arginine-dependent acid resistance . YhiM is predicted to be an inner membrane protein with ten membrane spanning domains; experimental topology analysis suggests the C terminus is located in the cytoplasm .

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0). Activated by gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37630|protein.P37630]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=yhiM; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=yhiM; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011400,ECOCYC:EG12228,GeneID:947997`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3634841-3635893:+; feature_type=gene
