---
entity_id: "gene.b1855"
entity_type: "gene"
name: "lpxM"
source_database: "NCBI RefSeq"
source_id: "gene-b1855"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1855"
  - "lpxM"
---

# lpxM

`gene.b1855`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1855`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxM (gene.b1855) is a gene entity. It encodes lpxM (protein.P24205). Encoded protein function: FUNCTION: Catalyzes the transfer of myristate from myristoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-(lauroyl)-lipid IV(A) to form Kdo(2)-lipid A. Can probably also catalyze the transfer of myristate to Kdo(2)-(palmitoleoyl)-lipid IV(A) to form the cold-adapted Kdo(2)-lipid A. In vitro, can acylate Kdo(2)-lipid IV(A), but acylation of (KDO)2-(lauroyl)-lipid IV(A) is about 100 times faster. In vitro, can use lauroyl-ACP but displays a slight kinetic preference for myristoyl-ACP. {ECO:0000269|PubMed:9099672, ECO:0000305|PubMed:10092655}. EcoCyc product frame: MYRISTOYLACYLTRAN-MONOMER. EcoCyc synonyms: mlt, waaN, msbB. Genomic coordinates: 1939222-1940193. EcoCyc protein note: Myristoyl-acyl carrier protein (ACP)-dependent acyltransferase (LpxM) catalyzes the transfer of myristate from myristoyl-ACP to the 3'-R-3-hydroxymyristoyl chain of KDO2-(lauroyl)-lipid IVA. This is one of the last two acylation reactions needed to synthesize KDO2-lipid A. LpxM functions optimally after laurate incorporation by LpxL has taken place . LpxM shares sequence homology and functional similarity to LpxL . Mutants of lpxM are characterized by attenuated cytokine induction and with an LPS that lacked the myristoyl fatty acid moiety of the lipid A...

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24205|protein.P24205]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006185,ECOCYC:EG10614,GeneID:945143`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1939222-1940193:-; feature_type=gene
