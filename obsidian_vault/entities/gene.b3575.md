---
entity_id: "gene.b3575"
entity_type: "gene"
name: "yiaK"
source_database: "NCBI RefSeq"
source_id: "gene-b3575"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3575"
  - "yiaK"
---

# yiaK

`gene.b3575`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3575`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiaK (gene.b3575) is a gene entity. It encodes dlgD (protein.P37672). Encoded protein function: FUNCTION: Catalyzes the reduction of 2,3-diketo-L-gulonate in the presence of NADH, to form 3-keto-L-gulonate. {ECO:0000269|PubMed:11741871}. EcoCyc product frame: EG12279-MONOMER. Genomic coordinates: 3742733-3743731. EcoCyc protein note: The yiaK gene encodes a 2,3-diketo-L-gulonate reductase . The enzyme is homodimeric in the crystal structure . A YiaK crystal structure is presented at 2.0 Å resolution, and a structure with NAD and tartrate is presented at 2.2 Å resolution. The His44 residue is predicted to be catalytic. YiaK shows an atypical interaction with NAD . A mutation causing consitutive yiaKLMNO-lyxK-sgbHUE operon expression results in induction of L-lyxose metabolic capability . Regulation has been described .

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37672|protein.P37672]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yiaK; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=yiaK; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yiaK; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=yiaK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011682,ECOCYC:EG12279,GeneID:948096`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3742733-3743731:+; feature_type=gene
