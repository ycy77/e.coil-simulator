---
entity_id: "gene.b2065"
entity_type: "gene"
name: "dcd"
source_database: "NCBI RefSeq"
source_id: "gene-b2065"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2065"
  - "dcd"
---

# dcd

`gene.b2065`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2065`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcd (gene.b2065) is a gene entity. It encodes dcd (protein.P28248). Encoded protein function: FUNCTION: Catalyzes the deamination of dCTP to dUTP. {ECO:0000255|HAMAP-Rule:MF_00146, ECO:0000269|PubMed:1324907, ECO:0000269|PubMed:15539408, ECO:0000269|PubMed:17651436, ECO:0000269|PubMed:17996716}. EcoCyc product frame: DCTP-DEAM-MONOMER. EcoCyc synonyms: dus, paxA. Genomic coordinates: 2141634-2142215. EcoCyc protein note: dCTP deaminase (Dcd) catalyzes the deamination of dCTP to dUTP in the main pathway for dTTP biosynthesis in E. coli, PWY-7187 . dCTP deaminase is unusual among nucleoside and nucleotide deaminases in that it does not require a metal ion for catalysis. Crystal structures of wild-type and mutant forms of the enzyme in complexes with the substrate, product or inhibitor have been determined . Site-directed mutagenesis of predicted active site residues produced catalytically inactive enzymes . The true substrate of dCTP deaminase appears to be the dCTP·Mg2+ complex; a catalytic mechanism was proposed . Mutations in the S111 and E138 residues alter the enzyme's inhibition by dTTP . dcd mutants require thymidine supplementation for optimal growth. deoA mutations bypass the requirement for thymidine supplementation by enabling diversion of an intermediate of the PWY0-181...

## Biological Role

Activated by rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28248|protein.P28248]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `S` - regulator=RbsR; target=dcd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006835,ECOCYC:EG11418,GeneID:946593`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2141634-2142215:-; feature_type=gene
