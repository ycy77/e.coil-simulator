---
entity_id: "gene.b1925"
entity_type: "gene"
name: "fliS"
source_database: "NCBI RefSeq"
source_id: "gene-b1925"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1925"
  - "fliS"
---

# fliS

`gene.b1925`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1925`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliS (gene.b1925) is a gene entity. It encodes fliS (protein.P26608). Encoded protein function: Flagellar secretion chaperone FliS EcoCyc product frame: EG11388-MONOMER. Genomic coordinates: 2005303-2005713. EcoCyc protein note: FliS, along with FliT and FlgN, are cytoplasmic, substrate-specific chaperones of the flagellar export system. They share several similarities with other type III cytoplasmic chaperone family members . Mutation-deletion studies have shown that FliS is the chaperone for FliC or flagellin, the subunit which polymerizes to form the filament of the flagellar structure . FliS has also been shown to be responsible for negatively regulating the export of FlgM, the anti-sigma factor . Co-purification and affinity blotting studies showed that FliS binds to the C-terminal 40 amino acid region of the D0 domain of FliC which is the polymerization domain and without FliS binding the C-terminus is degraded. This supports the role of FliS as a domain-specific chaperone that prevents degradation of FliC as well as premature self-aggregation .

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26608|protein.P26608]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006409,ECOCYC:EG11388,GeneID:946429`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2005303-2005713:+; feature_type=gene
