---
entity_id: "gene.b1071"
entity_type: "gene"
name: "flgM"
source_database: "NCBI RefSeq"
source_id: "gene-b1071"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1071"
  - "flgM"
---

# flgM

`gene.b1071`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1071`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flgM (gene.b1071) is a gene entity. It encodes flgM (protein.P0AEM4). Encoded protein function: FUNCTION: Responsible for the coupling of flagellin expression to flagellar assembly by preventing expression of the flagellin genes when a component of the middle class of proteins is defective. It negatively regulates flagellar genes by inhibiting the activity of FliA by directly binding to FliA. EcoCyc product frame: G369-MONOMER. Genomic coordinates: 1129835-1130128. EcoCyc protein note: FlgM is an anti-sigma factor that protects its corresponding sigma factor, σ28 (EG11355-MONOMER FliA), against degradation by the Lon protease . FlgM is an intrinsically disordered protein that exists in a pre-molten globule-like conformation . FlgM function has been extensively studied in Salmonella typhimurium. FlgM is an intrinsically disordered protein that becomes structured on binding to the transcription factor σ28, regulating flagellar synthesis . FlgM is produced from both the class 2 transcript of flgAMN and the class 3 transcript of flgMN. FlgM is initially translated from its class 2, FlhDC-activated, σ70-dependent transcript. FlgM is the anti-σ28 factor responsible for regulation of σ28 activity and functions in coupling of flagellar assembly to gene expression. FlgM prevents σ28 from binding to DNA by interacting with its promoter -binding domain...

## Biological Role

Repressed by omrA (gene.b4444), omrB (gene.b4445), csgD (protein.P52106).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEM4|protein.P0AEM4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=flgM; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=flgM; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=flgM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003634,ECOCYC:G369,GeneID:946684`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1129835-1130128:-; feature_type=gene
