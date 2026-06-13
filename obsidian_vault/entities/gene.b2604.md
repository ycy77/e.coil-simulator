---
entity_id: "gene.b2604"
entity_type: "gene"
name: "dgcN"
source_database: "NCBI RefSeq"
source_id: "gene-b2604"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2604"
  - "dgcN"
---

# dgcN

`gene.b2604`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2604`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcN (gene.b2604) is a gene entity. It encodes dgcN (protein.P46139). Encoded protein function: FUNCTION: Bifunctional protein that catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) in response to reductive stress and then dynamically relocates to the division site to arrest cell division in response to envelope stress. In the presence of high intracellular c-di-GMP levels, and in response to envelope stress, interacts with cell division proteins and halts cell division, without disassembling the Z ring, but by blocking its further progress toward cytokinesis (PubMed:27507823). Part of a network that regulates cell motility by altering levels of c-di-GMP (PubMed:20303158). {ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:27507823}. EcoCyc product frame: EG12880-MONOMER. EcoCyc synonyms: yfiN. Genomic coordinates: 2742383-2743609. EcoCyc protein note: DgcN is a diguanylate cyclase (DGC) that dynamically relocates to the division site in response to envelope stress. DgcN localizes to the Z ring in an FtsZ- and ZipA-dependent manner in the presence of high levels of c-di-GMP. G7354-MONOMER YfiR counteracts relocation of DgcN to the Z ring...

## Biological Role

Repressed by glaR (protein.P37338). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46139|protein.P46139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dgcN; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dgcN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008570,ECOCYC:EG12880,GeneID:947091`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2742383-2743609:+; feature_type=gene
