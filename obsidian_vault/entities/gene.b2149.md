---
entity_id: "gene.b2149"
entity_type: "gene"
name: "mglA"
source_database: "NCBI RefSeq"
source_id: "gene-b2149"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2149"
  - "mglA"
---

# mglA

`gene.b2149`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2149`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mglA (gene.b2149) is a gene entity. It encodes mglA (protein.P0AAG8). Encoded protein function: FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:4910389, ECO:0000305|PubMed:6294056, ECO:0000305|PubMed:6807987}. EcoCyc product frame: MGLA-MONOMER. EcoCyc synonyms: mglP, mgl. Genomic coordinates: 2237769-2239289. EcoCyc protein note: MglA is the predicted ATP-binding component of a D-galactose / D-galactoside ABC transporter. mglA mutants are unable to accumulate labeled methyl-β-D-galactopyranoside . mglA+ plasmids direct the synthesis of a 50 kD protein in minicells . mglA contains an ABC-ABC domain

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAG8|protein.P0AAG8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=mglA; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=mglA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mglA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007103,ECOCYC:EG10592,GeneID:949036`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2237769-2239289:-; feature_type=gene
