---
entity_id: "gene.b3883"
entity_type: "gene"
name: "yihV"
source_database: "NCBI RefSeq"
source_id: "gene-b3883"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3883"
  - "yihV"
---

# yihV

`gene.b3883`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3883`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihV (gene.b3883) is a gene entity. It encodes yihV (protein.P32143). Encoded protein function: FUNCTION: Phosphorylates 6-deoxy-6-sulfo-D-fructose (SF) to 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) (PubMed:24463506, PubMed:33791429). Cannot phosphorylate fructose 6-phosphate (PubMed:33791429). {ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}. EcoCyc product frame: EG11848-MONOMER. EcoCyc synonyms: squV. Genomic coordinates: 4073739-4074635. EcoCyc protein note: 6-Deoxy-6-sulfofructose kinase (YihV) catalyzes the ATP-dependent phosphorylation of CPD-16501 to CPD-16502 , a part of the PWY-7446 pathway. Expression of YihV is induced by growth on sulfoquinovose , lactose and galactose . A yihV mutant is unable to grow on sulfoquinovose as the sole source of carbon .

## Biological Role

Repressed by csqR (protein.P32144). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32143|protein.P32143]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yihV; function=+
- `represses` <-- [[protein.P32144|protein.P32144]] `RegulonDB` `S` - regulator=CsqR; target=yihV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012681,ECOCYC:EG11848,GeneID:948382`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4073739-4074635:+; feature_type=gene
