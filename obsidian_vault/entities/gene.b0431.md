---
entity_id: "gene.b0431"
entity_type: "gene"
name: "cyoB"
source_database: "NCBI RefSeq"
source_id: "gene-b0431"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0431"
  - "cyoB"
---

# cyoB

`gene.b0431`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0431`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyoB (gene.b0431) is a gene entity. It encodes cyoB (protein.P0ABI8). Encoded protein function: FUNCTION: Cytochrome bo(3) ubiquinol oxidase is the terminal enzyme in the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Catalyzes the four-electron reduction of O2 to water, using a ubiquinol as a membrane soluble electron donor for molecular oxygen reduction; ubiquinol-8 is the natural substrate for E.coli. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron and generating a proton motive force. All the redox centers of this enzyme complex are located within the largest subunit, subunit I. Protons are probably pumped via D- and K- channels found in this subunit (PubMed:11017202). {ECO:0000269|PubMed:11017202, ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. EcoCyc product frame: CYOB-MONOMER. Genomic coordinates: 448650-450641. EcoCyc protein note: cyoB encodes subunit I of the cytochrome bo complex. The three prosthetic groups (heme O, heme B and CuB) are located in subunit 1 and are liganded by conserved histidine residues: His106 and His421 for heme B; His419 for heme O; His284, His333 and His334 for CuB ( and reviewed in ). The 3.5Å crystal structure confirmed these assignments...

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABI8|protein.P0ABI8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyoB; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=cyoB; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=cyoB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001493,ECOCYC:EG10179,GeneID:945615`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:448650-450641:-; feature_type=gene
