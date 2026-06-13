---
entity_id: "gene.b0061"
entity_type: "gene"
name: "araD"
source_database: "NCBI RefSeq"
source_id: "gene-b0061"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0061"
  - "araD"
---

# araD

`gene.b0061`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0061`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araD (gene.b0061) is a gene entity. It encodes araD (protein.P08203). Encoded protein function: FUNCTION: Involved in the degradation of L-arabinose (PubMed:13890280). Catalyzes the interconversion of L-ribulose 5-phosphate (LRu5P) and D-xylulose 5-phosphate (D-Xu5P) via a retroaldol/aldol mechanism (carbon-carbon bond cleavage analogous to a class II aldolase reaction). {ECO:0000255|HAMAP-Rule:MF_00989, ECO:0000269|PubMed:10769138, ECO:0000269|PubMed:10769139, ECO:0000269|PubMed:11732896, ECO:0000269|PubMed:13890280, ECO:0000269|PubMed:4879898, ECO:0000269|PubMed:9548961}. EcoCyc product frame: RIBULPEPIM-MONOMER. Genomic coordinates: 65855-66550. EcoCyc protein note: L-ribulose 5-phosphate 4-epimerase catalyzes the third step in the pathway for degradation of L-arabinose, the epimerization at the C4 carbon to form D-xylulose-5-phosphate, which enters the NONOXIPENT-PWY. The enzyme catalyzes epimerization via a carbon-carbon bond cleavage analogous to a class II aldolase reaction . The H97N and other mutants can catalyze an aldolase reaction . The binding site for Zn2+, the physiological metal cofactor, has been identified by sequence similarity and mutagenesis as well as in the crystal structure . Mutagenesis of the predicted phosphate-binding pocket results in a significant increase in Km, and Asp120 was identified as one of two key catalytic acid/base residues...

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08203|protein.P08203]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araD; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araD; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araD; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000209,ECOCYC:EG10055,GeneID:945294`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:65855-66550:-; feature_type=gene
