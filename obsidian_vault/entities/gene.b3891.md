---
entity_id: "gene.b3891"
entity_type: "gene"
name: "fdhE"
source_database: "NCBI RefSeq"
source_id: "gene-b3891"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3891"
  - "fdhE"
---

# fdhE

`gene.b3891`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3891`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdhE (gene.b3891) is a gene entity. It encodes fdhE (protein.P13024). Encoded protein function: FUNCTION: Necessary for formate dehydrogenase activity. EcoCyc product frame: EG10284-MONOMER. Genomic coordinates: 4080299-4081228. EcoCyc protein note: FdhE is required for formate dehydrogenase-N enzymatic activity , but not for fdnGHI and fdoGHI transcription. FdhE is not a component of membrane-bound formate dehydrogenase-N itself . FdhE is an iron-binding rubredoxin that interacts with the catalytic molybdoprotein subunits (FdnG, FdoG) of both respiratory formate dehydrogenases, FORMATEDEHYDROGN-CPLX and FORMATEDEHYDROGO-CPLX . FdhE can exist as both a monomer and a homodimer in solution; the dimeric form is stabilized by anaerobiosis. Conserved cysteine residues are involved in ligation of Fe(III) and required for activity of FdhE . Expression of fdhE is sel-dependent and shows Chl- and FNR-dependent nitrate induction .

## Biological Role

Repressed by sdhX (gene.b4764).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13024|protein.P13024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=SdhX; target=fdhE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012703,ECOCYC:EG10284,GeneID:948384`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4080299-4081228:-; feature_type=gene
