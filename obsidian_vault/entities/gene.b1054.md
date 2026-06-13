---
entity_id: "gene.b1054"
entity_type: "gene"
name: "lpxL"
source_database: "NCBI RefSeq"
source_id: "gene-b1054"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1054"
  - "lpxL"
---

# lpxL

`gene.b1054`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1054`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxL (gene.b1054) is a gene entity. It encodes lpxL (protein.P0ACV0). Encoded protein function: FUNCTION: Catalyzes the transfer of laurate from lauroyl-[acyl-carrier-protein] (ACP) to Kdo(2)-lipid IV(A) to form Kdo(2)-(lauroyl)-lipid IV(A). Has 10 fold selectivity for lauroyl-ACP over myristoyl-ACP. In vitro, can also catalyze a slow second acylation reaction leading to the formation of Kdo(2)-(dilauroyl)-lipid IV(A). {ECO:0000269|PubMed:18656959, ECO:0000269|PubMed:2203778, ECO:0000269|PubMed:8662613}. EcoCyc product frame: LAUROYLACYLTRAN-MONOMER. EcoCyc synonyms: htrB, waaM. Genomic coordinates: 1115662-1116582. EcoCyc protein note: Lauroyl acyltransferase (LpxL) transfers laurate from lauroyl acyl carrier protein (ACP) to the free OH group of the 2'-R-3-hydroxymyristoyl chain of the KDO2-lipid IVA. This is one of the last two acylation reactions needed to synthesize KDO2-lipid A . LpxL is an inner membrane protein with a predicted single N-terminal transmembrane helix . LpxL shares sequence homology and functional similarity to LpxM, the final enzyme in the lipid A biosynthetic pathway . A third ortholog, LpxP, is induced below 20°C and competes with LpxL to transfer palmitoleate chain to KDO2-lipid IVA . Distant sequence homology exists between LpxL and the glycerol-3-phosphate acyltransferase (GPAT) family of enzymes...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACV0|protein.P0ACV0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=lpxL; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003574,ECOCYC:EG10464,GeneID:946216`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1115662-1116582:-; feature_type=gene
