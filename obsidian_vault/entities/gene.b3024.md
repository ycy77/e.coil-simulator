---
entity_id: "gene.b3024"
entity_type: "gene"
name: "ygiW"
source_database: "NCBI RefSeq"
source_id: "gene-b3024"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3024"
  - "ygiW"
---

# ygiW

`gene.b3024`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3024`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiW (gene.b3024) is a gene entity. It encodes ygiW (protein.P0ADU5). Encoded protein function: Protein YgiW EcoCyc product frame: G7574-MONOMER. EcoCyc synonyms: visP. Genomic coordinates: 3169284-3169676. EcoCyc protein note: YgiW is involved in the cellular response to hydrogen peroxide and cadmium stress . YgiW is a member of the bacterial oligonucleotide/oligosaccharide binding fold (BOF) family and contains an N-terminal sginal peptide suggesting that it localizes to the periplasmic space . The homologous S. typhimurium VisP is a virulence- and stress-related protein which binds to peptidoglycan, interacts with the lipid A-modifying enzyme LpxO (not present in E. coli K-12) and inhibits its function . Targeting of YgiW to the Sec-translocase for transport across the inner membrane is SecB-dependent . A ygiW mutant is much more sensitive to hydrogen peroxide and cadmium stress than wild type and shows increased biofilm formation. In a metabolically engineered strain that expresses genes required for the degradation of cis-dichloroethylene (cis-DCE), ygiW expression is induced . Expression of ygiW is reduced in an RpoS K173E mutant compared to wild type .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADU5|protein.P0ADU5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ygiW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009930,ECOCYC:G7574,GeneID:946051`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3169284-3169676:-; feature_type=gene
