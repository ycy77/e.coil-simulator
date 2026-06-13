---
entity_id: "gene.b0734"
entity_type: "gene"
name: "cydB"
source_database: "NCBI RefSeq"
source_id: "gene-b0734"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0734"
  - "cydB"
---

# cydB

`gene.b0734`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0734`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cydB (gene.b0734) is a gene entity. It encodes cydB (protein.P0ABK2). Encoded protein function: FUNCTION: A terminal oxidase that produces a proton motive force by the vectorial transfer of protons across the inner membrane. It is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at low aeration. Generates a proton motive force using protons and electrons from opposite sides of the membrane to generate H(2)O, transferring 1 proton/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:21987791, ECO:0000269|PubMed:6307994}. EcoCyc product frame: CYDB-MONOMER. EcoCyc synonyms: cyd-2. Genomic coordinates: 773042-774181. EcoCyc protein note: cydB encodes subunit II of the cytochrome bd-I complex. Subunit II has eight predicted transmembrane helices; the N and C-termini are located in the cytoplasm ; in the bd-I complex, the subunit forms two four-helix bundles with an additional peripheral helix . Subunit I (encoded by cydA) and subunit II are both required for binding of the heme b595 and heme d components of cytochrome bd-I . In the cryo-EM structure of the bd-I complex reported by , CydB binds a structural ubiquinone-8 cofactor that may have a role in CydAB dimer assembly (see also ).

## Biological Role

Repressed by fnr (protein.P0A9E5), hns (protein.P0ACF8). Activated by fnr (protein.P0A9E5), cra (protein.P0ACP1), yjiE (protein.P39376).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABK2|protein.P0ABK2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=cydB; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=cydB; function=+
- `activates` <-- [[protein.P39376|protein.P39376]] `RegulonDB` `S` - regulator=HypT; target=cydB; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=cydB; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=cydB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002501,ECOCYC:EG10174,GeneID:945347`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:773042-774181:+; feature_type=gene
