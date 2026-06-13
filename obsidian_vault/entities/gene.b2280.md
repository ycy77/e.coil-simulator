---
entity_id: "gene.b2280"
entity_type: "gene"
name: "nuoJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2280"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2280"
  - "nuoJ"
---

# nuoJ

`gene.b2280`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2280`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoJ (gene.b2280) is a gene entity. It encodes nuoJ (protein.P0AFE0). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOJ-MONOMER. Genomic coordinates: 2395342-2395896. EcoCyc protein note: NuoJ is part of the inner membrane component of NADH dehydrogenase I . The protein has five predicted transmembrane domains; the C terminus is located in the cytoplasm . A crystal structure of the membrane component at higher resolution has allowed better identification of the interactions between the subunits . Point mutations at conserved residues have been analyzed; mutation of Val65, which is located in the most conserved transmembrane segment, causes significant reduction of coupled electron transfer activity . Among other site-directed mutants, a V65G mutation had the most deleterious effect on growth on malate and on enzymatic activity...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFE0|protein.P0AFE0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoJ; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoJ; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoJ; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoJ; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoJ; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007536,ECOCYC:EG12090,GeneID:946756`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2395342-2395896:-; feature_type=gene
