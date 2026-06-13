---
entity_id: "gene.b2315"
entity_type: "gene"
name: "folC"
source_database: "NCBI RefSeq"
source_id: "gene-b2315"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2315"
  - "folC"
---

# folC

`gene.b2315`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2315`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folC (gene.b2315) is a gene entity. It encodes folC (protein.P08192). Encoded protein function: FUNCTION: Functions in two distinct reactions of the de novo folate biosynthetic pathway. Catalyzes the addition of a glutamate residue to dihydropteroate (7,8-dihydropteroate or H2Pte) to form dihydrofolate (7,8-dihydrofolate monoglutamate or H2Pte-Glu). Also catalyzes successive additions of L-glutamate to tetrahydrofolate or 10-formyltetrahydrofolate or 5,10-methylenetetrahydrofolate, leading to folylpolyglutamate derivatives. {ECO:0000269|PubMed:18232714, ECO:0000269|PubMed:1989505, ECO:0000269|PubMed:2985605}. EcoCyc product frame: FOLC-MONOMER. EcoCyc synonyms: dedC. Genomic coordinates: 2431674-2432942. EcoCyc protein note: During de novo tetrahydrofolate biosynthesis, dihydrofolate synthetase encoded by folC catalyzes the addition of the glutamyl residue to dihydropteroate (7,8-dihydropteroate) to form dihydrofolate (7,8-dihydrofolate monoglutamate) in an ATP-dependent reaction (see pathway PWY-6614). In E. coli FolC is a bifunctional enzyme that also catalyzes the subsequent additions of L-glutamate to tetrahydrofolate (folylpoly-γ-glutamate synthetase activity). This latter activity can also utilize the 10-formyl and methylene derivatives of tetrahydrofolate as substrate (see pathway PWY-2161). The folC gene has been shown to be essential in E...

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08192|protein.P08192]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007645,ECOCYC:EG10327,GeneID:945451`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2431674-2432942:-; feature_type=gene
