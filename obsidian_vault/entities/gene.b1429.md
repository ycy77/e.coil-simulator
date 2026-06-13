---
entity_id: "gene.b1429"
entity_type: "gene"
name: "tehA"
source_database: "NCBI RefSeq"
source_id: "gene-b1429"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1429"
  - "tehA"
---

# tehA

`gene.b1429`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1429`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tehA (gene.b1429) is a gene entity. It encodes tehA (protein.P25396). Encoded protein function: FUNCTION: Responsible for potassium tellurite resistance when present in high copy number. Ion channel involved in potassium tellurite resistance (By similarity). Otherwise, phenotypically silent. {ECO:0000250}. EcoCyc product frame: TEHA-MONOMER. Genomic coordinates: 1500573-1501565. EcoCyc protein note: Overexpression of tehAB from a plasmid confers resistance to tellurite through an unknown mechanism that does not appear to involve reduced uptake or increased efflux . Overexpression of tehA results in hypersensitivity to dequalinium and methyl viologen and resistance to tetraphenylarsonium, ethidium, crystal violet and proflavin . Whole cell experiments indicated that TehA confers ethidium resistance via active efflux. Efflux is inhibited by the ionophore carbonyl cyanide m-chlorophenylhydrazone (CCCP). The addition of tellurite has no effect on ethidium transport in vitro . Overexpression of tehAB protects against tellurite induced dissipation of the transmembrane pH gradient and depletion of intracellular ATP levels . TehA is a member of the tellurite resistance/dicarboxylate (TDT) family of transporters which includes malate transporters. The physiological role of tehA remains elusive.

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25396|protein.P25396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=tehA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004770,ECOCYC:EG11883,GeneID:945852`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1500573-1501565:+; feature_type=gene
