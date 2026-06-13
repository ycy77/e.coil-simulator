---
entity_id: "gene.b0432"
entity_type: "gene"
name: "cyoA"
source_database: "NCBI RefSeq"
source_id: "gene-b0432"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0432"
  - "cyoA"
---

# cyoA

`gene.b0432`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0432`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyoA (gene.b0432) is a gene entity. It encodes cyoA (protein.P0ABJ1). Encoded protein function: FUNCTION: Cytochrome bo(3) ubiquinol terminal oxidase is the component of the aerobic respiratory chain of E.coli that predominates when cells are grown at high aeration. Has proton pump activity across the membrane in addition to electron transfer, pumping 2 protons/electron. {ECO:0000269|PubMed:19542282, ECO:0000269|PubMed:22843529, ECO:0000269|PubMed:6308657}. EcoCyc product frame: CYOA-MONOMER. Genomic coordinates: 450663-451610. EcoCyc protein note: CyoA is subunit II of the 4 subunit cytochrome bo complex. CyoA was initially suggested to contain one of two ubiquinone binding sites; current work suggests that the complex contains only one binding site located in subunit I (CyoB) . CyoA consists of two domains - an N terminal domain containing two transmembrane helices and a large C-terminal domain located in the periplasm . CyoA is a lipoprotein; during maturation, the protein is modified by attachment of fatty acids and protease cleavage at C25. The addition of [14C]palmitic acid to the growth medium results in covalent labeling of CyoA with the fatty acid. A C25A mutation blocks lipoprotein processing but the protein retains oxidase activity suggesting that posttranslational modification is not essential for assembly or activity of the cytochrome bo terminal oxidase complex...

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABJ1|protein.P0ABJ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyoA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=cyoA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=cyoA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001495,ECOCYC:EG10178,GeneID:945080`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:450663-451610:-; feature_type=gene
