---
entity_id: "gene.b1622"
entity_type: "gene"
name: "malY"
source_database: "NCBI RefSeq"
source_id: "gene-b1622"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1622"
  - "malY"
---

# malY

`gene.b1622`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1622`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malY (gene.b1622) is a gene entity. It encodes malY (protein.P23256). Encoded protein function: FUNCTION: Acts as a beta-cystathionase and as a repressor of the maltose regulon. EcoCyc product frame: EG10564-MONOMER. Genomic coordinates: 1700957-1702129.

## Biological Role

Repressed by malI (protein.P18811), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23256|protein.P23256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malY; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malY; function=+
- `represses` <-- [[protein.P18811|protein.P18811]] `RegulonDB` `S` - regulator=MalI; target=malY; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=malY; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005432,ECOCYC:EG10564,GeneID:945937`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1700957-1702129:+; feature_type=gene
