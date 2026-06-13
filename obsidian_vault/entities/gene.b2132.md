---
entity_id: "gene.b2132"
entity_type: "gene"
name: "bglX"
source_database: "NCBI RefSeq"
source_id: "gene-b2132"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2132"
  - "bglX"
---

# bglX

`gene.b2132`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2132`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bglX (gene.b2132) is a gene entity. It encodes bglX (protein.P33363). Encoded protein function: Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) EcoCyc product frame: EG12013-MONOMER. EcoCyc synonyms: glh, yohA. Genomic coordinates: 2219692-2221989. EcoCyc protein note: bglX is predicted to encode a periplasmic β-glucosidase/β-galactosidase; the purified enzyme can hydrolyse artifical substrates (o-nitrophenyl-β-D-glucopyranoside, p-nitrophenyl-β-D-glucopyranoside, and o-nitrophenyl-β-D-galactopyranoside) with varying kinetics; it can also hydrolyse lactose (but not cellobiose, maltose or laminarin) . No obvious phenotype is associated with deletion or overexpression , and the physiological function of the enzyme remains uncertain. In the CAZy database, BglX is a Glycoside Hydrolase Family 3 (GH3) enzyme .

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00946` Degradation of flavonoids (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33363|protein.P33363]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=bglX; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007043,ECOCYC:EG12013,GeneID:946682`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2219692-2221989:-; feature_type=gene
