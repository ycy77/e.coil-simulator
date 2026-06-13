---
entity_id: "gene.b1923"
entity_type: "gene"
name: "fliC"
source_database: "NCBI RefSeq"
source_id: "gene-b1923"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1923"
  - "fliC"
---

# fliC

`gene.b1923`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1923`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliC (gene.b1923) is a gene entity. It encodes fliC (protein.P04949). Encoded protein function: FUNCTION: Flagellin is the subunit protein which polymerizes to form the filaments of bacterial flagella. EcoCyc product frame: EG10321-MONOMER. EcoCyc synonyms: H, flaF, hag. Genomic coordinates: 2002110-2003606. EcoCyc protein note: FliC, or flagellin, is the basic subunit that polymerizes to form the rigid flagellar filament of Escherichia coli. fliC was found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see . The 'pole-localizer' protein G7087-MONOMER TmaR protects and stabilizes fliA transcripts .

## Biological Role

Repressed by uxuR (protein.P39161), ecpR (protein.P71301), nac (protein.Q47005). Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04949|protein.P04949]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliC; function=+
- `represses` <-- [[protein.P39161|protein.P39161]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=fliC; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=fliC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006402,ECOCYC:EG10321,GeneID:949101`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2002110-2003606:-; feature_type=gene
