---
entity_id: "gene.b0428"
entity_type: "gene"
name: "cyoE"
source_database: "NCBI RefSeq"
source_id: "gene-b0428"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0428"
  - "cyoE"
---

# cyoE

`gene.b0428`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0428`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyoE (gene.b0428) is a gene entity. It encodes cyoE (protein.P0AEA5). Encoded protein function: FUNCTION: Converts heme B (protoheme IX) to heme O by substitution of the vinyl group on carbon 2 of heme B porphyrin ring with a hydroxyethyl farnesyl side group. {ECO:0000269|PubMed:1336371, ECO:0000269|PubMed:8253713}. EcoCyc product frame: HEMEOSYN-MONOMER. Genomic coordinates: 446815-447705. EcoCyc protein note: The CyoE protein, heme O synthase, catalyzes the synthesis of heme O, which is essential for the catalytic functions of the cytochrome bo oxidase complex . At one time it was thought that CyoE was a fifth subunit of the cytochrome bo oxidase, but it was shown that a 28 kDa polypeptide which co-purifies with the cytochrome bo oxidase complex appears even in a cyoE deletion strain .

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEA5|protein.P0AEA5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyoE; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=cyoE; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=cyoE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001484,ECOCYC:EG10182,GeneID:945073`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:446815-447705:-; feature_type=gene
