---
entity_id: "gene.b2465"
entity_type: "gene"
name: "tktB"
source_database: "NCBI RefSeq"
source_id: "gene-b2465"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2465"
  - "tktB"
---

# tktB

`gene.b2465`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2465`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tktB (gene.b2465) is a gene entity. It encodes tktB (protein.P33570). Encoded protein function: FUNCTION: Catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. {ECO:0000269|PubMed:8396116}. EcoCyc product frame: TRANSKETOII-MONOMER. Genomic coordinates: 2579636-2581639. EcoCyc protein note: Transketolase catalyzes the reversible transfer of a ketol group between several donor and acceptor substrates. This key enzyme is a reversible link between glycolysis and the pentose phosphate pathway. The enzyme is involved in the catabolism of pentose sugars, the formation of D-ribose 5-phosphate, and the provision of D-erythrose 4-phosphate, a precursor of aromatic amino acids and PLP . E. coli contains two transketolase isozymes, TktA and TktB. TktB is responsible for the minor transketolase activity . The subunit structure of transketolase 2 (TktB) has not been explicitly determined. However, transketolase 1 (TktA) is homodimeric . Overproduction of TktB suppresses the tktA mutant phenotype...

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33570|protein.P33570]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=tktB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008117,ECOCYC:EG12100,GeneID:945865`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2579636-2581639:+; feature_type=gene
