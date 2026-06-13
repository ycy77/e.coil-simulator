---
entity_id: "gene.b2570"
entity_type: "gene"
name: "rseC"
source_database: "NCBI RefSeq"
source_id: "gene-b2570"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2570"
  - "rseC"
---

# rseC

`gene.b2570`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2570`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseC (gene.b2570) is a gene entity. It encodes rseC (protein.P46187). Encoded protein function: FUNCTION: May play a role in reduction of the SoxR iron-sulfur cluster. May work together with the RsxABCDGE complex. {ECO:0000269|PubMed:12773378}. EcoCyc product frame: G7347-MONOMER. Genomic coordinates: 2707322-2707801. EcoCyc protein note: RseC is encoded as the fourth protein of the rpoE-rseABC operon . RseC, along with proteins encoded by the rsxABCDGE operon, may play a role in reduction of the SoxR iron-sulfur cluster . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . RseC may have additional SoxR-independent roles . RseC is predicted to be an inner membrane protein with two transmembrane domains; experimental topology analysis suggests that both the N-terminal and C-terminal domains are located in the cytoplasm . The N-terminal region of RseC contains a conserved cysteine motif (CX2CX5C); the purified N-terminal domain (residues 1-70) can form an oxygen-sensitive Fe-S cluster . Genetic evidence suggests that RseC has a subtle positive effect on σE activity and a minor positive role in the regulation of cell lysis...

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), glnG (protein.P0AFB8), glrR (protein.P0AFU4), rpoE (protein.P0AGB6), rcsB (protein.P0DMC7), rpoS (protein.P13445), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46187|protein.P46187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rseC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rseC; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rseC; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `S` - regulator=GlrR; target=rseC; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rseC; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=rseC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rseC; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rseC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008457,ECOCYC:G7347,GeneID:947052`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2707322-2707801:-; feature_type=gene
